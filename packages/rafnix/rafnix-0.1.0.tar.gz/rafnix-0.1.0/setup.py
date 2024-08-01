from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="rafnix",
    version="0.1.0",
    author="Emeka Iwuagwu",
    author_email="e.iwuagwu@hotmail.com",
    description="A library for disease prediction using machine learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EmekaIwuagwu/rafnix",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas",
        "scikit-learn",
    ],
)