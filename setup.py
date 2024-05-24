import setuptools
from setuptools.dist import Distribution
import os

with open('README.md', "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="UnderAutomation.UniversalRobots",
    version="7.4.1.0.1",
    author="UnderAutomation",
    author_email="support@underautomation.com",
    description="Quickly create applications that communicate with your Universal Robots cobot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://underautomation.com/universal-robots",
    project_urls={
        'Documentation': 'https://underautomation.com/universal-robots/documentation/get-started-python',
        'Source': 'https://github.com/underautomation/UniversalRobots',
    },
    classifiers=[],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.7",
    install_requires=[
        'pythonnet==3.0.3'
    ],
    include_package_data=True,
    package_data={"": [
        "universal_robots/lib/*.dll"
    ]}
)


