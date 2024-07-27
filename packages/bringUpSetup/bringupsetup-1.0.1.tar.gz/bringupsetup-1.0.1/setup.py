from setuptools import setup, find_packages

setup(
    name="AutomationSetup",
    version="1.0.0",
    author="ShreeKumar",
    author_email="shree_kumar@apple.com",
    description="Checks and Installs the Required Software for Bring up",
    url="https://github.pie.apple.com/shree-kumar/BringUpAutomation/tree/SetUp",
    package_dir={'':"src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Intended Audience :: Platform Software Developers"
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOSX",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "bringUpSetup = bringUpSetup.__main__:main",
        ],
    },
)