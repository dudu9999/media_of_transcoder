class Validations:
    def validate_midia(self, format_midia: str, tipo: str) -> str:
        formats_videos = ['mkv', 'mp4', 'wmv', 'avi']
        formats_audio = ['ogg', 'mp3', 'flac', 'aac']

        if not format_midia or format_midia == ' ':
            print('INFO: É preciso informar o formato do arquivo.', end='\n\n')
            return False
        if tipo == 'video':
            if format_midia not in formats_videos:
                print(
                    'INFO: Formato de vídeo(s) não existe ou não é suportado :(', end='\n\n')
                return False
            return True
        if tipo == 'audio':
            if format_midia not in formats_audio:
                print(
                    'INFO: Formato de áudio(s) não existe ou não é suportado :(', end='\n\n')
                return False
            return True

    def validate_time_midia(self, duration_time: str) -> str:
        if len(duration_time.split(':')) != 3:
            print('INFO: Formato de tempo incorreto!', end='\n\n')
            return False
        return True
