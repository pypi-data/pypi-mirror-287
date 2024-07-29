import base64

class InputData:
    def __init__(self):
        self.data = bytearray()
        self.text = ""
        self.length = 0
        self.encoding = "unknown"

    #如果encoding为“binary”，则调用base64_convert转为文本，否则将data直接赋予text
    def load_data(self, data, encoding):
        self.data = data
        self.encoding = encoding
        if self.encoding == "binary":
            self.base64_convert(self.data)
        else:
            self.text = self.data
            self.length = len(self.text)

    def base64_convert(self, data):
        self.text = base64.b64decode(data)
        self.length = len(self.text)