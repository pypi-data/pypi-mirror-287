import re
from pathlib import Path

from setuptools import setup  # type: ignore

path = Path(__file__).parent
txt = (path / "aiofreqlimit" / "__init__.py").read_text("utf-8")
version = re.findall(r"^__version__ = \"([^\"]+)\"\r?$", txt, re.M)[0]
readme = (path / "README.rst").read_text("utf-8")

setup(
    name="aiofreqlimit",
    version=version,
    description="Frequency limit for asyncio",
    long_description=readme,
    long_description_content_type="text/x-rst",
    url="https://github.com/gleb-chipiga/aiofreqlimit",
    license="MIT",
    author="Gleb Chipiga",
    # author_email='',
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Internet",
        "Framework :: AsyncIO",
    ],
    packages=["aiofreqlimit"],
    package_data={"aiofreqlimit": ["py.typed"]},
    python_requires=">=3.11,<3.13",
    tests_require=[
        "pytest",
        "pytest-asyncio",
        "pytest-mock",
        "pytest-cov",
        "hypothesis",
    ],
)
