from setuptools import setup, find_packages

setup(
    name='telegrafbot',
    version='0.1.0',
    author='iliya kaviyani',
    author_email='telegrafbot57@gmail.com',
    description='A simple Telegram bot library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # آدرس مخزن GitHub خود را وارد کنید
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
