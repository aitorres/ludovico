from setuptools import setup

setup(
    name="ludovico",
    version="0.0.1",
    description="An opinionated DataFrame-to-TeX table generator.",
    url="https://github.com/aitorres/ludovico",
    author="Andrés Ignacio Torres",
    author_email="dev@aitorres.com",
    license="MIT",
    packages=["ludovico"],
    install_requires=[
        "pandas",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Text Processing :: Markup :: LaTeX",
    ],
)
