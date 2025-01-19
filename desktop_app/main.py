import asyncio, sys, requests, json
from datetime import date
import bcrypt
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
    QMessageBox, QTreeWidgetItem, QFrame, QDialog)
from main_window import Ui_MainWindow
from api import *
from add_employee_dialog import Ui_Dialog


class DialogWindow(QDialog):
    def __init__(self, employees, cabinets, job_titles,
                 organizations, sub_divisions, sub_sub_divisions):
        super().__init__()

        self.employees = employees
        self.cabinets = cabinets
        self.boss = employees
        self.helpers = employees
        self.job_titles = job_titles
        self.organizations = organizations
        self.sub_divisions = sub_divisions
        self.sub_sub_divisions = sub_sub_divisions

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setup_optional_fields()

        self.ui.btn_save.clicked.connect(self.save)

    def save(self):
        full_name = self.ui.input_full_name.text()
        date_of_birth = self.ui.input_date_of_birth.text()
        more_info = self.ui.input_more_info.toPlainText()
        home_number = self.ui.input_home_number.text()
        work_number = self.ui.input_work_phone.text()
        work_email = self.ui.input_work_email.text()

        helper = self.ui.optional_helpers.currentText()
        helper_id = get_employee_by_name(helper)
        boss = self.ui.optional_boss.currentText()
        boss_id = get_employee_by_name(boss)
        job_title = self.ui.optional_job_titles.currentText()
        job_title_id = get_job_title_by_name(job_title)
        cabinet = self.ui.optional_cabinets.currentText()
        cabinet_id = get_cabinet_by_name(cabinet)
        organization = self.ui.optional_organizations.currentText()
        organization_id = get_organization_by_name(organization)
        sub_division = self.ui.optional_sub_divisions.currentText()
        sub_division_id = get_sub_division_by_name(sub_division)
        sub_sub_division = self.ui.optional_department.currentText()
        sub_sub_division_id = get_sub_sub_division_by_name(sub_sub_division)

        day, month, year = date_of_birth.split('.')
        password = bcrypt.hashpw(full_name.encode(), bcrypt.gensalt()).decode()
        birthday = date(int(year), int(month), int(day))

        url = "http://127.0.0.1:8000/api/V1/employees"
        response = requests.post(url=url, json={
            "username": full_name,
            "password": password,
            "email": work_email,
            "work_phone": work_number,
            "more_info": more_info,
            "birthday": str(birthday),
            "personal_phone": home_number,
            "position_id": job_title_id,
            "cabinet_id": cabinet_id,
            "boss_id": boss_id,
            "helper_id": helper_id,
            "organization": organization_id,
            "subdivision": sub_division_id,
            "sub_sub_division": sub_sub_division_id
        })

        print(response.content)


    def setup_optional_fields(self):
        self.ui.optional_boss.addItems(self.employees)
        self.ui.optional_cabinets.addItems(self.cabinets)
        self.ui.optional_boss.addItems(self.employees)
        self.ui.optional_job_titles.addItems(self.job_titles)
        self.ui.optional_helpers.addItems(self.employees)
        self.ui.optional_organizations.addItems(self.organizations)
        self.ui.optional_sub_divisions.addItems(self.sub_divisions)
        self.ui.optional_department.addItems(self.sub_sub_divisions)
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.employees = get_employees()
        self.cabinets = get_cabinets()
        self.job_titles = get_job_titles()
        self.organizations = [str(org['title']) for org in get_organizations()]
        self.sub_divisions = [str(sub_d['title']) for sub_d in get_subdivisions()]
        self.sub_sub_divisions = [str(sub_sub_d['title']) for sub_sub_d in get_sub_sub_divisions()]

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_tree_widget()

        self.ui.treeWidget_departments.itemClicked.connect(self.item_selected)
        self.ui.employee_add_button.clicked.connect(self.add_employee)


    def add_employee(self):
        dialog = DialogWindow(self.employees, self.cabinets,
                              self.job_titles, self.organizations,
                              self.sub_divisions, self.sub_sub_divisions)
        dialog.exec()


    def item_selected(self, item: QTreeWidgetItem, column: int):
        self.ui.listWidget.clear()
        users = get_employees_by_department(item.text(column))

        for user in users:
            self.ui.listWidget.addItem(user['username'])



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
