import os
import sys
import platform


def ffmpeg():
    """Executa no terminal a instalação do ffmpeg seta as permissões"""
    print(f'\n{"#" * 40}')
    ffmpeg_install = input('Deseja instalar o FFmpeg [y/n]? ')
    print(f'{"#" * 40}\n')
    # Verifica a plataforma e distro (linux)
    distro = platform.platform()
    if ffmpeg_install.lower() == 'y':
        if sys.platform == 'linux':
            if 'fedora' in distro:
                os.system('sudo dnf install https://download1.rpmfusion.org/free/fedora/'
                          'rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm -y && '
                          'sudo dnf install ffmpeg -y && chmod +x main.py'
                          )
                return True
            if 'arch' in distro:
                ...
            if 'ubuntu' in distro:
                os.system('sudo apt-get install ffmpeg -y && chmod +x main.py')


if __name__ == '__main__':
    ffmpeg()
