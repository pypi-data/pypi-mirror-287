from setuptools import setup, find_packages

setup(
    name="colorbykawa",
    version="2.4.3",
    description="A library for colored terminal text with 50 different colors and hex code",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="kawa",
    author_email="falekula1@gmail.com",
    url="https://github.com/falekula/colorbykawa",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

