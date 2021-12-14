from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wordflow-jmd",
    version="0.1.0",
    author="Joseph Diza",
    author_email="josephm.diza@gmail.com",
    description="Provides offline video subtitles/caption translations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jmdaemon/wordflow",
    project_urls={
        "Bug Tracker": "https://github.com/jmdaemon/wordflow/issues",
    },
    license='MIT',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    py_modules=[],
    install_requires=[
        'argparse',
    ],
    test_suite='tests',
)
