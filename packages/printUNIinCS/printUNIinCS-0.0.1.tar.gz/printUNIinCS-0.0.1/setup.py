from setuptools import setup, find_packages

setup(
    name="printUNIinCS",  # 包名称
    version="0.0.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple package to print a specific message",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/printUNIinCS",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
