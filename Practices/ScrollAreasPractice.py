from PySide6.QtWidgets import (
    QVBoxLayout,
QLabel,
QPushButton,
QFrame,
QScrollArea,
QWidget,
QHBoxLayout
)

class interface(QFrame):
    def __init__(self, parent, controller):
        QFrame.__init__(self, parent)
        self.controller = controller

        self.update_start_values()
        self.setLayout(self.container)


    def update_start_values(self):
        self.container = QVBoxLayout()

        self.heading_up = QLabel("Верхний заголовок")
        self.heading_up.setObjectName("Heading")
        self.container.addWidget(self.heading_up)

        self.hcontainer = QHBoxLayout()
        # scroll area
        self.scroll_area_up1 = self.create_scroll_area()
        self.hcontainer.addWidget(self.scroll_area_up1)
        self.scroll_area_up2 = self.create_scroll_area()
        self.hcontainer.addWidget(self.scroll_area_up2)
       
        self.container.addLayout(self.hcontainer)

        self.btn = QPushButton("верхняя кнопка")
        self.btn.setObjectName("btn_main_frame")
        self.container.addWidget(self.btn)

        self.heading_down = QLabel("Нижний заголовок")
        self.heading_down.setObjectName("Heading")
        self.container.addWidget(self.heading_down)

        self.scroll_area_down = self.create_scroll_area()
        self.container.addWidget(self.scroll_area_down)

        self.btn = QPushButton("нижняя кнопка")
        self.btn.setObjectName("btn_main_frame")
        self.container.addWidget(self.btn)

        self.scroll_area_up1.setWidget(self.create_card())
        self.scroll_area_up2.setWidget(self.create_card())
        self.scroll_area_down.setWidget(self.create_card())


    def create_scroll_area(self):
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        return self.scroll_area

    def create_scroll_area_widget_container(self):
        self.sa_widget_container = QWidget()
        return self.sa_widget_container

    def create_card(self):
        self.scroll_area_widget_container = (self.create_scroll_area_widget_container())
        self.card_layout = QVBoxLayout(self.scroll_area_widget_container)


        for card in range(10):
            self.partner_card = QWidget()
            self.partner_card.setObjectName("card")
            self.vbox = QVBoxLayout(self.partner_card)

            self.label1 = QLabel("первичный текст")
            self.vbox.addWidget(self.label1)

            self.label2 = QLabel("вторичный текст")
            self.vbox.addWidget(self.label2)

            self.label3 = QLabel("третичный текст")
            self.vbox.addWidget(self.label3)

            self.btn = QPushButton("кнопка на карточке")
            self.vbox.addWidget(self.btn)

            self.card_layout.addWidget(self.partner_card)


        return self.scroll_area_widget_container