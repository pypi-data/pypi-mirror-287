from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='ENSCardMaker',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'enscardmaker=ENSCardMaker.__main__:main',
        ],
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
)