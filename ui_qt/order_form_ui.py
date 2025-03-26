# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_add = QPushButton(Form)
        self.btn_add.setObjectName(u"btn_add")

        self.verticalLayout_2.addWidget(self.btn_add)

        self.btn_change_qty = QPushButton(Form)
        self.btn_change_qty.setObjectName(u"btn_change_qty")

        self.verticalLayout_2.addWidget(self.btn_change_qty)

        self.btn_cancel = QPushButton(Form)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.verticalLayout_2.addWidget(self.btn_cancel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_2, 3, 1, 1, 1)

        self.user_input = QLineEdit(Form)
        self.user_input.setObjectName(u"user_input")

        self.gridLayout.addWidget(self.user_input, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label_total = QLabel(Form)
        self.label_total.setObjectName(u"label_total")

        self.verticalLayout.addWidget(self.label_total)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0427\u0435\u043a", None))
        self.btn_add.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e \u041f\u041b\u0423", None))
        self.btn_change_qty.setText(QCoreApplication.translate("Form", u"\u0418\u0437\u043c.\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.btn_cancel.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_total.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

