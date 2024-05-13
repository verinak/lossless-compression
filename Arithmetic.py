import Functions as fn
from decimal import Decimal, getcontext

# Set the precision for Decimal
getcontext().prec = 120  # Set precision to a value that suits your needs

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
    return last_stage_min, last_stage_max, (last_stage_min + last_stage_max) / 2
    

# This function processes a stage in the encoding process
def process_stage(probability_table, stage_min, stage_max):
    """
    Processing a stage in the encoding process.
    """
    # Dictionary to store probabilities for each term in the stage
    stage_probs = {}
    # Calculating the range of the stage
    stage_domain = stage_max - stage_min
    # Iterating through the probability table
    for term_idx in range(len(probability_table.items())):
        # Extracting the term and its probability
        term = list(probability_table.keys())[term_idx]
        term_prob = probability_table[term]
        # Calculating cumulative probability for each term
        cum_prob = Decimal(term_prob) * Decimal(stage_domain) + Decimal(stage_min)
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
    last_stage_min, last_stage_max, encoded_msg = get_encoded_value(encoder)

    no_of_symbols = len(msg)
    entropy = fn.calculate_entropy(msg)
    bits_before= fn.calculate_bits_before(msg)
    bits_after = fn.calculate_bits_after (last_stage_min , last_stage_max)
    avg_len = fn.calculate_avg_length (entropy , no_of_symbols )
    

    output = {
        'result': "{:.16f}".format(encoded_msg),
        'bits_before': bits_before,
        'bits_after': bits_after,
        'cr': bits_before/bits_after,
        'entropy': entropy,
        'avg_len': avg_len,
        'efficiency': (entropy/avg_len)*100,
    }
    return  output

if __name__ == "__main__":
    
    # Example usage
    message = 'hanbame bame pin nunbushin bitcheoreom.. dalbiche banhae pin haiyan kkotcheoreom.. - oneus luna'
    probabilities = fn.calculate_probabilities(message)
    print(len(message))

    # Encode the message and get the output dictionary
    output = encode(message, probabilities)

    # Print the output dictionary
    print(output)


