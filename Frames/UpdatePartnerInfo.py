# импорт библиотек
from PySide6.QtWidgets import (
    QVBoxLayout,
    QFrame,
    QPushButton,
    QLabel,
    QLineEdit
)

import MessageBox
from Frames import Partners, PartnerInfo
import PartnerStaticName


class interface_update_parther_info(QFrame):
    def __init__ (self, parent, controller):
        QFrame.__init__(self, parent)
        self.controller = controller
        self.connection = controller.connection
        self.update_start_values()

        # добавление виджет лаяута во фрейм
        self.setLayout(self.widgets_layout_conainer)

    def update_start_values(self):
        self.widgets_layout_conainer = QVBoxLayout()

        self.single_partner_info = self.connection.take_current_parent_info(PartnerStaticName.Partner.return_name())

        self.widgets_layout_conainer.addWidget(QLabel("Введите имя"))
        self.input_partner_name = self.create_patern_QLineEdit(self.single_partner_info[0]['name'].strip())

        self.widgets_layout_conainer.addWidget(QLabel("Введите тип партнера"))
        self.input_partner_type = self.create_patern_QLineEdit(self.single_partner_info[0]['type'].strip())

        self.widgets_layout_conainer.addWidget(QLabel("Введите имя директора"))
        self.input_partner_director = self.create_patern_QLineEdit(self.single_partner_info[0]['director'].strip())

        self.widgets_layout_conainer.addWidget(QLabel("Введите телефон"))

        self.input_partner_phone = self.create_patern_QLineEdit(self.single_partner_info[0]['phone'].strip())
        self.input_partner_phone.setInputMask("+7 000 000 00 00")

        self.widgets_layout_conainer.addWidget(QLabel("Введите почту"))
        self.input_partner_mail = self.create_patern_QLineEdit(self.single_partner_info[0]['mail'].strip())

        self.widgets_layout_conainer.addWidget(QLabel("Введите юридический адрес"))
        self.input_partner_ur_addr = self.create_patern_QLineEdit(self.single_partner_info[0]['ur_addr'].strip())

        self.widgets_layout_conainer.addWidget(QLabel("Введите инн"))
        self.input_partner_inn = self.create_patern_QLineEdit(self.single_partner_info[0]['inn'].strip())

        self.widgets_layout_conainer.addWidget(QLabel("Введите рейтинг"))
        self.input_partner_rate = self.create_patern_QLineEdit(str(self.single_partner_info[0]['rate']).strip())

        self.btn_add_partner_to_db = QPushButton("Обновить партнера")
        self.btn_add_partner_to_db.clicked.connect(self.add_partner_to_db)
        self.widgets_layout_conainer.addWidget(self.btn_add_partner_to_db)

        self.btn_back = QPushButton("Назад")
        self.btn_back.clicked.connect(lambda : self.controller.switch_to_new_frame(PartnerInfo.interfacePartnerInfo))
        self.widgets_layout_conainer.addWidget(self.btn_back)


    def create_patern_QLineEdit(self, placeholder_text):
        input_text = QLineEdit()
        input_text.setText(placeholder_text)
        self.widgets_layout_conainer.addWidget(input_text)
        return input_text

    def add_partner_to_db(self):
        self.info_from_user: dict = {
            "name": self.input_partner_name.text(),
            "type": self.input_partner_type.text(),
            "director": self.input_partner_director.text(),
            "phone": self.input_partner_phone.text()[3:],
            "mail": self.input_partner_mail.text(),
            "ur_addr": self.input_partner_ur_addr.text(),
            "inn": self.input_partner_inn.text(),
            "rate": self.input_partner_rate.text()
        }
        print(self.info_from_user)

        if self.connection.update_partner_info(PartnerStaticName.Partner.return_name(), self.info_from_user):
            print("oke")
            PartnerStaticName.Partner.set_name(self.input_partner_name.text())
            MessageBox.send_info_message_box("Партнер обнавлен")
            return
        print('not oke')
        return





