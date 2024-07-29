from enum import Enum

#二维码版本
class QrCodeVersion(Enum):
    HIGH = 1
    Quarter = 2
    Middle = 3
    Low =4

#二维码模式
class QrCodeMode(Enum):
    Auto = 1
    Numeric = 2
    Alphanumeric = 3
    Byte = 4
    Kanji = 5
    ECI = 6