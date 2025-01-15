from setuptools import setup, find_packages

setup(
    name="script-game-engine",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add dependencies here as needed
        "pytest",  # for testing
    ],
    author="Deepak Silaych",
    description="A script-based army building game engine",
    license="MIT",
) 