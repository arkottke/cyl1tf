import platform
from setuptools import find_packages, setup, Extension

import numpy as np

# Build project with:
# python setup.py build_ext --inplace

with open("README.rst", encoding="utf-8") as fp:
    readme = fp.read()

with open("HISTORY.rst", encoding="utf-8") as fp:
    history = fp.read()

LIBRARIES = ["blas", "lapack"]
if platform.system() != "Windows":
    LIBRARIES.append("m")

ext_modules = [
    Extension(
        "cyl1tf.interface",
        ["cyl1tf/interface.pyx", "source/l1tf.c"],
        libraries=LIBRARIES,
        include_dirs=["cyl1tf", "source", np.get_include()],
        extra_compile_args=["-Ofast"],
    ),
]

setup(
    name="cyl1tf",
    version="0.1.3",
    description="Cython implementation of L1 trend fitting.",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    author="Albert Kottke",
    author_email="albert.kottke@gmail.com",
    url="https://github.com/arkottke/cyl1tf",
    packages=find_packages(exclude=["tests"]),
    setup_requires=[
        # Setuptools 18.0 properly handles Cython extensions.
        "setuptools>=18.0",
        "cython",
        "numpy",
    ],
    tests_require=[
        "pytest",
        "pytest-runner",
    ],
    ext_modules=ext_modules,
    zip_safe=False,
)
