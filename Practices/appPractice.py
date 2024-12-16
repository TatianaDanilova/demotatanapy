# Импорт библиотек
import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QStackedWidget,
    QApplication,
    QVBoxLayout,
    QWidget)

from Practices import ScrollAreasPractice


class Application(QWidget):
    ''' Класс приложения '''

    def __init__(self):
        QWidget.__init__(self)
        """ Настройка параметров приложения """
        # Установка названия окна
        self.setWindowTitle("Практики Олега")

        # Установка стартовых значений Ширина / Высота
        self.resize(QSize(800, 800))

        # Установка максимальных значений для расширения
        # Не дает объектам в окне самим его масштабировать и сохранит возможность уменьшать окно пользователю
        self.setMaximumSize(QSize(800, 800))

        self.buttonPractice = ScrollAreasPractice.interface(self, self)

        self.frames_container = QStackedWidget()
        self.frames_container.addWidget(self.buttonPractice)

        frame = QVBoxLayout(self)
        frame.addWidget(self.frames_container)

styles = '''
#card {
    background: #F4E8D3;
    border: 1px solid black
}

#Heading{
    font-size: 18px;
    qproperty-alignment: AlignCenter;
    font-weight: bold
}

#btn_main_frame{
    font-size: 20px;
}

QLabel{
    font-family: Segoe UI;
    font-size: 15px;
}

QPushButton {
    background: #67BA80;
}
'''



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(styles)
    # Инициализация приложения
    main_window = Application()
    # Демонстрация главного окна
    main_window.show()
    sys.exit(app.exec())

