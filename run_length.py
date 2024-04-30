import Functions as fn

def run_length_encoding(message):

    encoded_message = []

    # start counting with the first charcter in the message
    letter = message[0] 
    count = 0
    # iterate over each character in the message
    for char in message:
        # if character is found at current index, count++
        if(char == letter):
            count = count + 1
        # else (different character found at current index)
        # append current letter and count to encoded message
        # then start counting the new character
        else:
            encoded_message.append([letter, count])
            letter = char
            count = 1
    # append letter and count of the last character to encoded message
    encoded_message.append([letter, count])

    # calculate statistics and return results
    bits_before = fn.calculate_bits_before(message)
    bits_after = fn.calculate_bits_for_array(encoded_message)[2]
    entropy = fn.calculate_entropy(message)
    avg_len = bits_after/len(message) # fi habal hena bs ba3den ba2a
    output = {
        'result': encoded_message,
        'bits_before': bits_before,
        'bits_after': bits_after,
        'cr': bits_before/bits_after,
        'entropy': entropy,
        'avg_len': avg_len,
        'efficiency': (entropy/avg_len)*100,
    }

    return output

if __name__ == "__main__":
    print(run_length_encoding('aaaabbccccccddd'))
    print(run_length_encoding('000000111111111111110000000000000111111111'))


