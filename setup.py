import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="insurapy",
    version="0.1",
    author="Jake McAferty",
    author_email="jake.mcaferty@gmail.com",
    description="A python library for actuarial and insurance calculations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Intended Audience :: Financial and Insurance Industry"
    ],
)