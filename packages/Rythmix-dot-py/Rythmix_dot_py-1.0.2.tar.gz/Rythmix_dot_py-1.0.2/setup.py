from setuptools import setup, find_packages

setup(
    name="Rythmix_dot_py",
    version="1.0.2",
    packages=find_packages(),
    install_requires=[
        "youtube-search-python",
        "yt-dlp",
        "python-vlc"
    ],
    entry_points={
        "console_scripts": [
            "rythmix = Rythmix_dot_py:main"
        ]
    }
)
