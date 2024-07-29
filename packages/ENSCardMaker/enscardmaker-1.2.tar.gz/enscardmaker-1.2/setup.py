from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='ENSCardMaker',
    version='1.2',
    description='Takes an ENS name or ETH address and returns a card based on information from an ENS profile.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='LittleBit',
    author_email='littlebit@littlebitstudios.com',
    license='MIT',
    license_files='LICENSE',
    packages=find_packages(),
    install_requires=[
        'requests',
        'Pillow',
        'pydenticon'
    ],
    entry_points={
        'console_scripts': [
            'enscardmaker=ENSCardMaker:main',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
