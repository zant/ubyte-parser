import numpy as np

IMAGE_MODE = "i"
LABEL_MODE = "l"

class UByte:
    isValid = False

    @staticmethod
    def show_image(image):
        for row in image:
            for pixel in row:
                symbol = "#" if pixel > 127 else "%"
                print(symbol, end='')
            print("")

    def __init__(self, path, mode="i", read=10):
        if mode != "i":
            raise "Parsing labels is coming")

        self.path = path
        self.read = read
        self.file = open(self.path, 'rb')
        self.validate()

        self.parse_header()
        self.parse_contents()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        
    def validate(self):
        if self.isValid:
            return 

        if self.read_bytes(4) == 2051:
            self.isValid = True

    def read_bytes(self, size):
        return self.to_int(self.file.read(size))

    def parse_header(self):
        self.count = self.read_bytes(4)
        self.rows = self.read_bytes(4)
        self.cols = self.read_bytes(4)

    def parse_contents(self): 
        buf = self.file.read(self.read * self.cols * self.rows)
        data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
        data = data.reshape(self.read, self.rows, self.cols)
        self.data = data

    def to_int(self, b):
        return int.from_bytes(b, "big")
