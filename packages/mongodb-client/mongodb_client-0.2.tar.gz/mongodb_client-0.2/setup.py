### `mongodb_client/setup.py`

from setuptools import setup, find_packages

setup(
    name="mongodb_client",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Luis Resende Silva",
    author_email="luisresende13@gmail.com",
    description="A Python module to interact with a MongoDB database via HTTP requests.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/luisresende13/mongodb_client",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
