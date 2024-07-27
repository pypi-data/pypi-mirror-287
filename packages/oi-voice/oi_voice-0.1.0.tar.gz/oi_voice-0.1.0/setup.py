from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="oi-voice",
    version="0.1.0",  # Ensure version is in the correct format
    packages=find_packages(),
    install_requires=[
        "faster-whisper",
        "open-interpreter",
        "click",
        "requests",
        "pyaudio",  # Add pyaudio as a dependency
        "pydub"  # Add pydub as a dependency
    ],
    entry_points={
        "console_scripts": [
            "oi-voice=oi_voice.cli:main",
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
