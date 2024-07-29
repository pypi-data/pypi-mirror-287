from setuptools import setup, find_packages

setup(
    name="pinterest-scraper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "beautifulsoup4",
    ],
    entry_points={
        "console_scripts": [
        ],
    },
    author="Himasha Herath",
    author_email="himasha626@gmail.com",
    description="A Python package to scrape comments from Pinterest and extract usernames",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HimashaHerath/pinterest-scraper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
