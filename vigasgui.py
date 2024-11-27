# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vigasfFBPko.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(613, 689)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setBold(True)
        self.label_4.setFont(font)

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 2)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet(u"")
        self.label_12.setPixmap(QPixmap(u"logofcsoft-1-256x256.png"))
        self.label_12.setScaledContents(False)
        self.label_12.setOpenExternalLinks(False)

        self.gridLayout_3.addWidget(self.label_12, 0, 4, 2, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(80, 16777215))
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.AceroBox = QComboBox(self.centralwidget)
        self.AceroBox.addItem("")
        self.AceroBox.addItem("")
        self.AceroBox.setObjectName(u"AceroBox")

        self.gridLayout.addWidget(self.AceroBox, 1, 1, 1, 1)

        self.HormBox = QComboBox(self.centralwidget)
        self.HormBox.addItem("")
        self.HormBox.addItem("")
        self.HormBox.addItem("")
        self.HormBox.addItem("")
        self.HormBox.addItem("")
        self.HormBox.setObjectName(u"HormBox")

        self.gridLayout.addWidget(self.HormBox, 0, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.tipo = QComboBox(self.centralwidget)
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.setObjectName(u"tipo")

        self.gridLayout.addWidget(self.tipo, 2, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_3.addWidget(self.label_11, 3, 2, 1, 1)

        self.calcular = QPushButton(self.centralwidget)
        self.calcular.setObjectName(u"calcular")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.calcular.setFont(font1)

        self.gridLayout_3.addWidget(self.calcular, 3, 4, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(150, 16777215))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.L = QLineEdit(self.widget)
        self.L.setObjectName(u"L")
        self.L.setMinimumSize(QSize(0, 20))
        self.L.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.L, 0, 1, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.H = QLineEdit(self.widget)
        self.H.setObjectName(u"H")
        self.H.setMinimumSize(QSize(0, 20))
        self.H.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.H, 1, 1, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.B = QLineEdit(self.widget)
        self.B.setObjectName(u"B")
        self.B.setMinimumSize(QSize(0, 20))
        self.B.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.B, 2, 1, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)

        self.rec = QLineEdit(self.widget)
        self.rec.setObjectName(u"rec")
        self.rec.setMinimumSize(QSize(0, 20))
        self.rec.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.rec, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 4, 0, 1, 2)

        self.TablaCargas = QTableWidget(self.centralwidget)
        if (self.TablaCargas.columnCount() < 1):
            self.TablaCargas.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.TablaCargas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.TablaCargas.rowCount() < 4):
            self.TablaCargas.setRowCount(4)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TablaCargas.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TablaCargas.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TablaCargas.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TablaCargas.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TablaCargas.setItem(1, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TablaCargas.setItem(2, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TablaCargas.setItem(3, 0, __qtablewidgetitem7)
        self.TablaCargas.setObjectName(u"TablaCargas")
        self.TablaCargas.setMaximumSize(QSize(250, 16777215))
        self.TablaCargas.setFont(font)
        self.TablaCargas.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.TablaCargas.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.TablaCargas.setAutoScroll(True)

        self.gridLayout_3.addWidget(self.TablaCargas, 4, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 4, 4, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_3.addWidget(self.label_8, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 5, 2, 1, 1)

        self.resultados = QTableWidget(self.centralwidget)
        if (self.resultados.columnCount() < 3):
            self.resultados.setColumnCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.resultados.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.resultados.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.resultados.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        if (self.resultados.rowCount() < 5):
            self.resultados.setRowCount(5)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.resultados.setVerticalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.resultados.setVerticalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.resultados.setVerticalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.resultados.setVerticalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.resultados.setVerticalHeaderItem(4, __qtablewidgetitem15)
        self.resultados.setObjectName(u"resultados")
        self.resultados.horizontalHeader().setDefaultSectionSize(150)

        self.gridLayout_3.addWidget(self.resultados, 6, 0, 1, 5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.HormBox, self.AceroBox)
        QWidget.setTabOrder(self.AceroBox, self.tipo)
        QWidget.setTabOrder(self.tipo, self.TablaCargas)
        QWidget.setTabOrder(self.TablaCargas, self.resultados)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Programa para Calculo de Vigas - Felipe Cordero O.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Par\u00e1metros B\u00e1sicos de Dise\u00f1o", None))
        self.label_12.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hormig\u00f3n", None))
        self.AceroBox.setItemText(0, QCoreApplication.translate("MainWindow", u"A6342H", None))
        self.AceroBox.setItemText(1, QCoreApplication.translate("MainWindow", u"A4428H", None))

        self.HormBox.setItemText(0, QCoreApplication.translate("MainWindow", u"H20", None))
        self.HormBox.setItemText(1, QCoreApplication.translate("MainWindow", u"H25", None))
        self.HormBox.setItemText(2, QCoreApplication.translate("MainWindow", u"H30", None))
        self.HormBox.setItemText(3, QCoreApplication.translate("MainWindow", u"H35", None))
        self.HormBox.setItemText(4, QCoreApplication.translate("MainWindow", u"H40", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tipo de viga", None))
        self.tipo.setItemText(0, QCoreApplication.translate("MainWindow", u"Apoyado-Apoyado", None))
        self.tipo.setItemText(1, QCoreApplication.translate("MainWindow", u"Apoyado-Empotrado", None))
        self.tipo.setItemText(2, QCoreApplication.translate("MainWindow", u"Empotrado-Empotrado", None))
        self.tipo.setItemText(3, QCoreApplication.translate("MainWindow", u"Voladizo (x 1.3 incluido)", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Acero", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Dimensiones:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Definici\u00f3n de Cargas:", None))
        self.calcular.setText(QCoreApplication.translate("MainWindow", u"Calcular!", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Largo [m] =", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"H [cm]=", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"B [cm]=", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"rec [cm]=", None))
        ___qtablewidgetitem = self.TablaCargas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Cargas", None));
        ___qtablewidgetitem1 = self.TablaCargas.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Ancho Tributario [m]", None));
        ___qtablewidgetitem2 = self.TablaCargas.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Espesor Losa [cm]", None));
        ___qtablewidgetitem3 = self.TablaCargas.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"CM [kg/m2]", None));
        ___qtablewidgetitem4 = self.TablaCargas.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"SC [kg/m2]", None));

        __sortingEnabled = self.TablaCargas.isSortingEnabled()
        self.TablaCargas.setSortingEnabled(False)
        self.TablaCargas.setSortingEnabled(__sortingEnabled)

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Resultados:", None))
        ___qtablewidgetitem5 = self.resultados.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Izquierda", None));
        ___qtablewidgetitem6 = self.resultados.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Centro", None));
        ___qtablewidgetitem7 = self.resultados.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Derecha", None));
        ___qtablewidgetitem8 = self.resultados.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Momento [ton-m]", None));
        ___qtablewidgetitem9 = self.resultados.verticalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u" \u03c1 / \u03c1b [%]", None));
        ___qtablewidgetitem10 = self.resultados.verticalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Corte [ton]", None));
        ___qtablewidgetitem11 = self.resultados.verticalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Def. LP [cm]", None));
        ___qtablewidgetitem12 = self.resultados.verticalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Def Inst. [cm]", None));
    # retranslateUi

