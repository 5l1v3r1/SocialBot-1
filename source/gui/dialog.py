# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(":horizontalLayout_2")

        #Add Bot Button
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setObjectName("add")

        self.horizontalLayout_2.addWidget(self.add)

        #Delete Bot Button
        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setObjectName("delete_2")

        self.horizontalLayout_2.addWidget(self.delete_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(250, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 382, 546))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")

        #Bot Liste
        self.botTabelle = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        self.botTabelle.setObjectName("botTabelle")
        item = QtWidgets.QListWidgetItem()
        self.botTabelle.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.botTabelle.addItem(item)

        self.gridLayout_2.addWidget(self.botTabelle, 0, 0, 1, 1)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_2)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.protokoll = QtWidgets.QTabWidget(self.centralwidget)
        self.protokoll.setObjectName("protokoll")
        self.browser = QtWidgets.QWidget()
        self.browser.setAccessibleName("")
        self.browser.setObjectName("browser")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.browser)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.browser)
        self.webView.setProperty("url", QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.gridLayout_3.addWidget(self.webView, 0, 0, 1, 1)
        self.protokoll.addTab(self.browser, "")
        self.verhalten = QtWidgets.QWidget()
        self.verhalten.setObjectName("verhalten")

        #Auswahl Tweeten oder Retweeten
        self.comboBox = QtWidgets.QComboBox(self.verhalten)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        #Text Edit für Tweet Nachricht
        self.nachricht = QtWidgets.QTextEdit(self.verhalten)
        self.nachricht.setGeometry(QtCore.QRect(10, 80, 351, 51))
        self.nachricht.setObjectName("nachricht")

        #Text Edit für Suchkriteria
        self.suchkriteria = QtWidgets.QTextEdit(self.verhalten)
        self.suchkriteria.setGeometry(QtCore.QRect(10, 170, 351, 51))
        self.suchkriteria.setObjectName("suchkriteria")

        self.label = QtWidgets.QLabel(self.verhalten)
        self.label.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.verhalten)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 151, 16))
        self.label_2.setObjectName("label_2")

        #Start Button für Verhalten
        self.startButton = QtWidgets.QPushButton(self.verhalten)
        self.startButton.setGeometry(QtCore.QRect(290, 240, 75, 23))
        self.startButton.setObjectName("startButton")

        self.protokoll.addTab(self.verhalten, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.protokoll_text = QtWidgets.QTextBrowser(self.tab_2)
        self.protokoll_text.setGeometry(QtCore.QRect(20, 20, 331, 441))
        self.protokoll_text.setObjectName("protokoll_text")

        #Button für Protokoll anzeigenhttps://pypi.org/
        self.showProtokoll = QtWidgets.QPushButton(self.tab_2)
        self.showProtokoll.setGeometry(QtCore.QRect(280, 480, 75, 31))
        self.showProtokoll.setObjectName("showProtokoll")

        self.protokoll.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.protokoll, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.protokoll.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Socialbot"))

        #Add Bot Button
        self.add.setText(_translate("MainWindow", "Add Bot"))

        #Delete Bot Button
        self.delete_2.setText(_translate("MainWindow", "Delete Bot"))

        #Bot Liste
        __sortingEnabled = self.botTabelle.isSortingEnabled()
        self.botTabelle.setSortingEnabled(False)
        item = self.botTabelle.item(0)
        item.setText(_translate("MainWindow", "1. Bot"))
        item = self.botTabelle.item(1)
        item.setText(_translate("MainWindow", "2. Bot"))
        self.botTabelle.setSortingEnabled(__sortingEnabled)

        self.protokoll.setTabText(self.protokoll.indexOf(self.browser), _translate("MainWindow", "Browser"))

        #Auswahl Box Tweeten oder Retweeten
        self.comboBox.setItemText(0, _translate("MainWindow", "Tweeten"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Retweeten"))

        self.label.setText(_translate("MainWindow", "Nachricht"))
        self.label_2.setText(_translate("MainWindow", "Suchkriteria (bei Rewtweeten)"))

        #Start Button für Bot Verhalten
        self.startButton.setText(_translate("MainWindow", "START"))
        QWidget.connect(self.startButton, clicked(), this, self.startAct())

        self.protokoll.setTabText(self.protokoll.indexOf(self.verhalten), _translate("MainWindow", "Verhalten"))

        #Button für Protokoll anzeigen
        self.showProtokoll.setText(_translate("MainWindow", "Protokoll"))

        self.protokoll.setTabText(self.protokoll.indexOf(self.tab_2), _translate("MainWindow", "Protokoll"))

    def startAct(self):
#        def setupUi(self, MainWindow):
        tweetVal = self.nachricht.toPlainText()
        print(tweetVal)
        searchVal = self.suchkriteria.toPlainText()
        print(searchVal)
        return True

from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
