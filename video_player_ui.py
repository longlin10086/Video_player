# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_player.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, ClickableSlider, ComboBox, SpinBox)
from qmaterialwidgets import (FilledPushButton, ImageLabel, RadioButton)
from superqt import QLabeledRangeSlider

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(696, 753)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 656, 681))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.Load = FilledPushButton(self.layoutWidget)
        self.Load.setObjectName(u"Load")
        self.Load.setMaximumSize(QSize(200, 40))

        self.verticalLayout.addWidget(self.Load)

        self.Start = FilledPushButton(self.layoutWidget)
        self.Start.setObjectName(u"Start")
        self.Start.setMaximumSize(QSize(200, 40))

        self.verticalLayout.addWidget(self.Start)

        self.Stop = FilledPushButton(self.layoutWidget)
        self.Stop.setObjectName(u"Stop")
        self.Stop.setMaximumSize(QSize(200, 40))

        self.verticalLayout.addWidget(self.Stop)

        self.Conf = FilledPushButton(self.layoutWidget)
        self.Conf.setObjectName(u"Conf")
        self.Conf.setMaximumSize(QSize(200, 40))

        self.verticalLayout.addWidget(self.Conf)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_5)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.video_player = ImageLabel(self.layoutWidget)
        self.video_player.setObjectName(u"video_player")
        sizePolicy.setHeightForWidth(self.video_player.sizePolicy().hasHeightForWidth())
        self.video_player.setSizePolicy(sizePolicy)
        self.video_player.setPixmap(QPixmap(u"./img/OIP.jpg"))

        self.horizontalLayout_8.addWidget(self.video_player)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout_12.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.current = BodyLabel(self.layoutWidget)
        self.current.setObjectName(u"current")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.current.sizePolicy().hasHeightForWidth())
        self.current.setSizePolicy(sizePolicy1)
        self.current.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_7.addWidget(self.current)

        self.total = BodyLabel(self.layoutWidget)
        self.total.setObjectName(u"total")
        sizePolicy1.setHeightForWidth(self.total.sizePolicy().hasHeightForWidth())
        self.total.setSizePolicy(sizePolicy1)
        self.total.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_7.addWidget(self.total)

        self.Pause = FilledPushButton(self.layoutWidget)
        self.Pause.setObjectName(u"Pause")
        self.Pause.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_7.addWidget(self.Pause)

        self.Screenshot = FilledPushButton(self.layoutWidget)
        self.Screenshot.setObjectName(u"Screenshot")
        self.Screenshot.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_7.addWidget(self.Screenshot)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)


        self.horizontalLayout.addLayout(self.verticalLayout_12)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)

        self.comboBox = ComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_9.addWidget(self.comboBox)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Action_1 = RadioButton(self.layoutWidget)
        self.Action_1.setObjectName(u"Action_1")

        self.verticalLayout_5.addWidget(self.Action_1)

        self.Action_2 = RadioButton(self.layoutWidget)
        self.Action_2.setObjectName(u"Action_2")

        self.verticalLayout_5.addWidget(self.Action_2)

        self.Action_3 = RadioButton(self.layoutWidget)
        self.Action_3.setObjectName(u"Action_3")

        self.verticalLayout_5.addWidget(self.Action_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Action_4 = RadioButton(self.layoutWidget)
        self.Action_4.setObjectName(u"Action_4")

        self.verticalLayout_6.addWidget(self.Action_4)

        self.Action_5 = RadioButton(self.layoutWidget)
        self.Action_5.setObjectName(u"Action_5")

        self.verticalLayout_6.addWidget(self.Action_5)

        self.Action_6 = RadioButton(self.layoutWidget)
        self.Action_6.setObjectName(u"Action_6")

        self.verticalLayout_6.addWidget(self.Action_6)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Action_7 = RadioButton(self.layoutWidget)
        self.Action_7.setObjectName(u"Action_7")

        self.verticalLayout_7.addWidget(self.Action_7)

        self.Action_8 = RadioButton(self.layoutWidget)
        self.Action_8.setObjectName(u"Action_8")

        self.verticalLayout_7.addWidget(self.Action_8)

        self.Action_9 = RadioButton(self.layoutWidget)
        self.Action_9.setObjectName(u"Action_9")

        self.verticalLayout_7.addWidget(self.Action_9)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Write = FilledPushButton(self.layoutWidget)
        self.Write.setObjectName(u"Write")
        self.Write.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_4.addWidget(self.Write)

        self.Save = FilledPushButton(self.layoutWidget)
        self.Save.setObjectName(u"Save")
        self.Save.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_4.addWidget(self.Save)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Frames = BodyLabel(self.layoutWidget)
        self.Frames.setObjectName(u"Frames")
        self.Frames.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.Frames)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.min_frame = SpinBox(self.layoutWidget)
        self.min_frame.setObjectName(u"min_frame")
        self.min_frame.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.min_frame)

        self.label = BodyLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label)


        self.horizontalLayout_3.addLayout(self.verticalLayout_13)

        self.frames_slider = QLabeledRangeSlider(self.layoutWidget)
        self.frames_slider.setObjectName(u"frames_slider")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frames_slider.sizePolicy().hasHeightForWidth())
        self.frames_slider.setSizePolicy(sizePolicy2)
        self.frames_slider.setMaximumSize(QSize(16777215, 40))
        self.frames_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.frames_slider)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.max_frame = SpinBox(self.layoutWidget)
        self.max_frame.setObjectName(u"max_frame")
        self.max_frame.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.max_frame)

        self.label_2 = BodyLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_14)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Frame = BodyLabel(self.layoutWidget)
        self.Frame.setObjectName(u"Frame")
        self.Frame.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.Frame)

        self.frame_slider = ClickableSlider(self.layoutWidget)
        self.frame_slider.setObjectName(u"frame_slider")
        self.frame_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.frame_slider)

        self.frame_edit = SpinBox(self.layoutWidget)
        self.frame_edit.setObjectName(u"frame_edit")

        self.horizontalLayout_2.addWidget(self.frame_edit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.centralwidget.setLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 696, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.Start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.Conf.setText(QCoreApplication.translate("MainWindow", u"Conf", None))
        self.video_player.setText("")
        self.current.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.total.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Pause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.Screenshot.setText(QCoreApplication.translate("MainWindow", u"Screenshot", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Viewmode", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Left person", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Right person", None))

        self.Action_1.setText(QCoreApplication.translate("MainWindow", u"Action 1", None))
        self.Action_2.setText(QCoreApplication.translate("MainWindow", u"Action 2", None))
        self.Action_3.setText(QCoreApplication.translate("MainWindow", u"Action 3", None))
        self.Action_4.setText(QCoreApplication.translate("MainWindow", u"Action 4", None))
        self.Action_5.setText(QCoreApplication.translate("MainWindow", u"Action 5", None))
        self.Action_6.setText(QCoreApplication.translate("MainWindow", u"Action 6", None))
        self.Action_7.setText(QCoreApplication.translate("MainWindow", u"Action 7", None))
        self.Action_8.setText(QCoreApplication.translate("MainWindow", u"Action 8", None))
        self.Action_9.setText(QCoreApplication.translate("MainWindow", u"Action 9", None))
        self.Write.setText(QCoreApplication.translate("MainWindow", u"Write", None))
        self.Save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.Frames.setText(QCoreApplication.translate("MainWindow", u"Frames edit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Start frame", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"End frame", None))
        self.Frame.setText(QCoreApplication.translate("MainWindow", u"Frame edit", None))
    # retranslateUi

