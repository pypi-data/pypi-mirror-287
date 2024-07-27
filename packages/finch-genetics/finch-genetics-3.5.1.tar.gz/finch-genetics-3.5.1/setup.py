import setuptools

with open("Finch/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="finch-genetics",
    version="3.5.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A flexible framework for evolutionary algorithms in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dadukhankevin/Finch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",

        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.18.0",
        "matplotlib>=3.1.0",
        "pillow>=7.0.0",
    ],
    extras_require={
        "gpu": ["cupy>=7.0.0"],
    },
)