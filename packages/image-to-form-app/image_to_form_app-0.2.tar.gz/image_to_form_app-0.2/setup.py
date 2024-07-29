from setuptools import setup, find_packages

setup(
    name="image_to_form_app",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "PyQt5",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "image_to_form_app=image_to_form_app.main:main",
        ],
    },
    author="Preetam Verma",
    author_email="preetam.verma@hcl.software",
    description="A CLI tool to upload images to a REST API and handle the response.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://yourprojecturl.com",
)
