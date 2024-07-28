from setuptools import setup, find_packages

# Read the content of README.md
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mformodal',
    version='1.0.0',  # Changed to a standard version format
    packages=find_packages(),
    install_requires=[
        'discord.py',
    ],
    author='sforskeezy | sforskeezy.com',
    author_email='sforskeezy@sforskeezy.com',
    description='A simple package to create Discord modals',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sforskeezy/mformodal',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Add this if you're using MIT License
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
)