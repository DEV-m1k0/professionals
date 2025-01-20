from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)
from api import *
import bcrypt
from datetime import date
import add_employee_dialog, edit_employee


class EditEmployeeDialog(QDialog):
    def __init__(self, name, employees, cabinets, job_titles,
                 organizations, sub_divisions, sub_sub_divisions,
                 selected_department):
        super().__init__()

        self.name = name
        self.employees = employees
        self.cabinets = cabinets
        self.boss = employees
        self.helpers = employees
        self.job_titles = job_titles
        self.organizations = organizations
        self.sub_divisions = sub_divisions
        self.sub_sub_divisions = sub_sub_divisions
        self.selected_department = selected_department

        self.ui = edit_employee.Ui_Dialog()
        self.ui.setupUi(self)

        self.setup()

        self.ui.btn_save.clicked.connect(self.save)

    def setup(self):
        self.ui.optional_boss.addItems(self.employees)
        self.ui.optional_cabinets.addItems(self.cabinets)
        self.ui.optional_boss.addItems(self.employees)
        self.ui.optional_job_titles.addItems(self.job_titles)
        self.ui.optional_helpers_2.addItems(self.employees)
        self.ui.optional_organizations.addItems(self.organizations)
        self.ui.optional_sub_divisions.addItems(self.sub_divisions)
        self.ui.optional_department.addItems(self.sub_sub_divisions)

        employee = get_employee_by_name(self.name)
        self.employee = employee

        try:
            self.ui.input_full_name_2.setText(employee['username'])
        except:
            pass
        try:
            birthday = employee['birthday'].split("-")
            q_time = QDate()
            q_time.setDate(int(birthday[0]), int(birthday[1]), int(birthday[2]))
            self.ui.input_date_of_birth_2.setDate(q_time)
        except:
            pass
        try:
            self.ui.input_home_number_2.setText(employee['personal_phone'])
        except:
            pass
        try:
            self.ui.input_work_email.setText(employee['email'])
        except:
            pass
        try:
            self.ui.input_work_phone.setText(employee['work_phone'])
        except:
            pass
        try:
            self.ui.input_more_info.setPlainText(employee['more_info'])
        except:
            pass

    def save(self):
        from main import MainWindow

        full_name = self.ui.input_full_name_2.text()
        date_of_birth = self.ui.input_date_of_birth_2.text()
        more_info = self.ui.input_more_info.toPlainText()
        home_number = self.ui.input_home_number_2.text()
        work_number = self.ui.input_work_phone.text()
        work_email = self.ui.input_work_email.text()

        helper = self.ui.optional_helpers_2.currentText()
        helper_id = get_employee_id_by_name(helper)
        boss = self.ui.optional_boss.currentText()
        boss_id = get_employee_id_by_name(boss)
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

        url = f"http://127.0.0.1:8000/api/V1/employee/{self.employee['id']}"
        response = requests.put(url=url, json={
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

        print(response.json())

        self.close()

        


class AddEmployeeDialog(QDialog):
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

        self.ui = add_employee_dialog.Ui_Dialog()
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
        helper_id = get_employee_id_by_name(helper)
        boss = self.ui.optional_boss.currentText()
        boss_id = get_employee_id_by_name(boss)
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


    def setup_optional_fields(self):
        self.ui.optional_boss.addItems(self.employees)
        self.ui.optional_cabinets.addItems(self.cabinets)
        self.ui.optional_boss.addItems(self.employees)
        self.ui.optional_job_titles.addItems(self.job_titles)
        self.ui.optional_helpers.addItems(self.employees)
        self.ui.optional_organizations.addItems(self.organizations)
        self.ui.optional_sub_divisions.addItems(self.sub_divisions)
        self.ui.optional_department.addItems(self.sub_sub_divisions)