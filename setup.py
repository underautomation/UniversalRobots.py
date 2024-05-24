import setuptools
from setuptools.dist import Distribution
from underautomation.universal_robots.lib.version import VERSION

with open('README.md', "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="UnderAutomation.UniversalRobots",
    version=VERSION
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


