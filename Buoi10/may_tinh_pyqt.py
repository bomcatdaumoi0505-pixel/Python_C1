import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton,
    QGridLayout, QMessageBox
)


class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("May tinh bo tu")
        self.resize(300, 400)

        self.entry_hien_thi = QLineEdit()
        self.entry_hien_thi.setStyleSheet("font-size: 18px;")

        layout = QGridLayout()
        layout.addWidget(self.entry_hien_thi, 0, 0, 1, 4)

        cac_nut = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, hang, cot) in cac_nut:
            nut = QPushButton(text)
            if text == '=':
                nut.setStyleSheet("font-size: 14px; background-color: #000000; color: white;")
                nut.clicked.connect(self.tinh_ket_qua)
            elif text == 'C':
                nut.setStyleSheet("font-size: 14px; background-color: #f43636; color: white;")
                nut.clicked.connect(self.xoa_man_hinh)
            else:
                nut.setStyleSheet("font-size: 14px;")
                nut.clicked.connect(lambda _, t=text: self.nhap_phim(t))
            layout.addWidget(nut, hang, cot)

        self.setLayout(layout)

    def nhap_phim(self, gia_tri):
        hien_tai = self.entry_hien_thi.text()
        self.entry_hien_thi.setText(hien_tai + str(gia_tri))

    def xoa_man_hinh(self):
        self.entry_hien_thi.clear()

    def tinh_ket_qua(self):
        bieu_thuc = self.entry_hien_thi.text()
        try:
            ket_qua = str(eval(bieu_thuc))
            self.entry_hien_thi.setText(ket_qua)
        except ZeroDivisionError:
            QMessageBox.critical(self, "Loi", "Khong the chia cho 0.")
            self.entry_hien_thi.clear()
        except Exception:
            QMessageBox.critical(self, "Loi", "Bieu thuc khong hop le.")
            self.entry_hien_thi.clear()


app = QApplication(sys.argv)
cua_so = MayTinhBoTui()
cua_so.show()
sys.exit(app.exec_())
