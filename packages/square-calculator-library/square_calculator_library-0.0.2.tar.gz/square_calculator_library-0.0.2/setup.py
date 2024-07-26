import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    "flake8==6.0.0",
    "flake8-isort==6.0.0",
    "isort==5.13.2",
    "mccabe==0.7.0",
    "pycodestyle==2.10.0",
    "pyflakes==3.0.1",
]

setuptools.setup(
    name="square_calculator_library",
    version="0.0.2",
    author="Aleksandr Buchelnikov",
    author_email="al.buchelnikov@gmail.com",
    description="The library allows you to calculate the area of geometric shapes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AVanslov/square_calculator_library",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
