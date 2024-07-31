from setuptools import setup, find_packages

setup(
    name="ons-mkdocs-theme",
    version="0.2.0",
    description="ONS MkDocs theme",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="BSD-2-Clause",
    author="Keilan Evans",
    author_email="keilan.evans@ons.gov.uk",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: MkDocs",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Documentation",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "mkdocs >= 1.6",
        "mkdocs-material >= 9.5",
    ],
    entry_points={
        "mkdocs.themes": [
            "ons-mkdocs-theme = ons_mkdocs_theme",
        ],
    },
    url="https://github.com/ONSdigital/ons-mkdocs-theme",
)
