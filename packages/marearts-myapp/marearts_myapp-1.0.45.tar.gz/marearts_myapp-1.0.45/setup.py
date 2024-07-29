from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [Extension("marearts_myapp_compiled", ["myapp.pyx"])]

setup(
    name="marearts-myapp",
    version="1.0.45",  # Increment the version
    author="MareArts",
    author_email="hello@marearts.com",
    description="A short description of your application",
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MareArts/pypi_test",
    ext_modules=cythonize(extensions, compiler_directives={'language_level': "3"}),
    setup_requires=[
        "cython>=0.29.21",
    ],
    install_requires=[
        "cython>=0.29.21",
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
)