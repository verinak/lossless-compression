import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QLabel, QLineEdit
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
        # Check if the dialog is already open
        if not self.statistics_dialog or not self.statistics_dialog.isVisible():
            self.statistics_dialog = StatisticsDialog(self, self.text_input.toPlainText())
            self.statistics_dialog.show()


    def show_compression_results(self):
        # Check if the dialog is already open
        if not self.compression_results_dialog or not self.compression_results_dialog.isVisible():
            self.compression_results_dialog = CompressionResultsDialog(self, self.text_input.toPlainText())
            self.compression_results_dialog.show()

