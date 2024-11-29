# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vigasKdgofD.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1124, 560)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 50))
        self.label_12.setPixmap(QPixmap(u"logofcsoft-1-256x256.png"))
        self.label_12.setScaledContents(False)
        self.label_12.setOpenExternalLinks(True)

        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.HormBox = QComboBox(self.frame_4)
        self.HormBox.addItem("")
        self.HormBox.addItem("")
        self.HormBox.addItem("")
        self.HormBox.addItem("")
        self.HormBox.addItem("")
        self.HormBox.addItem("")
        self.HormBox.addItem("")
        self.HormBox.setObjectName(u"HormBox")
        self.HormBox.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_5.addWidget(self.HormBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)

        self.AceroBox = QComboBox(self.frame_4)
        self.AceroBox.addItem("")
        self.AceroBox.addItem("")
        self.AceroBox.setObjectName(u"AceroBox")
        self.AceroBox.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_5.addWidget(self.AceroBox, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)

        self.tipo = QComboBox(self.frame_4)
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.addItem("")
        self.tipo.setObjectName(u"tipo")
        self.tipo.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_5.addWidget(self.tipo, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 2, 0, 1, 1)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.TablaCargas = QTableWidget(self.frame_6)
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
        self.TablaCargas.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TablaCargas.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TablaCargas.setItem(2, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.TablaCargas.setItem(3, 0, __qtablewidgetitem8)
        self.TablaCargas.setObjectName(u"TablaCargas")
        self.TablaCargas.setFont(font)
        self.TablaCargas.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.TablaCargas.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.TablaCargas.horizontalHeader().setMinimumSectionSize(50)
        self.TablaCargas.horizontalHeader().setDefaultSectionSize(150)
        self.TablaCargas.verticalHeader().setDefaultSectionSize(36)
        self.TablaCargas.verticalHeader().setStretchLastSection(False)

        self.gridLayout_7.addWidget(self.TablaCargas, 1, 0, 1, 1)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setFont(font)

        self.gridLayout_7.addWidget(self.label_11, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_6, 2, 2, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setFont(font)

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.L = QLineEdit(self.frame_3)
        self.L.setObjectName(u"L")
        self.L.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.L, 0, 1, 1, 1)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setFont(font)

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.H = QLineEdit(self.frame_3)
        self.H.setObjectName(u"H")
        self.H.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.H, 1, 1, 1, 1)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setFont(font)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.B = QLineEdit(self.frame_3)
        self.B.setObjectName(u"B")
        self.B.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.B, 2, 1, 1, 1)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setFont(font)

        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)

        self.rec = QLineEdit(self.frame_3)
        self.rec.setObjectName(u"rec")
        self.rec.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.rec, 3, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 2, 1, 1, 1)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.resultados = QTableWidget(self.frame_5)
        if (self.resultados.columnCount() < 3):
            self.resultados.setColumnCount(3)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.resultados.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.resultados.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.resultados.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        if (self.resultados.rowCount() < 5):
            self.resultados.setRowCount(5)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.resultados.setVerticalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.resultados.setVerticalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.resultados.setVerticalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.resultados.setVerticalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.resultados.setVerticalHeaderItem(4, __qtablewidgetitem16)
        self.resultados.setObjectName(u"resultados")
        self.resultados.horizontalHeader().setDefaultSectionSize(320)
        self.resultados.horizontalHeader().setStretchLastSection(True)
        self.resultados.verticalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.resultados, 1, 0, 1, 1)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_5, 5, 0, 1, 3)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setOpenExternalLinks(True)

        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)

        self.calcular = QPushButton(self.centralwidget)
        self.calcular.setObjectName(u"calcular")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.calcular.setFont(font1)

        self.gridLayout_3.addWidget(self.calcular, 0, 1, 2, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.HormBox.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Programa para Calculo de Vigas - Felipe Cordero O.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hormig\u00f3n", None))
        self.HormBox.setItemText(0, QCoreApplication.translate("MainWindow", u"20 MPa", None))
        self.HormBox.setItemText(1, QCoreApplication.translate("MainWindow", u"25 MPa", None))
        self.HormBox.setItemText(2, QCoreApplication.translate("MainWindow", u"30 MPa", None))
        self.HormBox.setItemText(3, QCoreApplication.translate("MainWindow", u"35 MPa", None))
        self.HormBox.setItemText(4, QCoreApplication.translate("MainWindow", u"40 MPa", None))
        self.HormBox.setItemText(5, QCoreApplication.translate("MainWindow", u"45 MPa", None))
        self.HormBox.setItemText(6, QCoreApplication.translate("MainWindow", u"50 MPa", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Acero", None))
        self.AceroBox.setItemText(0, QCoreApplication.translate("MainWindow", u"420 MPa", None))
        self.AceroBox.setItemText(1, QCoreApplication.translate("MainWindow", u"280 MPa", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tipo de viga", None))
        self.tipo.setItemText(0, QCoreApplication.translate("MainWindow", u"Pined-Pined", None))
        self.tipo.setItemText(1, QCoreApplication.translate("MainWindow", u"Pined-Fixed", None))
        self.tipo.setItemText(2, QCoreApplication.translate("MainWindow", u"Fixed-Fixed", None))
        self.tipo.setItemText(3, QCoreApplication.translate("MainWindow", u"Cantilever (x 1.3 included)", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Par\u00e1metros B\u00e1sicos de Dise\u00f1o", None))
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
        ___qtablewidgetitem5 = self.TablaCargas.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem6 = self.TablaCargas.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem7 = self.TablaCargas.item(2, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"100", None));
        ___qtablewidgetitem8 = self.TablaCargas.item(3, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"200", None));
        self.TablaCargas.setSortingEnabled(__sortingEnabled)

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Definici\u00f3n de Cargas:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Dimensiones:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Largo [m] =", None))
        self.L.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"H [cm]=", None))
        self.H.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"B [cm]=", None))
        self.B.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"rec [cm]=", None))
        self.rec.setText(QCoreApplication.translate("MainWindow", u"5", None))
        ___qtablewidgetitem9 = self.resultados.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Izquierda", None));
        ___qtablewidgetitem10 = self.resultados.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Centro", None));
        ___qtablewidgetitem11 = self.resultados.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Derecha", None));
        ___qtablewidgetitem12 = self.resultados.verticalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Momento [ton-m]", None));
        ___qtablewidgetitem13 = self.resultados.verticalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u" \u03c1 / \u03c1b [%]", None));
        ___qtablewidgetitem14 = self.resultados.verticalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Corte [ton]", None));
        ___qtablewidgetitem15 = self.resultados.verticalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Def. LP [cm]", None));
        ___qtablewidgetitem16 = self.resultados.verticalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Def Inst. [cm]", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Resultados:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://felipecordero.com\"><span style=\" font-size:12pt; font-weight:700; text-decoration: underline; color:#0000ff;\">felipecordero.com</span></a></p></body></html>", None))
        self.calcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
    # retranslateUi

