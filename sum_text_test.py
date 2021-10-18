from SumText import addNumbers
import os
import shutil
import unittest


class SumTextTest(unittest.TestCase):
    def test_test1_return_value(self):
        open("tempFile.txt", 'w').close()
        shutil.copyfile("test1.txt", "tempFile.txt")
        self.assertEqual(addNumbers("tempFile.txt"), 153)

    def test_test1_write_value(self):
        open("tempFile.txt", 'w').close()
        shutil.copyfile("test1.txt", "tempFile.txt")
        total = addNumbers("tempFile.txt")
        with open("tempFile.txt", 'rb') as f:
            try:
                f.seek(-2, os.SEEK_END)
                while f.read(1) != b'\n':
                    f.seek(-2, os.SEEK_CUR)
                last_line = f.readline().decode()
            except OSError:
                f.seek(0)
        self.assertEqual(int(last_line), total)

    def test_non_existing_file(self):
        self.assertEqual(addNumbers("fakeFile.txt"), 0)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            addNumbers(0)

    def test_invalid_file_input(self):
        with self.assertRaises(ValueError):
            addNumbers("string.txt")

if __name__ == '__main__':
    unittest.main()
