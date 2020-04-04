import unittest
import os

from settings.setting_video import VideoConverter


class SettingsTest(unittest.TestCase):

    def setUp(self):
        self.settings = VideoConverter('.', '.')

    def test_creat_directory(self):
        self.settings.souce_path = 'test'
        self.settings.destination_path = 'test1'
        self.assertEqual(self.settings.create_directorys(
            self.settings.souce_path, self.settings.destination_path),
            os.path.exists('./test') and os.path.exists('./test1'))
        os.rmdir('./test')
        os.rmdir('./test1')

    def test_set_platform(self):
        self.assertEqual(self.settings.set_platform('', ''), 'linux')

    def test_format_input(self):
        self.assertEqual(self.settings.format_input('test'), 'test')

    def test_format_output(self):
        self.assertEqual(self.settings.format_output('test'), 'test')

    def test_time_midia(self):
        self.assertEqual(self.settings.time_midia(
            '00:00:00'), '-ss 00:00:00 -t 00:00:00')

    def test_execute(self):
        self.assertEqual(self.settings.execute(), True)
