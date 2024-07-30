import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import paramiko
from paramiko import SSHClient, AutoAddPolicy

from bot import config
from bot.sites import SITES


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


COMMANDS = {
    "check": "httpd -t",
    "restart": "systemctl restart httpd"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton(site, callback_data=site)] for site in SITES.keys()    
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Выберите сайт для выполнения действия:", reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query    
    await query.answer()
    site_name = query.data

    keyboard = [
        [InlineKeyboardButton("Перезапуск Apache", callback_data=f"{site_name}_restart")],
        [InlineKeyboardButton("Проверка конфигурации Apache", callback_data=f"{site_name}_check")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=f"Вы выбрали '{site_name}'. Что вы хотите сделать?",
        reply_markup=reply_markup
    )

async def execute_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data.split("_")
    site_name = data[0]
    action = data[1]

    site_info = SITES[site_name]
    hostname = site_info["hostname"]    
    port = site_info["port"]
    username = site_info["username"]    
    key = site_info["key"]
    command = COMMANDS[action]

    try:
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(hostname, port, username, key)

        stdin, stdout, stderr = client.exec_command(command)
        stdout_str = stdout.read().decode()
        stderr_str = stderr.read().decode()

        if action == "restart":
            await query.edit_message_text(
                text=f"Apache для сайта '{site_name}' успешно перезагружен."
            )
        elif action == "check":
            output_msg = stdout_str if not stderr_str else stderr_str
            await query.edit_message_text(
                text=f"Результат проверки конфигурации для сайта '{site_name}':\n{output_msg}"
            )
        
        client.close()

    except Exception as e:
        await query.edit_message_text(
            text=f"Произошла ошибка при попытке подключения к серверу: {str(e)}"
        )

    await start_over(update, context)

async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton(site, callback_data=site)] for site in SITES.keys()    
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.reply_text(
        "Выберите сайт для выполнения действия:", reply_markup=reply_markup
    )

def main() -> None:
    application = Application.builder().token(config.BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button, pattern="^[^_]+$"))
    application.add_handler(CallbackQueryHandler(execute_command, pattern="^[^_]+_(check|restart)$"))
    application.run_polling()


if __name__ == "__main__":
    main()

