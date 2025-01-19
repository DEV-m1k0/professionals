import asyncio, sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QModelIndex)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,
    QResizeEvent)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget, QTableWidgetItem, QFileDialog,
    QMessageBox, QTreeWidgetItem, QFrame)
from main_window import Ui_MainWindow
from api import (
                get_organizations, get_subdivision_by_id, get_sub_sub_division_by_id,
                get_employees_by_department
                )


# class Window(QFrame):
#     def __init__(self, parent=None):
#         super().__init__(parent)        
#         self.setObjectName(u"window")

#         self.dialog = Dialog(self)
#         self.dialog.setObjectName(u"dialog")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_tree_widget()

        self.ui.treeWidget_departments.itemClicked.connect(self.item_selected)
        # self.ui.listWidget.addItem(QListWidgetItem("Some"))
        # self.ui.listWidget.itemClicked.connect(self.employee_selected)


    # def employee_selected(self):
    #     window = Window()


    def item_selected(self, item: QTreeWidgetItem, column: int):
        users = get_employees_by_department(item.text(column))

        self.ui.listWidget.addItems(users)


    def setup_tree_widget(self):
        tree_widget = self.ui.treeWidget_departments
        tree_widget.setColumnCount(1)


        organizations = get_organizations()
        for organization in organizations:
            top_lvl = QTreeWidgetItem([organization['title']])
            for subdivision_id in organization["subdivisions"]:
                subdivision = get_subdivision_by_id(subdivision_id)
                bottom_lvl = QTreeWidgetItem([subdivision["title"]])
                top_lvl.addChild(bottom_lvl)
                for sub_sub_division_id in subdivision["sub_sub_division"]:
                    sub_sub_division = get_sub_sub_division_by_id(sub_sub_division_id)
                    if sub_sub_division:
                        next_bottom_lvl = QTreeWidgetItem([sub_sub_division['title']])
                        bottom_lvl.addChild(next_bottom_lvl)
            tree_widget.addTopLevelItem(top_lvl)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
