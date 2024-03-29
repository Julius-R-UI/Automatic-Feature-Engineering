from setuptools import setup, find_packages

with open("README.rst", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="strelok",
    version="0.0.1",
    author="Julius Riel",
    author_email="julius.riel@icloud.com",
    description="A short description of your project",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/yourusername/strelok",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="strelok, feature, selection, machine learning",
    python_requires='>=3.6',
)