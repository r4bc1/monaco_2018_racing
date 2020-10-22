import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="report-of-racing-using-flask-by-r4bc1",
    version="0.1",
    author="Roman Kaharlytskyi",
    author_email="r4bckagarl@gmail.com",
    description="Reads data from 2 files, order racers by time and print pretty report on the web pages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.foxminded.com.ua/r4bc1/task-7-web-report-of-racing",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
