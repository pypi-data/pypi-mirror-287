# setup.py

from setuptools import setup, find_packages

setup(
    name='request-id-middleware',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'sentry-sdk>=0.14.0',
    ],
    include_package_data=True,
    description='Middleware for setting X-Request-Id header in Sentry scope',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Oluwatosin Olasupo',
    author_email='tosin@wafi.cash',
    url='https://github.com/Wafi-inc/request-id-middleware',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
