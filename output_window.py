from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea, QWidget
import math

class CompressionResultsDialog(QDialog):
    def __init__(self, parent=None, input_text=''):
        super().__init__(parent)
        self.setWindowTitle('Compression Results')
        self.resize(900, 800)  

        # Scroll area setup
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        content_widget = QWidget()
        scroll.setWidget(content_widget)
        layout = QVBoxLayout(content_widget)

        # Initialize variables for best compression technique
        best_technique = ''
        best_compression_ratio = 0.0


         # Determine the appropriate compression techniques based on the input text
        techniques = []
        if all(char in {'0', '1'} for char in input_text):
            techniques.append(('Run Length Encoding', self.run_length_encoding))
            techniques.append(('Golomb Encoding', self.golomb_encoding))
        elif input_text.isdigit():
            techniques.append(('Golomb Encoding', self.golomb_encoding))
        else:
            techniques.append(('Huffman Encoding', self.huffman_encoding))
            techniques.append(('Arithmetic Encoding', self.arithmetic_encoding))
            techniques.append(('LZW Encoding', self.lzw_encoding))
            techniques.append(('Run Length Encoding', self.run_length_encoding))

        for name, func in techniques:
            compression_ratio, bits_after, encoded_message, efficiency, avg_len = func(input_text)
            if name == "Golomb Encoding":
                if all(c in '01' for c in input_text):   
                    results_text = (
                    f"<b><span style='font-size:14pt;'>{name}</span></b><br><br>"
                    f"Compression Ratio  {compression_ratio:.2f}<br>"
                    f"Bits After Encoding  {bits_after} bits<br>"
                    f"Encoded Message  {encoded_message}<br>"
                    f"Efficiency  {efficiency:.2f}%<br>"
                    f"Average Length  {avg_len} bits<br>"
                )
                else:
                    results_text = (
                        f"<b><span style='font-size:14pt;'>{name}</span></b><br><br>"
                        f"Compression Ratio  {compression_ratio:.2f}<br>"
                        f"Bits After Encoding  {bits_after} bits<br>"
                        f"Encoded Message  {encoded_message}<br>"
                        f"Average Length  {avg_len} bits<br>"
                        )
            else:
                results_text = (
                f"<b><span style='font-size:14pt;'>{name}</span></b><br><br>"  # Applying HTML to make name bold and larger
                f"Compression Ratio    {compression_ratio:.2f}<br>"
                f"Bits After Encoding    {bits_after} bits<br>"
                f"Encoded Message    {encoded_message}<br>"
                f"Efficiency  {efficiency:.2f}%<br>"
                f"Average Length  {avg_len} bits<br>"
    
                )
            label = QLabel(results_text)
            label.setWordWrap(True)
            layout.addWidget(label)

            # Check if the current compression ratio is the best 
            if compression_ratio > best_compression_ratio:
                best_technique = name
                best_compression_ratio = compression_ratio

        # Print the name of the best compression technique and its compression ratio
        if best_technique:
            best = (
                f"<span style='font-size:16pt;'>Final Result</span><br><br>"
                f"<span style='font-size:14pt;'>Best Compression Technique: {best_technique}</span><br>"
                f"<span style='font-size:14pt;'>Compression Ratio: {best_compression_ratio:.2f}</span>")
            best_label = QLabel(best)
            best_label.setWordWrap(True)
            layout.addWidget(best_label)

        # Set the dialog layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)



    def run_length_encoding(self, input_text):
        from run_length import run_length_encoding
        results = run_length_encoding(input_text)
        encoded_message = ', '.join([f'{pair[0]}({pair[1]})' for pair in results['result']])
        compression_ratio = results['cr']
        bits_after = results['bits_after']
        efficiency = results['efficiency']
        avg_len = results['avg_len']

        return compression_ratio, bits_after, encoded_message, efficiency, avg_len



    def huffman_encoding(self, input_text):
        from huffman import compression_with_huffman
        results = compression_with_huffman(input_text)
        encoded_message = results["result"]
        #prob_table = results["prob_dict"]
        avg_len = results["avg_len"]
        #entropy = results["entropy"]
        efficiency = results["efficiency"] 
        #before_bits = results["bits_before"]
        bits_after = results["bits_after"]
        compression_ratio = results["cr"]

        return compression_ratio, bits_after, encoded_message, efficiency, avg_len



    def arithmetic_encoding(self, input_text):
        from Arithmetic import encode
        from Functions import calculate_probabilities
        probabilities = calculate_probabilities(input_text)
        results = encode(input_text, probabilities)
        compression_ratio = results['cr']
        bits_after = results['bits_after']
        encoded_message = results['result']
        efficiency = results['efficiency']
        avg_len = results['avg_len']

        return compression_ratio, bits_after, encoded_message, efficiency, avg_len



    def golomb_encoding(self, input_text):
        from golomb import golomb, calculate_golomb_and_stats

    # Checking if the input text is binary (consists of 0s and 1s only)
        if all(c in '01' for c in input_text):
            results = calculate_golomb_and_stats(input_text)
            return (results['cr'], results['bits_after'], results['result'], results['efficiency'], results['bits_after'])
        else:
            decimal_value = int(input_text)
            m = round(math.sqrt(decimal_value)) if decimal_value > 0 else 1

    
        result = golomb(decimal_value, m)
        encoded_message = result['result']
        bits_before = result['bits_before']
        bits_after = result['bits_after']
        compression_ratio = result['cr']
        avg_len = result['bits_after']
        
        return compression_ratio, bits_after, encoded_message, avg_len



    def lzw_encoding(self, input_text):
          from LZW import lzw_compress
          results = lzw_compress(input_text)
          compression_ratio = results['compression_ratio']
          bits_after = results['compressed_length']
          encoded_message = ', '.join(map(str, results['tag']))
          efficiency =  results['efficiency']
          avg_len = results["average_length"]
          return compression_ratio, bits_after, encoded_message, efficiency, avg_len

