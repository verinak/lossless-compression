from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHeaderView

from Functions import calculate_probabilities, calculate_entropy, calculate_bits_before

class StatisticsDialog(QDialog):
    def __init__(self, parent=None, input_text=''):
        super().__init__(parent)
        self.setWindowTitle('Text Statistics')
        layout = QVBoxLayout()

        # Create a table to display probabilities
        self.probabilities_table = QTableWidget()
        self.probabilities_table.setColumnCount(2)
        self.probabilities_table.setHorizontalHeaderLabels(['Character', 'Probability'])
        probabilities = calculate_probabilities(input_text)
        self.probabilities_table.setRowCount(len(probabilities))

        for index, (char, prob) in enumerate(probabilities.items()):
            self.probabilities_table.setItem(index, 0, QTableWidgetItem(char))
            self.probabilities_table.setItem(index, 1, QTableWidgetItem(f'{prob:.4f}'))
        
        self.probabilities_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.probabilities_table)

        # Calculating other statistics
        entropy = calculate_entropy(input_text)
        bits_before = calculate_bits_before(input_text)
        

        layout.addWidget(QLabel(f'Entropy: {entropy:.2f} bits'))
        layout.addWidget(QLabel(f'Number of bits before encoding: {bits_before} bits'))
        

        self.setLayout(layout)
