import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qrdata",
    version="0.0.2",
    author="netbuddy",
    author_email="netbuddy@qq.com",
    description="a tool that can generate qrcode from text or file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/netbuddy/qrcode",
    project_urls={
        "Bug Tracker": "https://github.com/netbuddy/qrcode/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Chinese (Simplified)",
    ],
    # package_dir={"": "qrdata"},
    include_package_data=True,  # 包含 MANIFEST.in 文件中指定的数据文件
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': ['qrdata = qrdata.main:main']},
    install_requires=[
        'chardet>=5.2.0',
        'click>=8.1.7',
        'numpy>=2.0.1',
        'opencv-python>=4.10.0.84',
        'pillow>=10.4.0',
        'pypng>=0.20220715.0',
        'PyQt5>=5.15.9',
        'pyqt5-plugins>=5.15.9.2.3',
        'PyQt5-Qt5>=5.15.2',
        'pyqt5-tools>=5.15.9.3.3',
        'PyQt5_sip>=12.15.0',
        'python-dotenv>=1.0.1',
        'pyzbar>=0.1.9',
        'qrcode>=7.4.2',
        'qt5-applications>=5.15.2.2.3',
        'qt5-tools>=5.15.2.1.3',
        'typing_extensions>=4.12.2',
        'zxing>=1.0.3'
    ],
    python_requires=">=3.6",
)
