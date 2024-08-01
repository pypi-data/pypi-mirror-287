from setuptools import setup, find_packages

setup(
    name="wealthguru",
    version="0.1",
    author="ravikiranmnaik01",
    author_email="ravikiranmnaik@gmail.com",
    description="Stock market analysis of BSE stocks",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ravikiranmnaik01/python_packages/wealthguru",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your package dependencies here
        'numpy>=1.26.4',
        'pandas>=2.1.4',
        'requests>=2.31.0',
        'yfinance>=0.2.41'
    ],
)
