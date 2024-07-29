from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension(
        "treethestima.estima",
        ["treethestima/estima.pyx"],
        include_dirs=[np.get_include()],
    )
]

setup(
    name="treethestima",
    version="0.1.0",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/treethestima",
    license="MIT",
    packages=["treethestima"],
    ext_modules=cythonize(extensions),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Cython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy",
        "cython",
    ],
    include_package_data=True,
)
