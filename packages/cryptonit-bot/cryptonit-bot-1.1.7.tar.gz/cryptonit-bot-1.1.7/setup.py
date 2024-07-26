# setup.py

import setuptools

setuptools.setup(
    name='cryptonit-bot',
    version='1.1.7',
    description="A bot for encryption and decryption using Telegram",
    author="ruslanlap",  # Replace with your actual name
    packages=setuptools.find_packages(),
    install_requires=open('cryptonit_bot/requirements.txt').readlines(),
    entry_points={
        'console_scripts': [
            'cryptonit-bot=cryptonit_bot.bot:run_bot',
        ],
    },
)