from setuptools import setup

setup(
    name='nurl',
    install_requires=[
        'requests',
        'flask',
    ],
    test_requires=[
        'mock',
        'pytest',
        'pytest-mock'
    ]
)

