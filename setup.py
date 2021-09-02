from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# TODO: move to setup.cfg
setup(
    name="ludovico",
    version="0.0.3",
    description="An opinionated DataFrame-to-TeX table generator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aitorres/ludovico",
    author="Andrés Ignacio Torres",
    author_email="dev@aitorres.com",
    license="MIT",
    packages=["ludovico"],
    install_requires=[
        "pandas",
    ],
    extras_require={
        "dev": [
            "pytest",
        ]
    },
    project_urls={
        "Bug Tracker": "https://github.com/aitorres/ludovico/issues",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Text Processing :: Markup :: LaTeX",
    ],
    python_requires=">=3.7",
)
