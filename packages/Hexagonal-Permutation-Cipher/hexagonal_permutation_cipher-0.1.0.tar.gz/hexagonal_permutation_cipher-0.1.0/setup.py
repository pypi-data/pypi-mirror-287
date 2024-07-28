from setuptools import setup, find_packages

setup(
    name='hexagonal_permutation_cipher',
    version='0.1.0',
    description='A hexagonal permutation cipher with AES encryption.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Joseph Webster C',
    author_email='rwc.webster@gmail.com',
    url='https://github.com/00-python/hexagonal_permutation_cipher',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'numpy',
        'pycryptodome',
        'pygame',
    ],
    extras_require={
        'dev': [
            'pytest',
            'flake8',
            'black',
        ],
    },
    entry_points={
        'console_scripts': [
            'hexagonal-permutation-cipher=hexagonal_permutation_cipher.__main__:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)