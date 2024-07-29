from setuptools import setup, find_packages

setup(
    name='nusratjahanjahan',
    version='1.2.3',  # bump2version will update this
    packages=find_packages(),
    license='MIT',
    description='A simple example package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    install_requires=[
        # Your dependencies here
    ],
)
