import subprocess
import platform
import ctypes
import os


def is_root():
    if platform.system() == 'Windows':
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    return os.geteuid() == 0


def is_apple_silicon():
    return platform.machine() in ['arm64', 'aarch64']


def install_vlc():
    if not is_root():
        print("This script must be run as root/administrator.")
        return
    system = platform.system()

    if system == 'Windows':
        vlc_installer_url = 'https://get.videolan.org/vlc/3.0.21/win64/vlc-3.0.21-win64.exe'
        installer_path = os.path.join(os.getenv('TEMP'), 'vlc_installer.exe')
        subprocess.run(['wget', '-O', installer_path, vlc_installer_url], check=True)
        subprocess.run([installer_path, '/S'])

    elif system == 'Darwin':
        if is_apple_silicon():
            vlc_installer_url = 'https://get.videolan.org/vlc/3.0.21/macosx/vlc-3.0.21-arm64.dmg'
        else:
            vlc_installer_url = 'https://get.videolan.org/vlc/3.0.21/macosx/vlc-3.0.21-intel64.dmg'
        subprocess.run(['curl', '-L', '-o', 'vlc.dmg', vlc_installer_url])
        subprocess.run(['hdiutil', 'attach', 'vlc.dmg'])
        subprocess.run(['sudo', 'cp', '-R', '/Volumes/VLC media player/VLC.app', '/Applications'])
        subprocess.run(['hdiutil', 'detach', '/Volumes/VLC media player'])
        subprocess.run(['sudo', 'rm', 'vlc.dmg'])

    elif system == 'Linux':
        try:
            import distro
            distro_name = distro.id().lower()
        except ImportError:
            print("Please install the 'distro' package for Linux distribution detection.")
            return

        if 'ubuntu' in distro_name or 'debian' in distro_name:
            subprocess.run(['sudo', 'apt-get', 'update', '-y'])
            subprocess.run(['sudo', 'apt-get', 'install', '-y', 'vlc'])

        elif 'centos' in distro_name or 'rhel' in distro_name:
            subprocess.run(['sudo', 'yum', 'install', '-y', 'epel-release'])
            subprocess.run(['sudo', 'yum', 'install', '-y', 'vlc'])

        elif 'fedora' in distro_name:
            subprocess.run(['sudo', 'dnf', 'install', '-y', 'vlc'])

        else:
            print(f"Error: Unsupported Linux distribution: {distro_name}")
            return

    else:
        print(f"Error: Unsupported operating system: {system}")
        return


if __name__ == '__main__':
    install_vlc()
