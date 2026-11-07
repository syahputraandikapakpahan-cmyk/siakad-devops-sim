   import unittest
   from krs import bisa_ambil_kelas


   class TestKrs(unittest.TestCase):
       def test_kelas_kosong(self):
           self.assertTrue(bisa_ambil_kelas(40, 0))

       def test_masih_ada_kursi(self):
           self.assertTrue(bisa_ambil_kelas(40, 39))

       def test_kelas_penuh_ditolak(self):
           self.assertFalse(bisa_ambil_kelas(40, 40))


   if __name__ == "__main__":
       unittest.main()
