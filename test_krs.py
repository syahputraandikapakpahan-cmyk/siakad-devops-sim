import unittest
from krs import bisa_ambil_kelas


class TestKrs(unittest.TestCase):
    def test_kelas_kosong(self):
        self.assertTrue(bisa_ambil_kelas(40, 0))


if __name__ == "__main__":
    unittest.main()
