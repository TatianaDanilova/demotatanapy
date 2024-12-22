from PySide6.QtWidgets import (
    QVBoxLayout,
    QFrame,
    QWidget,
    QPushButton,
    QLabel,
    QScrollArea
)

import PartnerStaticName
from Frames import AddPartner, Partners, UpdatePartnerInfo


class interfacePartnerInfo(QFrame):
    def __init__ (self, parent, controller):
        QFrame.__init__(self, parent)

        self.controller = controller
        self.connection = controller.connection
        self.update_start_values()

        # добавление виджет лаяута во фрейм
        self.setLayout(self.widgets_layout_conainer)

    # в нем хранятся все элементы интерфейса
    def update_start_values(self):
        # вртикальная разметка контейнера
        self.widgets_layout_conainer = QVBoxLayout(self)

        self.single_partner_info = self.connection.take_current_parent_info(PartnerStaticName.Partner.return_name())

        print(self.single_partner_info)

        self.widgets_layout_conainer.addWidget(self.qlabel_pattenr_title("Имя партнера"))
        self.widgets_layout_conainer.addWidget(self.qlabel_pattenr_info(self.single_partner_info[0]['name']))

        self.widgets_layout_conainer.addWidget(self.qlabel_pattenr_title("Тип партнера"))
        self.widgets_layout_conainer.addWidget(self.qlabel_pattenr_info(self.single_partner_info[0]['type']))

        self.widgets_layout_conainer.addWidget(self.qlabel_pattenr_title("Имя директора партнера"))
        self.widgets_layout_conainer.addWidget(self.qlabel_pattenr_info(self.single_partner_info[0]['director']))

        self.widgets_layout_conainer.addWidget(self.qlabel_pattenr_title("Телефон"))
        self.widgets_layout_conainer.addWidget(self.qlabel_pattenr_info(f'+7 {self.single_partner_info[0]["phone"]}'))

        self.widgets_layout_conainer.addWidget(self.qlabel_pattenr_title("Юридический адрес партнера"))
        self.widgets_layout_conainer.addWidget(self.qlabel_pattenr_info(self.single_partner_info[0]['ur_addr']))

        self.widgets_layout_conainer.addWidget(self.qlabel_pattenr_title("ИНН партнера"))
        self.widgets_layout_conainer.addWidget(self.qlabel_pattenr_info(self.single_partner_info[0]['inn']))

        self.widgets_layout_conainer.addWidget(self.qlabel_pattenr_title("Почта партнера"))
        self.widgets_layout_conainer.addWidget(self.qlabel_pattenr_info(self.single_partner_info[0]['mail']))

        self.widgets_layout_conainer.addWidget(self.qlabel_pattenr_title("Рейтинг партнера"))
        self.widgets_layout_conainer.addWidget(self.qlabel_pattenr_info(f"{self.single_partner_info[0]['rate']}"))

        self.btn_update = QPushButton("Обновить партнера")
        self.btn_update.clicked.connect(lambda : self.controller.switch_to_new_frame(UpdatePartnerInfo.interface_update_parther_info))
        self.widgets_layout_conainer.addWidget(self.btn_update)

        self.btn_back = QPushButton("Назад")
        self.btn_back.clicked.connect(lambda : self.controller.switch_to_new_frame(Partners.interface))
        self.widgets_layout_conainer.addWidget(self.btn_back)

    def qlabel_pattenr_info(self, text):
        label = QLabel(text)
        label.setObjectName("PartnerInfo")
        return label

    def qlabel_pattenr_title(self, text):
        label = QLabel(text)
        label.setObjectName("TitleInfo")
        return label