from setuptools import setup, find_packages

setup(
    name='fs_store_cli',
    version='1.0',
    license='proprietary',
    description='A CLI tool to interact with the file server',
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'os'
    ],
    entry_points={
        'console_scripts': [
            'fs-store=fs_store_cli.cli:cli',
        ],
    },
    author='Gajendra Waghmare',
    author_email='gajendraw1237@gmail.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
