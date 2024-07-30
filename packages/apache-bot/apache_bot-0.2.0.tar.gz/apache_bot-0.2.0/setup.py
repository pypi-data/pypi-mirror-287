from setuptools import setup, find_packages

setup(
    name="apache_bot",
    version="0.2.0",
    author="Ivan",
    author_email="your.email@example.com",
    description="A brief description of your project",
    url="https://github.com/yourusername/your_project",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "python-telegram-bot",
        "paramiko",
    ],
    entry_points={
        'console_scripts': [
            'bot=bot.scripts.bot:main',  
        ],
    },
)
