from setuptools import setup, find_packages
import setuptools_scm

setup(
    name="progress_basic",
    # use_scm_version=True,
    setup_requires=["setuptools>=42", "setuptools_scm"],
    version='0.1',
    packages=find_packages(include=['progress_basic', 'progress_basic.*']),
    include_package_data=True,
    install_requires=['library_externals'],
    author="leonardogonzalolaura",
    author_email="glleonardodaniel@gmail.com",
    description="A simple example of a Python library",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/leonardogonzalolaura/progress_basic",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)