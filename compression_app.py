import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QLabel, QLineEdit, QMessageBox
from statistics_window import StatisticsDialog
from output_window import CompressionResultsDialog

class TextCompressionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Text Compression App')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.text_input = QTextEdit(self)
        self.text_input.setPlaceholderText("Enter text here to compress...")
        layout.addWidget(self.text_input)


        self.stats_button = QPushButton('Calculate Statistics', self)
        self.stats_button.clicked.connect(self.show_statistics)
        layout.addWidget(self.stats_button)

        self.results_button = QPushButton('Show Compression Results', self)
        self.results_button.clicked.connect(self.show_compression_results)
        layout.addWidget(self.results_button)

        # Store dialog references
        self.statistics_dialog = None
        self.compression_results_dialog = None


    def show_statistics(self):
        # check for empty message
        if(not self.text_input.toPlainText().strip()):
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a message to compress.')
            return
        # Check if the dialog is already open
        if self.statistics_dialog and self.statistics_dialog.isVisible():
            self.statistics_dialog.close()
        # open dialog
        self.statistics_dialog = StatisticsDialog(self, self.text_input.toPlainText())
        self.statistics_dialog.show()


    def show_compression_results(self):
        # check for empty message
        if(not self.text_input.toPlainText().strip()):
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a message to compress.')
            return
        # Check if the dialog is already open
        if self.compression_results_dialog and self.compression_results_dialog.isVisible():
            self.compression_results_dialog.close()
        # open dialog
        self.compression_results_dialog = CompressionResultsDialog(self, self.text_input.toPlainText())
        self.compression_results_dialog.show()

