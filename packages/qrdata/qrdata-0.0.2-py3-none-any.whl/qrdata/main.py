import sys
from PyQt5.QtCore import pyqtSlot, QMetaObject
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from chardet.universaldetector import UniversalDetector

from qrdata.qrdata_ui import Ui_MainWindow  # 导入从.ui文件生成的UI类
from qrdata.qrcode_data import QRData
from qrdata.inputdata import InputData
from qrdata.qrcode_generator import QRCodeGenerator
from qrdata.logger import Logger

class MainWindow(QMainWindow):
    def __init__(self, qrdata, input_data):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QMetaObject.connectSlotsByName(self)

        self.qrdata = qrdata
        self.input_data = input_data
        self.logger = Logger(self.ui.logTextEdit)

        self.ui.versionSlider.valueChanged.connect(self.updateVersionLabel)
        self.ui.versionSlider.valueChanged.connect(lambda x: self.qrdata.set_version(self.ui.versionSlider.value()))
        self.ui.inputFilePushButton.clicked.connect(self.openFileDialog)
        self.ui.outputDirPushButton.clicked.connect(self.selectOutputDirectory)
        self.ui.runPushButton.clicked.connect(self.runPushButton_clicked)

        self.show()
    
    def updateVersionLabel(self):
        version_value = self.ui.versionSlider.value()
        self.ui.versionLabel.setText(str(version_value))

    def openFileDialog(self):
        selected_file, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*)")
        if selected_file:
            file_encoding, confidence = self.detcect_encoding(selected_file)
            log_str = "文件编码格式为：{}， 置信度为：{}".format(file_encoding, confidence)
            self.logger.log(log_str)
            if file_encoding != 'unknown' and confidence > 0.75:
                with open(selected_file, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                self.ui.inputTextTextEdit.setText(content)
            else:
                self.ui.inputTextTextEdit.setText(f"<span style='color:red;'>该文件为二进制文件</span>")
            self.ui.inputFileLineEdit.setText(selected_file)
    def selectOutputDirectory(self):
        selected_directory = QFileDialog.getExistingDirectory(self, "选择目录")
        if selected_directory:
            self.ui.outputDirLineEdit.setText(selected_directory)

    def detcect_encoding(self, filepath):
        """检测文件编码
        Args:
            detector: UniversalDetector 对象
            filepath: 文件路径
        Return:
            file_encoding: 文件编码
            confidence: 检测结果的置信度，百分比
        """
        detector = UniversalDetector()
        detector.reset()
        for each in open(filepath, 'rb'):
            detector.feed(each)
            if detector.done:
                break
        detector.close()
        file_encoding = detector.result['encoding']
        confidence = detector.result['confidence']
        if file_encoding is None:
            file_encoding = 'unknown'
            confidence = 0.99
        return file_encoding, confidence
    
    @pyqtSlot()
    def on_inputTextTextEdit_textChanged(self):
        text = self.ui.inputTextTextEdit.toPlainText()
        self.input_data.load_data(text, "utf-8")

    def runPushButton_clicked(self):
        version = int(self.ui.versionSlider.value())
        #判断errCorrGroupBox中哪一个radiobox被选中
        if self.ui.errCorrHRadioButton.isChecked():
            error_correction = "H"
        elif self.ui.errCorrQRadioButton.isChecked():
            error_correction = "Q"
        elif self.ui.errCorrMRadioButton.isChecked():
            error_correction = "M"
        elif self.ui.errCorrLRadioButton.isChecked():
            error_correction = "L"
        data = self.ui.inputTextTextEdit.toPlainText()
        output_dir = self.ui.outputDirLineEdit.text()
        generator = QRCodeGenerator(version, error_correction, data, output_dir, self.logger)
        generator.generate_qrcodes()

def main():
    app = QApplication(sys.argv)
    qr_data = QRData()
    input_data = InputData()
    window = MainWindow(qr_data, input_data)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()