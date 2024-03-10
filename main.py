import sys as System
from PyQt6.QtWidgets import QApplication
from qt_material import apply_stylesheet as applyStylesheet

from DAO import DAO
from MainWindow import MainWindow

app: QApplication = QApplication(System.argv)
applyStylesheet(app, "dark_yellow.xml")
window: MainWindow = MainWindow(app, DAO("database.db"))
System.exit(app.exec())
