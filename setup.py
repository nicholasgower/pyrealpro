import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrealpro",
    version="0.2.1",
    author="Nicholas Gower, Andy Chase",
    author_email="nicholasgower01@gmail.com, andychase@gmail.com",
    description="Tools for building iRealPro songs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/splendidtoad/pyrealpro",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Software Development :: Libraries"
    ],
    python_requires='>=3.6',
)
