from setuptools import setup

VERSION = "0.1.0"

setup(
    name="aiostep",
    version=VERSION,
    description="A Python library to handle steps in aiogram framework.",
    author="Nasrollah Yusefi",
    url="https://github.com/NasrollahYusefi/aiostep/",
    packages=["aiostep"],
    install_requires=[
        "cachebox"
    ],
    license="MIT",
    license_files=["LICENSE"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
