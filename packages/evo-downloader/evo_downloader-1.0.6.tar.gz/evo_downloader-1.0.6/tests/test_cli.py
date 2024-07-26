import os
import shutil
import unittest
from click.testing import CliRunner
from evo_downloader.cli import cli


class TestCli(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.test_folder = os.path.abspath("test_downloads")
        if os.path.exists(self.test_folder):
            shutil.rmtree(self.test_folder)
        os.makedirs(self.test_folder, exist_ok=True)

    def tearDown(self):
        if os.path.exists(self.test_folder):
            shutil.rmtree(self.test_folder)

    def test_download_command_supports_range(self):
        result = self.runner.invoke(
            cli,
            [
                "download",
                "http://images.cocodataset.org/annotations/image_info_test2014.zip",
                "--folder",
                self.test_folder,
                "--num-threads",
                "10",
            ],
        )

        self.assertEqual(result.exit_code, 0)
        downloaded_file_path = os.path.join(self.test_folder, "image_info_test2014.zip")
        self.assertTrue(os.path.isfile(downloaded_file_path))
        self.assertGreater(os.path.getsize(downloaded_file_path), 0)
        print("File 'image_info_test2014.zip' downloaded successfully with range support.")

    def test_download_command_not_support_range(self):
        result = self.runner.invoke(
            cli,
            [
                "download",
                "https://github.com/maycuatroi/evo_downloader/archive/refs/heads/main.zip",
                "--folder",
                self.test_folder,
                "--num-threads",
                "10",
            ],
        )

        self.assertEqual(result.exit_code, 0)
        downloaded_file_path = os.path.join(self.test_folder, "main.zip")
        self.assertTrue(os.path.isfile(downloaded_file_path))
        self.assertGreater(os.path.getsize(downloaded_file_path), 0)
        print("File 'evo_downloader.zip' downloaded successfully without range support.")


if __name__ == "__main__":
    unittest.main()
