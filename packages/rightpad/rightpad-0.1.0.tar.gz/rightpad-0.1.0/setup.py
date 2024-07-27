import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rightpad",
    version="0.1.0",
    author="Marie Kodes",
    author_email="mariekodes@gmail.com",
    description="A port of the infamous right-pad npm package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mariekodes/rightpad",
    py_modules=['rightpad'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)