from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="miku_ai",
    version="0.1.0",
    author="Gobin",
    author_email='gobinmiku@gmail.com',
    description='A project about wechat_article_spider',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GobinFan/Miku_Spider",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'aiohttp',
        'bs4',
        'fake-useragent'
    ],
)