from setuptools import setup

setup(
    name='HyDi',
    version='0.0.1',
    install_requires=[
        'requests',
        'pandas',
        'json',
        'random',
        'importlib-metadata; python_version<"3.10"',
    ],
)