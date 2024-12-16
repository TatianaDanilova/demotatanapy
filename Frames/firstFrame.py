# импорт библиотек
from PySide6.QtWidgets import (
    QVBoxLayout,
    QFrame,
    QWidget,
    QPushButton,
    QLabel,
    QScrollArea
)



class interface(QFrame):
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

        # создание заголовка
        self.heading = QLabel("Партнеры")
        self.heading.setObjectName("heading1")
        # добавление заголовка в котнейнер
        self.widgets_layout_conainer.addWidget(self.heading)

        # перемнная с функцией добавления скролла
        self.ScrollArea = self.create_scroll_area()
        # добавление скролла в контейнер
        self.widgets_layout_conainer.addWidget(self.ScrollArea)

        # создание кнопки внизу фрейма
        self.btn = QPushButton("Добавить партнера")
        self.btn.clicked.connect(
            lambda : print("Добавить"))
        # добавление кнопки в контейнер
        self.widgets_layout_conainer.addWidget(self.btn)

        # добавление карточки в контейнер скролла
        self.ScrollArea.setWidget(self.create_partner_card())


    '''Функция создания скрола'''
    def create_scroll_area(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        return scroll_area

    '''Функция создания контейнера карточек товара'''
    def create_scroll_area_widget_container(self):
        scroll_area_widget_container = QWidget()
        return scroll_area_widget_container

    '''Создание кароточки товара'''
    def create_partner_card(self):
        # создали контейнер для карточки товара
        self.scroll_area_widget_container = (self.create_scroll_area_widget_container())
        # установка вертикальной разметки для контейнера карточек
        self.card_layout = QVBoxLayout(self.scroll_area_widget_container)


        # цикл для вывода карточек партнеров
        for partner in self.connection.take_partner_information():
            # создание виджета (поле карточки)
            self.partner_card = QWidget()
            self.partner_card.setObjectName("partner_card")
            # вертикальная разметка для карточки
            self.vbox = QVBoxLayout(self.partner_card)
            # первый лебл
            self.label1 = QLabel(f'{partner["name"]}')
            self.vbox.addWidget(self.label1)
            self.label1.setObjectName("company_name")


            self.label2 = QLabel(f'Телефон {partner["phone"]}')
            self.vbox.addWidget(self.label2)
            self.label2.setObjectName("company_phone")

            self.label3 = QLabel(f'ИНН {partner["inn"]}')
            self.vbox.addWidget(self.label3)
            self.label3.setObjectName("company_inn")

            self.btn_to_partner_info = QPushButton("Подробнее")
            self.vbox.addWidget(self.btn_to_partner_info)

            # добавление карточки в лайаут для карточки
            self.card_layout.addWidget(self.partner_card)
        return self.scroll_area_widget_container

    def ptint_btn_obj_name(self):
        sender = self.sender()
        print("button name: ", sender.objectName())


