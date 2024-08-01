from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="matrixkit",
    version="0.1.1",
    author=["Toni Johann Schulze Dieckhoff", "Anna-Valentina Hirsch"],
    author_email="a-valentina.hirsch@hotmail.com",
    description="Synthetic Matrix Generation for Machine Learning and Scientific Computing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AnnaValentinaHirsch/matrixkit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy~=1.26.4",
        "scipy~=1.13.1",
        "pillow~=10.3.0",
        "matplotlib~=3.5.2",
        "seaborn~=0.13.2"
    ],
)
