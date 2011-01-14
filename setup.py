from distutils.core import setup

setup(
    name = "adminlettuce",
    packages = ["adminlettuce"],
    package_data={'adminlettuce': ['templates/*.html']},
    version = "0.0.5",
    description = "Displays lettuce features as documentation in Django admin.",
    author = "Red Interactive",
    author_email = "geeks@ff0000.com",
    url = "http://ff0000.com/",
    download_url = "https://github.com/ff0000/adminlettuce",
    keywords = ["django", "admin", "bdd", "tdd", "documentation"],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Natural Language :: English",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities"
        ],
    long_description = """\
Admin documentation for lettuce-generated integration tests.
-------------------------------------

This module integrates lettuce (http://www.lettuce.it) support for Django by
printing out the content of the features and scenarios to the Django admin
interface.

The goal is to make the final user aware of the specifications and requirements
of the application without having to browse the source code.
"""
)