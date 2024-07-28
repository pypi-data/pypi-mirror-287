"""
This project is a simple unit converter.
"""

from setuptools import setup
from setuptools import find_packages

classifiers = (
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Science/Research',   
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development',
)

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

setup(
    name="unit_converter_python",
    version="0.0.2",
    author="Daniel Torres de Andrade",
    author_email="danieltorresandrade@gmail.com",
    classifiers=classifiers,
    description="This project is a simple unit converter.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Danieltandrade/Unit-Converter",
    packages=find_packages(),
    license="MIT License",
    keywords="unit converter, unit-converter, unit_converter",
    python_requires='>=3.8',
)
