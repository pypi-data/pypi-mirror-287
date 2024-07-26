import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='cryptonit-bot',
    version='1.2.2',
    description="A bot for encryption and decryption using Telegram",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="ruslanlap",  # Replace with your actual name
    author_email="your-email@example.com",  # Replace with your actual email
    url="https://github.com/your-username/cryptonit-bot",  # Replace with your actual repository URL
    packages=setuptools.find_packages(),
    install_requires=[req.strip() for req in open('cryptonit_bot/requirements.txt')],
    entry_points={
        'console_scripts': [
            'cryptonit-bot=cryptonit_bot.bot:run_bot',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
