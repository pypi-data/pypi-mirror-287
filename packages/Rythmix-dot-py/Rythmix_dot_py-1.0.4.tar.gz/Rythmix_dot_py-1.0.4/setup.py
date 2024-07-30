from setuptools import setup, find_packages

setup(
    name="Rythmix_dot_py",
    version="1.0.4",
    packages=find_packages(),
    description="A simple CLI tool for playing music. (VLC is required!)",
    long_description=open("README.md").read(),
    install_requires=[
        "youtube-search-python==1.6.6",
        "yt-dlp==2024.7.25",
        "python-vlc==3.0.20123",
        "distro==1.9.0"
    ],
    entry_points={
        "console_scripts": [
            "rythmix = Rythmix_dot_py:main",
            "rythmix_setup_vlc = Rythmix_dot_py:install_vlc"
        ]
    }
)
