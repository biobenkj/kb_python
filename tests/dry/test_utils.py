import os
from unittest import mock, TestCase

import kb_python.dry.utils as utils
from kb_python.config import UnsupportedOSError


class TestUtils(TestCase):

    def test_run_executable(self):
        with mock.patch('kb_python.dry.utils.print') as p:
            self.assertIsNone(utils.run_executable(['1', '2', 3]))
            p.assert_called_once_with('1 2 3')

    def test_run_executable_quiet(self):
        with mock.patch('kb_python.dry.utils.print') as p:
            self.assertIsNone(utils.run_executable(['1', '2', 3], quiet=True))
            p.assert_not_called()

    def test_make_directory(self):
        with mock.patch('kb_python.dry.utils.print') as p,\
            mock.patch('kb_python.dry.utils.PLATFORM', 'darwin'):
            self.assertIsNone(utils.make_directory('path'))
            p.assert_called()

    def test_make_directory_windows(self):
        with mock.patch('kb_python.dry.utils.print') as p,\
            mock.patch('kb_python.dry.utils.PLATFORM', 'windows'):
            self.assertIsNone(utils.make_directory('path'))
            p.assert_called()

    def test_remove_directory(self):
        with mock.patch('kb_python.dry.utils.print') as p,\
            mock.patch('kb_python.dry.utils.PLATFORM', 'darwin'):
            self.assertIsNone(utils.remove_directory('path'))
            p.assert_called()

    def test_remove_directory_windows(self):
        with mock.patch('kb_python.dry.utils.print') as p,\
            mock.patch('kb_python.dry.utils.PLATFORM', 'windows'):
            self.assertIsNone(utils.remove_directory('path'))
            p.assert_called()

    def test_stream_file(self):
        with mock.patch('kb_python.dry.utils.print') as p,\
            mock.patch('kb_python.dry.utils.PLATFORM', 'darwin'):
            self.assertEqual('path', utils.stream_file('url', 'path'))
            p.assert_called()

    def test_stream_file_windows(self):
        with mock.patch('kb_python.dry.utils.print') as p,\
            mock.patch('kb_python.dry.utils.PLATFORM', 'windows'):
            with self.assertRaises(UnsupportedOSError):
                utils.stream_file('url', 'path')
            p.assert_not_called()

    def test_move_file(self):
        with mock.patch('kb_python.dry.utils.print') as p,\
            mock.patch('kb_python.dry.utils.PLATFORM', 'darwin'):
            self.assertEqual(
                'destination', utils.move_file('source', 'destination')
            )
            p.assert_called()

    def test_move_file_windows(self):
        with mock.patch('kb_python.dry.utils.print') as p,\
            mock.patch('kb_python.dry.utils.PLATFORM', 'windows'):
            self.assertEqual(
                'destination', utils.move_file('source', 'destination')
            )
            p.assert_called()

    def test_copy_whitelist(self):
        with mock.patch('kb_python.dry.utils.print') as p:
            self.assertEquals(
                'path/10x_version2_whitelist.txt',
                utils.copy_whitelist('10xv2', 'path')
            )
            p.assert_called()

    def test_create_10x_feature_barcode_map(self):
        with mock.patch('kb_python.dry.utils.print') as p:
            self.assertEqual(
                'path/to/feature/barcode/map',
                utils.
                create_10x_feature_barcode_map('path/to/feature/barcode/map')
            )
            p.assert_called()

    def test_get_temporary_filename(self):
        temp = utils.get_temporary_filename('temp')
        self.assertTrue(temp.startswith(os.path.join('temp', 'tmp')))
