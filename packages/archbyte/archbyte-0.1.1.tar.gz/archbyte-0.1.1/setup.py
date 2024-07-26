from setuptools import setup, find_packages

setup(
    name='archbyte',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'flask',
        'telethon',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            # Define command line scripts here if necessary
        ],
    },
    author='Arch Byte',
    author_email='cophtew@gmail.com',
    description='Telegram  , discord and Ai focused library ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/archbyte',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
