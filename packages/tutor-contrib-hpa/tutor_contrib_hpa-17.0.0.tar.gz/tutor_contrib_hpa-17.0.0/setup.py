"""
Setuptools file for tutor-contrib-hpa
"""
import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    """
    Load readme file.
    :return:
    """
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    """
    Load about file.
    :return:
    """
    about = {}
    with io.open(
        os.path.join(HERE, "tutorhpa", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="tutor-contrib-hpa",
    version=ABOUT["__version__"],
    url="https://github.com/myusername/tutor-contrib-hpa",
    project_urls={
        "Code": "https://github.com/myusername/tutor-contrib-hpa",
        "Issue tracker": "https://github.com/myusername/tutor-contrib-hpa/issues",
    },
    license="AGPLv3",
    author="Aulasneo",
    author_email="andres@aulasneo.com",
    description="Tutor plugin to enable HPA for Kubernetes installations of Open edX",
    long_description=load_readme(),
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["tutor >= 17.0.0, < 18.0.0"],
    entry_points={
        "tutor.plugin.v1": [
            "hpa = tutorhpa.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
