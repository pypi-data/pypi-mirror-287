from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="timeseriesfcst",
    packages=["timeseriesfcst"],
    version="0.1.3",
    author="Anna-Valentina Hirsch",
    author_email="a-valentina.hirsch@hotmail.com",
    description="A python toolkit for time series preprocessing, feature engineering, and forecasting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AnnaValentinaHirsch/time-series-toolkit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "statsmodels",
        "scikit-learn",
        "tensorflow"
    ],
)