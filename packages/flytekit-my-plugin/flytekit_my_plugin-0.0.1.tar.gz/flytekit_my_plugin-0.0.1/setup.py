from setuptools import setup, find_packages

setup(
    name='flytekit_my_plugin',
    version='0.0.1',
    packages=find_packages(include=['flytekitplugins', 'flytekitplugins.my_plugin']),
    install_requires=[
        'flytekit',
    ],
)
