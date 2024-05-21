import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from compression_app import TextCompressionApp

app = QApplication(sys.argv)
my_style = """
    * {
        font-family: 'Verdana';
        font-size: 16px;
        padding:5px;
    }
    QTextEdit {
        border: 1px solid #000000;
        color: #eb8e15;
        font-weight: bold;
    }
    QLabel {
    }
    """
with open(r"stylesheets/style_black.css") as style:
    my_style += style.read()

app.setStyleSheet(my_style)
app.setWindowIcon(QIcon(r"media/zip2.png"))
ex = TextCompressionApp()
ex.show()
sys.exit(app.exec_())


