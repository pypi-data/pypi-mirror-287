import unittest
from QRCraft import utils

class TestQRCodeGenerator(unittest.TestCase):
    def test_generate_qr_code(self):
        data = "HELLO"
        qr_matrix = generate_qr_code(data)
        self.assertIsNotNone(qr_matrix)
        self.assertEqual(qr_matrix.shape[0], qr_matrix.shape[1])

if __name__ == '__main__':
    unittest.main()
