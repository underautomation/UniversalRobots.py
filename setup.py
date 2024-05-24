import setuptools
import os

with open('README.md', "r", encoding="utf-8") as fh:
    long_description = fh.read()

version_file = os.path.realpath(os.path.join(os.path.dirname(__file__), "underautomation",  'universal_robots', 'lib', 'version.txt'))

with open(version_file, "r", encoding="utf-8") as fh:
    version = fh.read()

setuptools.setup(
    name="UnderAutomation.UniversalRobots",
    version=version,
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
        "universal_robots/lib/*.dll",
        "universal_robots/lib/*.txt"
    ]}
)


