import os
from fnmatch import fnmatch

from .setting_video import VideoConverter
from utils.check_file_exist import file_exist


class ExtractedAudio(VideoConverter):
    """Script para extração de audio de video utilizando o FFMpeg"""

    def format_output(self, format_audio: str) -> str:
        if format_audio == 'mp3':
            self.output_format = format_audio
            self.codec_audio = '-acodec libmp3lame'
            self.bitrate_audio = '-b:a 320k'
            return True
        elif format_audio == 'ogg':
            self.output_format = format_audio
            self.codec_audio = '-acodec libvorbis'
            self.bitrate_audio = '-b:a 320k'
            return True
        elif format_audio == 'aac':
            self.output_format = format_audio
            self.codec_audio = '-acodec aac'
            self.bitrate_audio = '-b:a 320k -f adts'
            return True
        elif format_audio == 'flac':
            self.output_format = format_audio
            self.codec_audio = '-c:a flac'
            self.bitrate_audio = '-b:a 320k'
            return True

    # Função que extrai/converte os videos
    def execute(self):
        for root, folders, files in os.walk(self.souce_path):
            if not files:
                print(
                    f'\nINFO: O diretório "{self.souce_path[2:]}" está vazio :(')
            for file in files:
                # Verifica se o arquivo com a extensão passada existe
                if not fnmatch(file, '*.' + self.input_format):
                    print(
                        f'\nINFO: Não foi encontrado nenhum arquivo .{self.input_format}'
                        f' em "{self.souce_path}"')
                    continue

                # Junta o diretório raiz com o arquivo
                full_path = os.path.join(root, file)
                # Separa o nome do arquivo da extensão
                name_file, extension_file = os.path.splitext(full_path)

                # Separa o nome do arquivo da extensão
                name_file, extension_file = os.path.splitext(file)

                # Cria o path de saída
                exit_file = (
                    f'{self.destination_path}/{name_file}.{self.output_format}'
                )
                command = (
                    f'{self.command_ffmpeg} -i "{full_path}" -vn {self.bitrate_audio} '
                    f'{self.codec_audio} {self.time} "{exit_file}" -y'
                )
                if file_exist(exit_file):
                    os.system(command)
                else:
                    continue
        return True


class AudioConverter(ExtractedAudio):
    ...
