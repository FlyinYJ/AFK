import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="AFK",
    version="1.0.1",
    description="A mouse jigger written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yifan Jin",
    packages=find_packages(),
    install_requires=["pyautogui", "alive_progress"],
    entry_points={  # Optional
        "console_scripts": [
            "AFK=AFK:AFK",
        ],
    },
)
