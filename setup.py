import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bser-python-client",
    version="0.0.2",
    author="myungseokang",
    author_email="iam@myungseokang.dev",
    description="A Python API client for bser-open-api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/myungseokang/bser-python-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
