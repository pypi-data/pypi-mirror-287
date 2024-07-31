import numpy as np

class QRCodeGenerator:
    def __init__(self, version=1):
        self.version = version
        self.size = self._calculate_size(version)
        self.matrix = np.zeros((self.size, self.size), dtype=int)

    def _calculate_size(self, version):
        return 21 + (version - 1) * 4

    def encode_data(self, data):
        # Encode data (alphanumeric encoding for simplicity)
        encoded_data = []
        for char in data:
            encoded_data.append(format(ord(char), '08b'))
        return ''.join(encoded_data)

    def add_finder_patterns(self):
        patterns = [
            (0, 0),
            (0, self.size - 7),
            (self.size - 7, 0)
        ]
        for row, col in patterns:
            self._add_finder_pattern(row, col)

    def _add_finder_pattern(self, row, col):
        pattern = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]
        for i in range(7):
            for j in range(7):
                self.matrix[row + i, col + j] = pattern[i][j]

    def generate_qr(self, data):
        self.add_finder_patterns()
        encoded_data = self.encode_data(data)
        self._place_data(encoded_data)
        return self.matrix

    def _place_data(self, encoded_data):
        # Place the data bits in the QR matrix (simplified)
        idx = 0
        for i in range(self.size - 1, -1, -2):
            for j in range(self.size):
                if idx < len(encoded_data):
                    self.matrix[j, i] = int(encoded_data[idx])
                    idx += 1
                if idx < len(encoded_data):
                    self.matrix[j, i - 1] = int(encoded_data[idx])
                    idx += 1

def utils(data):
    qr = QRCodeGenerator()
    return qr.generate_qr(data)
