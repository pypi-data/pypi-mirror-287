import glob
import os
import shutil
import unittest

from evo_downloader.downloader import Downloader


class TestDownloader(unittest.TestCase):
    def setUp(self):
        self.downloader = Downloader(num_threads=10)
        self.test_folder = "test_downloads"
        self.temp_folder = "./temp"
        if os.path.exists(self.test_folder):
            shutil.rmtree(self.test_folder)
        if os.path.exists(self.temp_folder):
            shutil.rmtree(self.temp_folder)
        os.makedirs(self.test_folder, exist_ok=True)

    def tearDown(self):
        if os.path.exists(self.test_folder):
            shutil.rmtree(self.test_folder)
        if os.path.exists(self.temp_folder):
            shutil.rmtree(self.temp_folder)

    def test_download_supports_range(self):
        file_url = "http://images.cocodataset.org/annotations/image_info_test2014.zip"
        file_name = "image_info_test2014.zip"
        file_urls = [file_url]

        downloaded_paths = self.downloader.download_files(file_urls, self.test_folder)
        output_file_path = downloaded_paths[0]

        self.assertTrue(os.path.isfile(output_file_path))
        self.assertGreater(os.path.getsize(output_file_path), 0)
        print(f"File '{file_name}' downloaded successfully with range support.")

    def test_download_not_support_range(self):
        file_url = "https://github.com/maycuatroi/evo_downloader/archive/refs/heads/main.zip"
        file_name = "coco128-seg.zip"
        file_urls = [file_url]

        downloaded_paths = self.downloader.download_files(file_urls, self.test_folder)
        output_file_path = downloaded_paths[0]

        self.assertTrue(os.path.isfile(output_file_path))
        self.assertGreater(os.path.getsize(output_file_path), 0)
        print(f"File '{file_name}' downloaded successfully without range support.")


if __name__ == "__main__":
    unittest.main()
