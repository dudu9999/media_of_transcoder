#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from settings.setting_audio import AudioConverter, ExtractedAudio
from settings.setting_video import VideoConverter

from utils.install_ffmpeg import ffmpeg
from utils.validations import Validations

from apps.media_app import apps, app_cut


while True:
    print('''
*****************************************
*     -  ESCOLHA UMA DAS OPÇÕES  -      *
*****************************************
* 1 - Para instalar o FFMpeg (Linux)    *
* 2 - Para converter vídeos(s)          *
* 3 - Para converter áudio(s)           *
* 4 - Para extrair áudio(s) de vídeo(s) *
* 5 - Para o Help                       *
* 0 - Para sair                         *
*****************************************
    ''')

    opc = input('Digite a opção desejada: ')

    # Instala o FFmpeg
    if opc == '1':
        ffmpeg()
        continue

    # Converter vídeos
    elif opc == '2':
        settings = VideoConverter(
            './videos_para_converter', './videos_convertidos')
        validate = Validations()
        settings.set_platform(True, True)

        if apps(settings, validate, 'video', 'origem', 'vídeo'):
            pass
        if apps(settings, validate, 'video', 'destino', 'vídeo', False):
            pass
        if app_cut(settings, validate):
            exit()

    # Converter áudios
    elif opc == '3':
        settings = AudioConverter(
            './audios_para_converter', './audios_convertidos')
        validate = Validations()
        settings.set_platform(False, True)

        if apps(settings, validate, 'audio', 'origem', 'áudio'):
            pass
        if apps(settings, validate, 'audio', 'destino', 'áudio', False):
            pass
        if app_cut(settings, validate):
            exit()

    # Extrai áudios
    elif opc == '4':
        settings = ExtractedAudio(
            './videos_para_extracao', './audios_extraidos')
        validate = Validations()
        settings.set_platform(True, False)

        if apps(settings, validate, 'video', 'origem', 'vídeo'):
            pass
        if apps(settings, validate, 'audio', 'destino', 'áudio', False):
            pass
        if app_cut(settings, validate):
            exit()

    # Help
    elif opc == '5':
        os.system('clear && cat ./help.txt')
        op = input('\nPressione qualquer tecla para abrir as opções... ')
        continue

    elif opc == '0':
        break

    else:
        print('Opção incorreta.')
        continue
