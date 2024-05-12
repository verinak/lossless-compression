from collections import Counter
import math
##Probability of occurence
def calculate_probabilities(string):
    # Count the frequency of each character in the string
    frequency = Counter(string)
    
    # Calculate the total number of characters in the string
    total_characters = len(string)
    
    # Calculate the probability of occurrence for each character
    probabilities = {char: count / total_characters for char, count in frequency.items()}
    
    return probabilities

if __name__ == "__main__":
  # Example usage
  input_string = "hello"
  probabilities = calculate_probabilities(input_string)
  print("Probabilities of occurrence for each character:", probabilities)


##Avg length
def calculate_average_length(symbol_dict, probabilities):
  """Calculates the average length of characters in a symbol dictionary,
  weighted by their probabilities.

  Args:
      symbol_dict: A dictionary where keys are symbols and values are code words.
      probabilities: A dictionary where keys are symbols and values are their probabilities.

  Returns:
      The average length of characters in the symbol dictionary, weighted by their probabilities.
  """

  total_length = 0
  total_probability = 0

  for symbol, code_word in symbol_dict.items():
    symbol_length = len(code_word)
    symbol_probability = probabilities.get(symbol, 0)  # Handle missing probabilities

    total_length += symbol_length * symbol_probability

  return total_length

if __name__ == "__main__":
  # Example usage
  symbol_dict = {'a': '1', 'b': '10', 'c': '111'}
  string = "aabcaacbab"  # Example string for probability calculation
  probabilities = calculate_probabilities(string)
  average_length = calculate_average_length(symbol_dict, probabilities)
  print("Average length of characters (weighted by probabilities):", average_length)


##Entropy
def calculate_entropy(string):
  """Calculates the entropy of a string.

  Args:
      string: The string to calculate the entropy for.

  Returns:
      The entropy of the string.
  """

  # Calculate the probabilities of occurrence for each character
  probabilities = calculate_probabilities(string)

  # Calculate the entropy
  entropy = 0
  for probability in probabilities.values():
    if probability > 0:  # Avoid log(0) errors
      entropy -= probability * math.log2(probability)

  return entropy

if __name__ == "__main__":
  # Example usage
  input_string = "aabbcaacbab"
  entropy = calculate_entropy(input_string)
  print("Entropy of the string:", entropy)


## no. of bits Before
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


## no. of bits After
### bits After for LZW
def calculate_bits_for_list(numbers):
    # Find the maximum number in the list
    max_number = max(numbers)
    
    # Calculate the number of bits required to represent the maximum number
    num_bits_for_max_number = len(bin(max_number)) - 2  # Subtract 2 to exclude '0b' prefix
    
    # Calculate the total number of bits required for the list
    total_bits = len(numbers) * num_bits_for_max_number
    
    return total_bits

if __name__ == "__main__":
  # Example usage
  numbers = [10, 20, 30, 40, 50]
  num_bits = calculate_bits_for_list(numbers)
  print("Number of bits After:", num_bits)


### bits After for RLE
def calculate_bits_for_array(array):
  num_keys = 0
  key_lengths = []
  value_bit_reqs = []

  for key_value_pair in array:
    key, value = key_value_pair  # Unpack key-value pair
    num_keys += 1

    key_lengths.append(len(str(key)))  # Store key length
    value_bit_reqs.append(len(bin(value)) - 2)  # Estimate value bit requirement

  num_bits_for_key = 1 if all(key in ('0', '1') for key, _ in array) else 8
  total_bits = num_keys * (num_bits_for_key + max(value_bit_reqs))

  return key_lengths, value_bit_reqs, total_bits

if __name__ == "__main__":
  # Example usage
  my_array = [['0', 6], ['1', 14], ['0', 13], ['1', 9]]
  key_lengths, value_bit_reqs, num_bits = calculate_bits_for_array(my_array)
  print("Number of bits After:", num_bits)

# for arithmetic
def calculate_bits_after (l , h):
    result = math.ceil(math.log2(1 / (h - l))) + 1
    return result
# for arithmetic
def calculate_avg_length (entropy , no_of_symbols ):
    avg_len = entropy + (2/ no_of_symbols)
    return avg_len
