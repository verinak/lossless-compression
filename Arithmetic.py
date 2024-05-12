from collections import Counter
import math

class ArithmeticEncoding:
    """
    ArithmeticEncoding is a class for building arithmetic encoding.
    """

# This function calculates the single value representing the entire message after encoding
def get_encoded_value(encoder):
    """
    After encoding the entire message, this method returns the single value that represents the entire message.
    """
    # Extracting values from the last stage of encoding
    last_stage = list(encoder[-1].values())
    last_stage_values = []
    # Iterating through the sublist of the last stage
    for sublist in last_stage:
        # Extracting elements from the sublist
        for element in sublist:
            last_stage_values.append(element)

    # Calculating the minimum and maximum values from the last stage
    last_stage_min = min(last_stage_values)
    last_stage_max = max(last_stage_values)

    # Computing the encoded value representing the entire message
    return (last_stage_min + last_stage_max) / 2
    

# This function processes a stage in the encoding process
def process_stage(probability_table, stage_min, stage_max):
    """
    Processing a stage in the encoding process.
    """
    # Dictionary to store probabilities for each term in the stage
    stage_probs = {}
    # Calculating the domain of the stage
    stage_domain = stage_max - stage_min
    # Iterating through the probability table
    for term_idx in range(len(probability_table.items())):
        # Extracting the term and its probability
        term = list(probability_table.keys())[term_idx]
        term_prob = probability_table[term]
        # Calculating cumulative probability for each term
        cum_prob = term_prob * stage_domain + stage_min
        stage_probs[term] = [stage_min, cum_prob]
        stage_min = cum_prob
    return stage_probs

# This function encodes a message
def encode(msg, probability_table):
    """
    Encodes a message.
    """
    # Initializing an empty list to store encoder stages
    encoder = []

    # Initializing the minimum and maximum values for the first stage
    stage_min = 0
    stage_max = 1

    # Iterating over each term in the message
    for msg_term_idx in range(len(msg)):
        # Processing the current stage and obtaining probabilities
        stage_probs = process_stage(probability_table, stage_min, stage_max)

        # Extracting the current term from the message
        msg_term = msg[msg_term_idx]
        
        # Updating the stage's minimum and maximum values based on the probabilities of the current term
        stage_min = stage_probs[msg_term][0]
        stage_max = stage_probs[msg_term][1]

        # Storing the probabilities for the current stage
        encoder.append(stage_probs)

    # Processing the final stage after encoding all terms
    stage_probs = process_stage(probability_table, stage_min, stage_max)
    encoder.append(stage_probs)

    # Computing the single value representation of the entire encoded message
    encoded_msg = get_encoded_value(encoder)

    # Returning the encoder (list of stages) and the encoded message
    return encoder, encoded_msg

def calculate_probabilities(string):
    # Count the frequency of each character in the string
    frequency = Counter(string)
    
    # Calculate the total number of characters in the string
    total_characters = len(string)
    
    # Calculate the probability of occurrence for each character
    probabilities = {char: count / total_characters for char, count in frequency.items()}
    
    return probabilities

def calculate_entropy(string):
  """Calculates the entropy of a string.

  Args:
      string: The string to calculate the entropy for.

  Returns:
      The entropy of the string.
  """

  # Calculate the probabilities of occurrence for each character
  probabilities = calculate_probabilities(msg)

  # Calculate the entropy
  entropy = 0
  for probability in probabilities.values():
    if probability > 0:  # Avoid log(0) errors
      entropy -= probability * math.log2(probability)

  return entropy

def calculate_bits_before(string):
    # Count the number of characters in the string
    num_characters = len(string)
    
    # Check if the string consists only of zeros and ones
    if all(char in '01' for char in string):
        # If yes, each character represents a single bit
        num_bits = num_characters
    else:
        # If the string contains other characters, each character is represented using 8 bits (1 byte)
        num_bits = num_characters * 8
    return num_bits


# Example usage

# Get user input for the message to encode
msg = input("Enter your message to encode here: ")
probabilities = calculate_probabilities(msg)

# Encode the message
encoder, encoded_msg = encode(msg, probabilities)
entropy = calculate_entropy(msg)
bits_before = calculate_bits_before(msg)

print("Probabilities of occurrence for each character:", probabilities)
print("Encoder:", encoder)
print("Original Message:", msg)
print("Encoded message:", encoded_msg)
print("Entropy of the string:", entropy)
print("No of bits before:", bits_before)
