from PySide6.QtWidgets import (
    QVBoxLayout,
    QFrame,
    QPushButton,
    QLabel,
    QLineEdit,
    QTreeWidget,
    QTreeWidgetItem
)

import MessageBox
import PartnerStaticName
from Frames import Partners, PartnerInfo


class interface_history(QFrame):
    def __init__ (self, parent, controller):
        QFrame.__init__(self, parent)
        self.controller = controller
        self.connection = controller.connection
        self.update_start_values()

        # добавление виджет лаяута во фрейм
        self.setLayout(self.widgets_layout_conainer)

    def update_start_values(self):
        self.widgets_layout_conainer = QVBoxLayout()

        self.single_partner_history_info = self.connection.take_history_information(PartnerStaticName.Partner.return_name())

        print(self.single_partner_history_info)


        self.tablica = QTreeWidget()
        self.tablica.setHeaderLabels(["Продукт", "Партнер", "Количество", "Дата операции"])

        for key in self.single_partner_history_info:
            item = QTreeWidgetItem(self.tablica)
            item.setText(0, key['product_name_fk'])
            item.setText(1, key['partner_name_fk'])
            item.setText(2, key['history_products_count'])
            item.setText(3, key['history_sale_date'])

        self.widgets_layout_conainer.addWidget(self.tablica)

        self.btn_back = QPushButton("Назад")
        self.btn_back.clicked.connect(lambda : self.controller.switch_to_new_frame(PartnerInfo.interfacePartnerInfo))
        self.widgets_layout_conainer.addWidget(self.btn_back)