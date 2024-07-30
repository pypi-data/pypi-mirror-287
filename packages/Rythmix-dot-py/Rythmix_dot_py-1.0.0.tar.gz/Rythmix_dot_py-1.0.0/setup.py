from setuptools import setup, find_packages

setup(
    name="Rythmix_dot_py",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "youtube-search-python==1.6.6",
        "yt-dlp==2024.7.25",
        "python-vlc==3.0.20123"
    ],
    entry_points={
        "console_scripts": [
            "rythmix = Rythmix_dot_py:main"
        ]
    }
)
