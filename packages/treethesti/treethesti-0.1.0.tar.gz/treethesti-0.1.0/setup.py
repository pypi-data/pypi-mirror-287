from setuptools import setup, find_packages

setup(
    name="treethesti",
    version="0.1.0",
    description="A package for using pkl files to calculate frequency percentages",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="YN",
    author_email="morgen@emory.edu.com",
    url="https://github.com/yourusername/treethestima",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy",
    ],
    include_package_data=True,
)
