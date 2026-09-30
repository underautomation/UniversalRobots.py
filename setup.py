import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version_file = os.path.realpath(os.path.join(os.path.dirname(__file__), "underautomation", "universal_robots", "lib", "version.txt"))

with open(version_file, "r", encoding="utf-8") as fh:
    version = fh.read().strip()

setuptools.setup(
    name="UnderAutomation.UniversalRobots",
    version=version,
    author="UnderAutomation",
    author_email="support@underautomation.com",
    description="Communicate with Universal Robots cobots: RTDE, Primary Interface, Dashboard Server, REST API, XML-RPC, Interpreter Mode, SFTP and kinematics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://underautomation.com/universal-robots",
    project_urls={
        "Documentation": "https://underautomation.com/universal-robots/documentation/get-started-python",
        "Source": "https://github.com/underautomation/UniversalRobots.py",
        "Changelog": "https://github.com/underautomation/UniversalRobots.py/releases",
        "Issues": "https://github.com/underautomation/UniversalRobots.py/issues",
    },
    license="Commercial",
    keywords=["robot", "industrial robot", "cobot", "universal robots", "ur", "rtde", "dashboard server", "primary interface", "urscript", "polyscope"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
    ],
    packages=setuptools.find_packages(include=["underautomation", "underautomation.*"]),
    python_requires="<3.14,>=3.7",
    install_requires=[
        "pythonnet==3.0.5",
    ],
    include_package_data=True,
    package_data={
        "underautomation": [
            "universal_robots/lib/*.dll",
            "universal_robots/lib/*.txt",
        ],
    },
)
