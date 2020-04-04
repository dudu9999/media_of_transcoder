import unittest

from utils.validations import Validations
from utils.check_file_exist import file_exist


class CheckFileTest(unittest.TestCase):

    def setUp(self):
        self.file = 'teste_arquivo_origem.txt'

    # Checa se o arquivo existe, não existindo retorna true
    def test_file_exist_video(self):
        self.assertEqual(file_exist(self.file), True)


class ValidationsTests(unittest.TestCase):

    def setUp(self):
        self.validation = Validations()
        self.videos = ['mkv', 'mp4', 'wmv', 'avi']
        self.audios = ['ogg', 'mp3', 'flac', 'aac']

    # Checa se o vídeo recebido pelo input é um formato válido de vídeo
    def test_validation_videos(self):
        for video in self.videos:
            self.assertEqual(
                self.validation.validate_midia(video, 'video'), True)

    # Checa se o áudio recebido pelo input é um formato válido de áudio
    def test_validation_audios(self):
        for audio in self.audios:
            self.assertEqual(
                self.validation.validate_midia(audio, 'audio'), True)

    # Checa o formato de tempo recebido no input é válido
    def test_validation_time(self):
        self.assertEqual(self.validation.validate_time_midia('00:00:00'), True)


class InstallFFmpegTest(unittest.TestCase):
    ...
