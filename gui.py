from PyQt5.QtWidgets import *


class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        # label
        lblName = QLabel("gene Project")
        # message

        # input
        editBox = QLineEdit()
        # button
        btnOK = QPushButton("OK")
        # checkbox
        btnCheck = QCheckBox("checkbox")
        # list
        listwidget = QListWidget()
        for i in range(10):
            item = QListWidgetItem("Item %i" % i)
            listwidget.addItem(item)

        # create layout
        layout = QVBoxLayout()
        layout.addWidget(lblName)
        layout.addWidget(editBox)
        layout.addWidget(btnOK)
        layout.addWidget(btnCheck)
        layout.addWidget(listwidget)

        # apply layout
        self.setLayout(layout)


app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()
