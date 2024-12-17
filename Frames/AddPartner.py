# импорт библиотек
from PySide6.QtWidgets import (
    QVBoxLayout,
    QFrame,
    QWidget,
    QPushButton,
    QLabel,
    QScrollArea,
    QLineEdit
)

from Frames import MessageBox

class interface_reg_parther(QFrame):
    def __init__ (self, parent, controller):
        QFrame.__init__(self, parent)
        self.controller = controller
        self.connection = controller.connection
        self.update_start_values()

        # добавление виджет лаяута во фрейм
        self.setLayout(self.widgets_layout_conainer)

    def update_start_values(self):
        self.widgets_layout_conainer = QVBoxLayout()

        self.widgets_layout_conainer.addWidget(QLabel("Введите имя"))
        self.input_partner_name = self.create_patern_QLineEdit("Ввод имени")

        self.widgets_layout_conainer.addWidget(QLabel("Введите тип партнера"))
        self.input_partner_type = self.create_patern_QLineEdit("Ввод типа партнера")

        self.widgets_layout_conainer.addWidget(QLabel("Введите имя директора"))
        self.input_partner_director = self.create_patern_QLineEdit("Ввод имени директора")

        self.widgets_layout_conainer.addWidget(QLabel("Введите телефон"))
        self.input_partner_phone = self.create_patern_QLineEdit("Ввод телефона")

        self.widgets_layout_conainer.addWidget(QLabel("Введите почту"))
        self.input_partner_mail = self.create_patern_QLineEdit("Ввод почты")

        self.widgets_layout_conainer.addWidget(QLabel("Введите юридический адрес"))
        self.input_partner_ur_addr = self.create_patern_QLineEdit("Ввод юридического адреса")

        self.widgets_layout_conainer.addWidget(QLabel("Введите инн"))
        self.input_partner_inn = self.create_patern_QLineEdit("Ввод инн")

        self.widgets_layout_conainer.addWidget(QLabel("Введите рейтинг"))
        self.input_partner_rate = self.create_patern_QLineEdit("Ввод рейтинга")

        self.btn_add_partner_to_db = QPushButton("Добавить партнера")
        self.btn_add_partner_to_db.clicked.connect(self.add_partner_to_db)
        self.widgets_layout_conainer.addWidget(self.btn_add_partner_to_db)


    def create_patern_QLineEdit(self, placeholder_text):
        input_text = QLineEdit()
        input_text.setPlaceholderText(placeholder_text)
        self.widgets_layout_conainer.addWidget(input_text)
        return input_text

    def add_partner_to_db(self):
        self.info_from_user = {
            "name": self.input_partner_name.text(),
            "type": self.input_partner_type.text(),
            "director": self.input_partner_director.text(),
            "phone": self.input_partner_phone.text()[3:],
            "mail": self.input_partner_mail.text(),
            "ur_addr": self.input_partner_ur_addr.text(),
            "inn": self.input_partner_inn.text(),
            "rate": self.input_partner_rate.text(),
        }
        print(self.info_from_user)

        MessageBox.send_info_message_box("Партнер добавлен")






