# Импорт библиотек
import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QStackedWidget,
    QApplication,
QVBoxLayout,
    QWidget)

from Frames import firstFrame
from database_work import database

class Application(QWidget):
    ''' Класс приложения '''
    def __init__(self):

        QWidget.__init__(self)
        """ Настройка параметров приложения """
        # Установка названия окна
        self.setWindowTitle("MainWindow")

        # Установка стартовых значений Ширина / Высота
        self.resize(QSize(800, 800))

        # Установка максимальных значений для расширения
        # Не дает объектам в окне самим его масштабировать и сохранит возможность уменьшать окно пользователю
        self.setMaximumSize(QSize(800, 800))

        self.connection = database.Database()

        self.firstFrame = firstFrame.interface(self, self)

        self.frames_container = QStackedWidget()
        self.frames_container.addWidget(self.firstFrame)

        frame = QVBoxLayout(self)
        frame.addWidget(self.frames_container)



styles = '''
QLabel {
    color: #000000;
    font-size: 20px;
    qproperty-alignment: AlignLeft;
    } 
QPushButton{
    background: #67BA80;
    color: #000000;
    font-size: 20px;
}
#partner_card {
    background: #F4E8D3;
    border: 1px solid #000000;
}
#card_btn {
    background: #67BA80;
    color: #000000;
    font-size: 20px;
}
#heading1 {
    color: #000000;
    qproperty-alignment: AlignCenter;
    font-size: 30px;
    font-weight: bold;
}
#procent{
    qproperty-alignment: AlignRight;
}

#company_name{
    font-weight: bold;
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

