"""
.. module:: setup
   :platform: Multiplatform
   :synopsis: installer module
.. moduleauthor:: Andrea Cervesato <andrea.cervesato@mailbox.org>
"""

from setuptools import setup

import libkirk

setup(
    name="kirk",
    version=libkirk.__version__,
    description="All-in-one Linux Testing Framework",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Linux Test Project",
    author_email="ltp@lists.linux.it",
    license="GPLv2",
    url="https://github.com/linux-test-project/kirk",
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Testing",
    ],
    extras_require={
        "ssh": ["asyncssh <= 2.13.2"],
        "ltx": ["msgpack <= 1.0.5"],
    },
    packages=["libkirk"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "kirk=libkirk.main:run",
        ],
    },
)
