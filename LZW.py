import Functions

def lzw_compress(text):
    # Initialize the dictionary with ASCII values from 0 to 127
    dictionary = {}
    for i in range(128):
        dictionary[chr(i)] = i

    compressed_text = []
    w = ""
    for char in text:
        wc = w + char
        if wc in dictionary:
            w = wc
        else:
            compressed_text.append(dictionary[w])
            dictionary[wc] = len(dictionary)
            w = char
    if w:
        compressed_text.append(dictionary[w])

    # # Print the dictionary
    # for key, value in dictionary.items():
    #     print(key, ":", value)

    # Calculate probabilities
    total_codes = len(compressed_text)
    probabilities = {code: compressed_text.count(code) / total_codes for code in compressed_text}

    entropy = Functions.calculate_entropy(text)

    length_before = Functions.calculate_bits_before(text)
    length_after = Functions.calculate_bits_for_list(compressed_text)
    cr = length_before / length_after

    # Calculate average length
    average_length = sum(len(format(code, 'b')) * probabilities[code] for code in set(compressed_text))
    
    efficiency = entropy / average_length

    results = {
        "entropy": entropy,
        "tag": compressed_text,
        "original_length": length_before,
        "compressed_length": length_after,
        "compression_ratio": cr,
        "average_length": average_length,
        "efficiency": efficiency
    }
    return results



#example
if __name__ == "__main__":
    user_input = "ABAABABBAABAABAAAABABBBBBBBB"
    results = lzw_compress(user_input)
    print("Results:", results)





