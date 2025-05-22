import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class FormMahasiswa(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Form Input Data Mahasiswa')
        self.setGeometry(100, 100, 400, 200)
        self.initUI()

    def initUI(self):
        # Label dan Input untuk Nama
        self.label_nama = QLabel('Nama:', self)
        self.label_nama.move(20, 20)
        self.input_nama = QLineEdit(self)
        self.input_nama.move(150, 20)

        self.label_nim = QLabel('NIM:', self)
        self.label_nim.move(20, 60)
        self.input_nim = QLineEdit(self)
        self.input_nim.move(150, 60)

        self.label_prodi = QLabel('Program Studi:', self)
        self.label_prodi.move(20, 100)
        self.input_prodi = QLineEdit(self)
        self.input_prodi.move(150, 100)

        self.tombol = QPushButton('Tampilkan Data', self)
        self.tombol.move(150, 140)
        self.tombol.clicked.connect(self.tampilkan_data)

    def tampilkan_data(self):
        nama = self.input_nama.text()
        nim = self.input_nim.text()
        prodi = self.input_prodi.text()

        message = QMessageBox()
        message.setWindowTitle('Data Mahasiswa')
        message.setText(f'Nama: {nama}\nNIM: {nim}\nProgram Studi: {prodi}')
        message.exec_()

    # def tampilkan_data(self):
    #     nama = self.input_nama.text()
    #     nim = self.input_nim.text()

    #     prodi = self.input_prodi.text()
    #     print(f'Nama: {nama}\nNIM: {nim}\nProgram Studi: {prodi}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormMahasiswa()
    window.show()
    sys.exit(app.exec_())