# setup.py

import setuptools

setuptools.setup(
    name='cryptonit-bot',
    version='1.0.1',
    description="A bot for encryption and decryption using Telegram",
    author="кгідфтдфз",  # Replace with your actual name
    packages=setuptools.find_packages(),
    install_requires=open('cryptonit_bot/requirements.txt').readlines(),
    entry_points={
        'console_scripts': [
            'cryptonit-bot=cryptonit_bot.bot:run_bot',
        ],
    },
)