import csv
import qrcode
from qrdata.logger import Logger
import os

class QRCodeGenerator:
    def __init__(self, version, error_correction, data, output_dir, logger):
        self.version = version
        self.error_correction = error_correction
        self.data = data
        self.qrcodes = []
        self.output_dir = output_dir
        self.logger = logger

    def generate_qrcodes(self):
        #读取qrcode.csv文件，基于version和error_correction的值从文件中筛选出特定的行
        max_bytes = 0
        #得到当前文件所在的目录
        current_dir = os.path.dirname(__file__)
        with open(os.path.join(current_dir, 'data/qrcode.csv'), 'r') as file:
            reader = csv.reader(file)
            #不读取header
            next(reader)
            for row in reader:
                if int(row[0]) == self.version and row[1] == self.error_correction:
                    max_bytes = int(row[4])
                    #将max_bytes凑整为100的整数倍
                    max_bytes = max_bytes - max_bytes % 100
                    break

        for i in range(0, len(self.data), max_bytes):
            chunk = self.data[i:i + max_bytes]
            if self.error_correction == "H":
                error_correction=qrcode.constants.ERROR_CORRECT_H
            elif self.error_correction == "M":
                error_correction=qrcode.constants.ERROR_CORRECT_M
            elif self.error_correction == "L":
                error_correction=qrcode.constants.ERROR_CORRECT_L
            elif self.error_correction == "Q":
                error_correction=qrcode.constants.ERROR_CORRECT_Q
            qr = qrcode.QRCode(
                version=self.version,
                error_correction=error_correction,
                box_size=10,
                border=4,
            )
            qr.add_data(chunk)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            self.qrcodes.append(img)
        self.save_qrcodes(self.output_dir)
            
    def save_qrcodes(self, output_dir):
        for i, qrcode in enumerate(self.qrcodes):
            filename = f"qrcode_{i}.png"
            filepath = output_dir + "/" + filename
            qrcode.save(filepath)
            self.logger.log("Saved QR code to: " + filepath + "\n")
        self.logger.log("All QR codes saved to: " + output_dir + "\n")