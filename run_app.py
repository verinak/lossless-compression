import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from compression_app import TextCompressionApp

app = QApplication(sys.argv)
with open(r"stylesheets/aqua_dark.css") as style:
    my_style = style.read()

app.setStyleSheet(my_style)
app.setWindowIcon(QIcon(r"media/zip2.png"))
ex = TextCompressionApp()
ex.show()
sys.exit(app.exec_())


