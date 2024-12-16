from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFrame, QWidget, QScrollArea
)

class PracticeInterface(QFrame):
    def __init__(self, parent, controller):
        QFrame.__init__(self, parent)
        self.controller = controller
        # вызываем функцию, в которой содержатся все виджеты
        self.update_start_values()

        # присваиваем лаяуту созданный в предыдущей функции контейнер
        self.setLayout(self.container)


    def update_start_values(self):
        # делаем так, чтобы все виджеты равномерно распредилялись по лаяуту
        self.container = QVBoxLayout(self)

        # создаем текст
        self.first_label = QLabel("Первый текст")
        # присваиваем лэйблу имя
        self.first_label.setObjectName("first_label")
        # вставляем текст в контейнер
        self.container.addWidget(self.first_label)

        self.second_label = QLabel("Обычный текст")
        self.second_label.setObjectName("second_label")
        self.container.addWidget((self.second_label))

        self.finish_label = QLabel("Завершающий")
        self.finish_label.setObjectName("finish_label")
        self.container.addWidget(self.finish_label)

        # создаем кнопку, которая вызывает функцию
        self.change_btn = QPushButton("Поменять на DONE")
        self.change_btn.setObjectName("change_btn")
        # вызываем функцию (! не забывать убирать скобки !)
        self.change_btn.clicked.connect(
            self.change_text
        )
        # вставляем кнопку в контенер
        self.container.addWidget(self.change_btn)

        # создаем кнопки лямбду
        self.print_btn = QPushButton("Вывод")
        self.print_btn.setObjectName("print_btn")
        self.print_btn.clicked.connect(
            lambda : print("Интресный текст")
        )
        self.container.addWidget(self.print_btn)

        self.click_btn = QPushButton("Поменять на NOT")
        self.click_btn.setObjectName("click_btn")
        self.click_btn.clicked.connect(
            lambda :self.first_label.setText("NOT")
        )
        self.container.addWidget(self.click_btn)


    def change_text(self):
        self.first_label.setText("DONE")








