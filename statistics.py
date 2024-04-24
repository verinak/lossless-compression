import math

def calculate_entropy(message):
    # Calculate the frequency of each character
    frequencies = {}
    for char in message:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    
    # Calculate the entropy
    entropy = 0
    message_length = len(message)
    for frequency in frequencies.values():
        probability = frequency / message_length
        entropy -= probability * math.log2(probability)
    
    return entropy
