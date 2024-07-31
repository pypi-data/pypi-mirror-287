from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
Long_description = (this_directory / "README.md").read_text()
setup(
    author="Tanish",
    author_email="sharmatanish0907@gmail.com",
    description="it is a tool for encrypting images",
    long_description_content_type='text/markdown',
    long_description=Long_description,
    name="image_vault",
    version="1.0.2",
    packages=find_packages(),
    install_requires=[
        "pillow",
        "cryptography",
        "click",
    ],
    keywords=["python","cryptography","image_vault","vault","encrypt","encryption","fs"],
    entry_points={
        "console_scripts": [
            "fs=Fs.main:main",
        ],
    },
)
