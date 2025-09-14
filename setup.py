from setuptools import setup

setup(name='dev_aberto_Aava_Niskakangas',
    version='0.1', 
    install_requires=[
        "requests>=2.0.0",
    ],
    scripts=['scripts/hello.py'],
    packages=['dev_aberto']
)


