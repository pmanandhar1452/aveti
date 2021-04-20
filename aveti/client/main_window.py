"""
main_window.py
Entry point for the client
"""

__author__     = "Prakash Manandhar"
__copyright__  = "Copyright 2021, Prakash Manandhar"
__credits__    = ["Prakash Manandhar"]
__license__    = "MIT"
__version__    = "1.0.0"
__maintainer__ = "Prakash Manandhar"
__email__      = "prakashm@alum.mit.edu"
__status__     = "Production"

import sys
from PySide6 import QtWidgets, QtGui
from qt_material import apply_stylesheet

class MainWindow(QtWidgets.QWidget):

    def _addTreeChildren(self, pNode):
        pNode.addChild(QtWidgets.QTreeWidgetItem(["Light"]))
        pNode.addChild(QtWidgets.QTreeWidgetItem(["Temperature"]))
        pNode.addChild(QtWidgets.QTreeWidgetItem(["Humidity"]))
        pNode.addChild(QtWidgets.QTreeWidgetItem(["Moisture"]))

    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_layout = QtWidgets.QVBoxLayout()
        self.button = QtWidgets.QPushButton("Test")
        self.main_layout.addWidget(self.button)
        
        l1 = QtWidgets.QTreeWidgetItem([ "Living Room Spider Plant"])
        l2 = QtWidgets.QTreeWidgetItem([ "Kitchen Orchid"])
    
        self._addTreeChildren(l1)
        self._addTreeChildren(l2)
        
        tw = QtWidgets.QTreeWidget(self)
        tw.setColumnCount(1)
        tw.setHeaderLabels(["My Plants"])
        tw.addTopLevelItem(l1)
        tw.addTopLevelItem(l2)
        self.main_layout.addWidget(tw)
        self.setLayout(self.main_layout)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    window = MainWindow()
    window.resize(1500, 740)
    window.show()
    sys.exit(app.exec_())
