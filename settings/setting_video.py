import os
import fnmatch
import sys

from utils.check_file_exist import file_exist


class VideoConverter:
    '''Script para converter vídeos utilizando o FFmpeg'''

    # Cria os diretórios de origem e destino caso eles não existam
    def create_directorys(self, midia, action):
        if midia:
            typo = 'video'
        else:
            typo = 'áudio'
        if action:
            act = 'conversão'
        else:
            act = 'extração'
        if not os.path.isdir(self.souce_path):
            try:
                os.mkdir(self.souce_path)

            except FileExistsError:
                ...
        print(
            f'\n# Adicione seu(s) {typo}(s) na pasta "{self.souce_path[2:]}" :) #\n'
        )
        if not os.path.isdir(self.destination_path):
            try:
                os.mkdir(self.destination_path)

            except FileExistsError:
                ...
        print(
            f'# O(s) {typo}(s) {act}(s) estão na pasta "{self.destination_path[2:]}" :) #\n'
        )
        return True

    def __init__(self, souce_path, destination_path):
        # Define parâmetros do FFmpeg
        self.codec_video = ''  # codec de video
        self.codec_audio = ''  # codec de audio
        self.crf = '-crf 20'  # crf
        self.preset = '-preset ultrafast'  # preset
        self.bitrate_audio = ''  # bitate ádio
        self.command_ffmpeg = ''  # o comando ffmpeg
        self.time = ''  # tempo de vídeo/audio de saída
        self.input_format = ''  # formato mídia de entrada
        self.output_format = ''  # formato de mídia de saida
        self.souce_path = souce_path  # pasta de origem
        self.destination_path = destination_path  # pasta de destino

    # Seta a plataforma
    def set_platform(self, midia, action):
        # Linux
        if sys.platform == 'linux':
            self.create_directorys(midia, action)
            self.command_ffmpeg = 'ffmpeg'
        return sys.platform

    # Recebe o formato de entrada do video/audio
    def format_input(self, format_video: str) -> str:
        self.input_format = format_video
        self.codec_video = '-c:v libx264'
        self.codec_audio = '-c:a aac'
        return self.input_format

    # Recebe o formato de saída do video
    def format_output(self, format_video: str) -> str:
        self.output_format = format_video
        return self.output_format

    # Recebe o tempo que o vídeo extraído terá | Padrão (todo vídeo)
    def time_midia(self, duration_time: str) -> str:
        if not duration_time:
            return False
        self.time = f'-ss 00:00:00 -t ' + duration_time
        return self.time

    # Função que converte os videos
    def execute(self):
        # Percorre da raiz até o arquivo passando por subpastas
        for root, folders, files in os.walk(self.souce_path):
            if not files:
                print(
                    f'\nINFO: O diretório "{self.souce_path[2:]}" está vazio :(')
            for file in files:
                # Verifica se o arquivo com a extensão passada existe
                if not fnmatch.fnmatch(file, '*.' + self.input_format):
                    print(
                        f'\nINFO: Não foi encontrado nenhum arquivo .{self.input_format}'
                        f' na pasta "{self.souce_path}"')
                    continue

                # Junta o diretório raiz com o arquivo
                full_path = os.path.join(root, file)
                # Separa o nome do arquivo da extensão
                name_file, extension_file = os.path.splitext(full_path)

                # Concatena o nome do arquivo com .srt
                caption_path = name_file + '.srt'

                # Verifica se o vídeo possui legenda
                if os.path.isfile(caption_path):
                    caption_input = f'-i "{caption_path}"'
                    caption_map = '-c:s -map v:0 -map a -map 1:0'
                else:
                    caption_input = ''
                    caption_map = ''

                # Separa o nome do arquivo da extensão
                name_file, extension_file = os.path.splitext(file)

                # Cria o path de saída
                exit_file = (
                    f'{self.destination_path}/{name_file}.{self.output_format}'
                )
                command = (
                    f'{self.command_ffmpeg} -i "{full_path}" {caption_input} '
                    f'{self.codec_video} {self.crf} {self.preset} {self.codec_audio} '
                    f'{self.bitrate_audio} {self.time} {caption_map} "{exit_file}"'
                )

                # Verifica se o arquivo já existe
                if file_exist(exit_file):
                    os.system(command)
                else:
                    continue
            return True
