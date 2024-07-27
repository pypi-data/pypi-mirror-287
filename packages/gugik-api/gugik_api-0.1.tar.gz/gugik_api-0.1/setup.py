from setuptools import setup, find_packages

setup(
    name="gugik_api",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests>=2.0",
        "pytest>=6.0",
        "pyproj", 
    ],
    extras_require={
        "dev": [
            "flake8>=3.8",
        ]
    },
    author="Lech Hubicki",
    author_email="lech.hubicki@gmail.com",
    description="A Python client for the GUGiK API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lechplace/gugik_api",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
