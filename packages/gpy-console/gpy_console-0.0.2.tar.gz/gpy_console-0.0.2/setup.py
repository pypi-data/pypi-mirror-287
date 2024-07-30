from setuptools import setup
import re

version = ""
with open("gpyConsole/__init__.py") as initpy:
    regex = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', initpy.read(), re.MULTILINE
    )
    assert regex != None
    version = regex.group(1)

if not version:
    raise RuntimeError("Version is not set.")

setup(
    name="gpy-console",
    version="0.0.2",
    description="Execute your bot's commands from the console!",
    long_description=open("README.md", encoding="utf8").read(),
    url="https://github.com/EcoNuker/guilded.py-console",
    long_description_content_type="text/markdown",
    author="YumYummity",
    license="MIT",
    classifiers=["Programming Language :: Python :: 3.7"],
    packages=["gpyConsole"],
    install_requires=["google-re2", "typing", "aioconsole"],
    include_package_data=True,
    extras_require={"gil.py": ["gil.py"], "guilded.py": ["guilded.py"]},
)
