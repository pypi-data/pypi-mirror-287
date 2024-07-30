from pathlib import Path

from setuptools import setup, find_packages

from comberload import __version__

project_dir = Path(__file__).parent

try:
    long_description = (project_dir / "README.md").read_text()
except FileNotFoundError:
    try:
        long_description = Path("README.md").read_text()
    except FileNotFoundError:
        try:
            long_description = Path("/src/README.md").read_text()
        except FileNotFoundError:
            long_description = (project_dir.parent / "README.md").read_text()

deps = ()


extra_test = (
    "pytest",
    "pytest-cov",
)

extra_dev = (*extra_test,)

extra_ci = (
    *extra_test,
    "coveralls",
)

setup(
    name="comberload",
    version=__version__,
    py_modules=["comberload"],
    project_urls={
        "Funding": "https://ko-fi.com/kenmorel",
        "Source": "https://github.com/ken-morel/comberload/",
        "Tracker": "https://github.com/ken-morel/comberload/issues",
    },
    url="https://github.com/ken-morel/comberload",
    license="MIT",
    author="ken-morel",
    author_email="engonken8@gmail.com",
    maintainer="ken-morel",
    maintainer_email="engonken8@gmail.com",
    description=("Stop letting heavy packages block down your scripts!"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=deps,
    extras_require={
        "dev": extra_dev,
        "ci": extra_ci,
    },
    classifiers=[
        # See https://pypi.org/classifiers/
        "Intended Audience :: Developers",
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        "Development Status :: 3 - Alpha",
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        # "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
