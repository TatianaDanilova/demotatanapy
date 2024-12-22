# Импорт библиотек
import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QStackedWidget,
    QApplication,
QVBoxLayout,
    QWidget)

import PartnerStaticName
from Frames import Partners, AddPartner, PartnerInfo
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

        self.firstFrame = Partners.interface(self, self)
        self.RegPartner = AddPartner.interface_reg_parther(self, self)

        self.frames_container = QStackedWidget()
        self.frames_container.addWidget(self.firstFrame)
        self.frames_container.addWidget(self.RegPartner)


        frame = QVBoxLayout(self)
        frame.addWidget(self.frames_container)

    def switch_to_new_frame(self, frame, current_partner_name: str = None):
        if current_partner_name != None:
            PartnerStaticName.Partner.set_name(current_partner_name)

        current_frame_to_show = frame(self, self)

        print("Переданное объектное имя: ", current_frame_to_show)

        self.frames_container.removeWidget(current_frame_to_show)

        self.frames_container.addWidget(current_frame_to_show)
        self.frames_container.setCurrentWidget(current_frame_to_show)




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
QLineEdit{
    height: 30px;
}

#label_procent{
    qproperty-alignment: AlignRight;
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
#PartnerInfo {
    background: #F4E8D3;
}

#TitleInfo{
    font-weight: bold;
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

