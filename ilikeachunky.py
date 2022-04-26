from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget,QHBoxLayout,QPushButton

app = QApplication([])
window = QWidget()

window.setWindowTitle('Испытай удачу!')

window.resize(400,200)

k1=QPushButton('1')
k2=QPushButton('2')
k3=QPushButton('3')
k4=QPushButton('4')
k5=QPushButton('5')

layout_main = QVBoxLayout()

mainline1 = QHBoxLayout()
mainline2 = QHBoxLayout()
mainline3 = QHBoxLayout()

mainline1.addWidget(k1,alignment = Qt.AlignCenter)
mainline1.addWidget(k2,alignment = Qt.AlignCenter)
mainline2.addWidget(k3,alignment = Qt.AlignCenter)
mainline3.addWidget(k4,alignment = Qt.AlignCenter)
mainline3.addWidget(k5,alignment = Qt.AlignCenter)

layout_main.addLayout(mainline1)
layout_main.addLayout(mainline2)
layout_main.addLayout(mainline3)

window.setLayout(layout_main)

window.show()
app.exec_()


