from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLineEdit, QPushButton, QScrollArea, QWidget

from DAO import DAO


class MainWindow(QScrollArea):
    def __init__(self, app: QApplication, dao: DAO):
        super().__init__()
        self.setWidgetResizable(True)
        self.widget = QWidget()
        self.__app: QApplication = app
        self.__dao: DAO = dao
        root: QVBoxLayout = QVBoxLayout(self.widget)
        self.__inputWord: QLineEdit = QLineEdit(self)
        root.addWidget(self.__inputWord)
        self.__inputWord.setPlaceholderText("Слово на английском")
        self.__inputTranslate: QLineEdit = QLineEdit(self)
        root.addWidget(self.__inputTranslate)
        self.__inputTranslate.setPlaceholderText("Перевод слова")
        self.__inputType: QLineEdit = QLineEdit(self)
        root.addWidget(self.__inputType)
        self.__inputType.setPlaceholderText("Тип слова")
        self.__pushBtn: QPushButton = QPushButton(self)
        self.__pushBtn.setText("Добавить в Базу Данных")
        self.__pushBtn.clicked.connect(self.onClick)
        root.addWidget(self.__pushBtn)
        self.setWidget(self.widget)
        self.showMaximized()

    def onClick(self):
        self.__dao.addWord(self.__inputWord.text(), self.__inputTranslate.text(), self.__inputType.text())
        self.__inputWord.setText("")
        self.__inputTranslate.setText("")
        self.__inputType.setText("")
