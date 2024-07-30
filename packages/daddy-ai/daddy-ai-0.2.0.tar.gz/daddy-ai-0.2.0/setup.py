from setuptools import setup, find_packages

setup(
    name="daddy-ai",
    version="0.2.0",  # Updated version number
    author="Rajesh Roy",
    author_email="rajeshroy402@gmail.com",
    description="A package for deploying and managing Python commands.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rajeshroy402/daddy-ai",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

