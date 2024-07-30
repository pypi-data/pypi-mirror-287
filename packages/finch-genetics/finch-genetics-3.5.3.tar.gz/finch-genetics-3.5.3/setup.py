import setuptools

with open("Finch/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="finch-genetics",
    version="3.5.3",
    author="Daniel Losey",
    author_email="danieljlosey@gmail.com",
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

token = "pypi-AgEIcHlwaS5vcmcCJGI2NTRhY2JhLWRhNTItNDA4NC1hMGQxLTRlMWU1MDc1ZjE3NgACFlsxLFsiZmluY2gtZ2VuZXRpY3MiXV0AAixbMixbIjE3ZjdiNzRjLTg0MjItNDAxNi04MDE2LTg0ZjkxNTU4ZTljZiJdXQAABiCKr3kPpHgrDG4OjeeILaC3YvPMaFgY0gIt965VT4d77g"
# python3.11 setup.py sdist bdist_wheel
# twine upload dist/*