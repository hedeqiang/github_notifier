from setuptools import setup, find_packages

setup(
    name="github-notifier",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "github-notifier=github_notifier.cli:run_cli",
        ],
    },
    author="hedeqiang",
    author_email="laravel_code@163.com",
    description="A CLI tool to manage GitHub notifications",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hedeqiang/github-notifier",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
