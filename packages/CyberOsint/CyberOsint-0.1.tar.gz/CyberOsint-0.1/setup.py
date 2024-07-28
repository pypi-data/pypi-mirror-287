from setuptools import setup, find_packages

setup(
    name='CyberOsint',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'colorama',
        'faker'
    ],
    entry_points={
        'console_scripts': [
            'cyberosint=CyberOsint.main:main',
        ],
    },
    author='Luka',
    author_email='thecyberstalker@gmail.com',
    description='A tool for OSINT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/TheCyberStalker/CyberOsint',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
