"""
   PyPSADiagGUI.py

   Copyright (C) 2024 - 2025 Marc Postema (mpostema09 -at- gmail.com)

   This program is free software; you can redistribute it and/or
   modify it under the terms of the GNU General Public License
   as published by the Free Software Foundation; either version 2
   of the License, or (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
   Or, point your browser to http://www.gnu.org/copyleft/gpl.html
"""

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

from EcuZoneTreeView  import EcuZoneTreeView

class PyPSADiagGUI(object):

    def setupGUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 700)
        MainWindow.setSizeIncrement(QSize(1, 1))
        MainWindow.setWindowTitle("PyPSADiag")
        self.centralwidget = QWidget(MainWindow)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)

        self.frame = QFrame(self.centralwidget)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.command = QLineEdit()
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        self.sendCommand = QPushButton()
        self.sendCommand.setText(QCoreApplication.translate("MainWindow", u"Send Command", None))
        self.openCSVFile = QPushButton()
        self.openCSVFile.setText(QCoreApplication.translate("MainWindow", u"Open CSV File", None))
        self.saveCSVFile = QPushButton()
        self.saveCSVFile.setText(QCoreApplication.translate("MainWindow", u"Write CSV File", None))

        self.portNameComboBox = QComboBox()
        self.ConnectPort = QPushButton()
        self.ConnectPort.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.DisconnectPort = QPushButton()
        self.DisconnectPort.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.openZoneFile = QPushButton()
        self.openZoneFile.setText(QCoreApplication.translate("MainWindow", u"Open Zone File", None))
        self.ecuComboBox = QComboBox()
        self.ecuKeyComboBox = QComboBox()
        self.readZone = QPushButton()
        self.readZone.setText(QCoreApplication.translate("MainWindow", u"Read", None))
        self.writeZone = QPushButton()
        self.writeZone.setText(QCoreApplication.translate("MainWindow", u"Write", None))
        self.rebootEcu = QPushButton()
        self.rebootEcu.setText(QCoreApplication.translate("MainWindow", u"Reboot ECU", None))
        self.readEcuFaults = QPushButton()
        self.readEcuFaults.setText(QCoreApplication.translate("MainWindow", u"Read ECU Faults", None))
        self.writeSecureTraceability = QCheckBox()
        self.writeSecureTraceability.setText(QCoreApplication.translate("MainWindow", u"Write Secure Traceability", None))
        self.useSketchSeedGenerator = QCheckBox()
        self.useSketchSeedGenerator.setText(QCoreApplication.translate("MainWindow", u"Use Sketch Seed Generator", None))
        self.treeView = EcuZoneTreeView(self.frame)

        # Setup Top Left Layout
        self.topLeftLayout = QVBoxLayout()
        self.topLeftLayout.addWidget(self.command)
        self.topLeftLayout.addWidget(self.output)

        # Setup Top Right Layout
        self.topRightLayout = QVBoxLayout()
        self.topRightLayout.addWidget(self.sendCommand)
        self.topRightLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.topRightLayout.addWidget(self.openCSVFile)
        self.topRightLayout.addWidget(self.saveCSVFile)
        self.topRightLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.topRightLayout.addWidget(self.portNameComboBox)
        self.topRightLayout.addWidget(self.ConnectPort)
        self.topRightLayout.addWidget(self.DisconnectPort)
        self.topRightLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Setup Bottom Left Layout
        self.bottomLeftLayout = QVBoxLayout()
        self.bottomLeftLayout.addWidget(self.treeView)

        # Setup Bottom Right Layout
        self.bottomRightLayout = QVBoxLayout()
        self.bottomRightLayout.addWidget(self.openZoneFile)
        self.bottomRightLayout.addWidget(self.ecuComboBox)
        self.bottomRightLayout.addWidget(self.ecuKeyComboBox)
        self.bottomRightLayout.addWidget(self.readZone)
        self.bottomRightLayout.addWidget(self.writeZone)
        self.bottomRightLayout.addWidget(self.readEcuFaults)
        self.bottomRightLayout.addWidget(self.rebootEcu)
        self.bottomRightLayout.addWidget(self.writeSecureTraceability)
        self.bottomRightLayout.addWidget(self.useSketchSeedGenerator)
        self.bottomRightLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Add Top Left, Right Layout -> Main Top Layout
        self.topLayout = QHBoxLayout()
        self.topLayout = QHBoxLayout()
        self.topLayout.addLayout(self.topLeftLayout)
        self.topLayout.addLayout(self.topRightLayout)

        # Add Bottom Left, Right Layout -> Main Bottom Layout
        self.bottomLayout = QHBoxLayout()
        self.bottomLayout = QHBoxLayout()
        self.bottomLayout.addLayout(self.bottomLeftLayout)
        self.bottomLayout.addLayout(self.bottomRightLayout)

        # Setup splitter
        self.splitter = QSplitter(self.frame)
        self.splitter.setOrientation(Qt.Orientation.Vertical)

        self.topWidget = QWidget()
        self.topWidget.setLayout(self.topLayout)
        self.splitter.addWidget(self.topWidget)

        self.bottomWidget = QWidget()
        self.bottomWidget.setLayout(self.bottomLayout)
        self.splitter.addWidget(self.bottomWidget)

        self.frameLayout = QHBoxLayout()
        self.frameLayout.addWidget(self.splitter)
        self.frame.setLayout(self.frameLayout)

        # Setup Main Frame
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.frame)
        self.centralwidget.setLayout(self.mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)
