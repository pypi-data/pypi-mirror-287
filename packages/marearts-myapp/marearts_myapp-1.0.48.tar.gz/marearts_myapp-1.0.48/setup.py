from setuptools import setup, Extension
from setuptools.command.sdist import sdist as _sdist
from Cython.Build import cythonize
import sys

class sdist(_sdist):
    def run(self):
        # Make sure the compiled Cython files are included in the source
        # distribution
        from Cython.Build import cythonize
        cythonize(["myapp.pyx"])
        _sdist.run(self)

# Define the extension
extensions = [Extension("marearts_myapp_compiled", ["myapp.pyx"])]

# On Windows, we need to specify additional compile args
if sys.platform == "win32":
    for e in extensions:
        e.extra_compile_args = ["/O2"]

setup(
    name="marearts-myapp",
    version="1.0.48",  # Increment the version
    author="MareArts",
    author_email="hello@marearts.com",
    description="A short description of your application",
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MareArts/pypi_test",
    ext_modules=cythonize(extensions),
    install_requires=[
        "cython",
    ],
    py_modules=["run_myapp"],
    entry_points={
        "console_scripts": [
            "marearts-myapp=run_myapp:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    cmdclass={
        'sdist': sdist,
    },
)