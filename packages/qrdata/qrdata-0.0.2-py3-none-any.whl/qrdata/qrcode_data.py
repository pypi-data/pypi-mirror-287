from qrdata.enums import *
class QRData:
    def __init__(self):
        self.version = 40
        self.err_correct_level = QrCodeVersion.HIGH
        self.mode = QrCodeMode.Auto
    def set_version(self, version):
        self.version = version

    def set_err_correct_level(self, err_correct_level):
        self.err_correct_level = err_correct_level

    def set_mode(self, mode):
        self.mode = mode