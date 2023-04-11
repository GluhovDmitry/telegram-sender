from setuptools import setup, find_packages

setup(
    name='telegram_send_api',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tg_api=main:main',
        ]
    },
)
