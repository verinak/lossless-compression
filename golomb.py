# Section 5
# Let's implement a simple Golomb-Rice encoding and decoding function in Python
# to demonstrate how it could be used, for example, in the context of compressing data like Bitcoin block filters.

def golomb_rice_encode(value, M):
    """
    Encodes a value using Golomb-Rice coding for a given parameter M.
    M must be a power of 2 for this implementation.
    
    :param value: The integer value to encode.
    :param M: The parameter M, which must be a power of 2.
    :return: The encoded binary string.
    """
    quotient = value // M
    remainder = value % M
    
    # Encode quotient in unary; a sequence of 1s followed by a 0.
    unary = '1' * quotient + '0'
    
    # Encode remainder in binary. The length of the binary representation is log2(M).
    binary_length = M.bit_length() - 1
    binary = format(remainder, f'0{binary_length}b')
    
    return unary + binary

def golomb_rice_decode(encoded, M):
    """
    Decodes a Golomb-Rice coded binary string for a given parameter M.
    
    :param encoded: The Golomb-Rice encoded binary string.
    :param M: The parameter M, which must be a power of 2.
    :return: The decoded integer value.
    """
    # Split the encoded string into unary (quotient) and binary (remainder) parts.
    quotient = 0
    while encoded[quotient] == '1':
        quotient += 1
    encoded = encoded[quotient + 1:]  # Skip over the unary part and the separator '0'.
    
    binary_length = M.bit_length() - 1
    remainder = int(encoded[:binary_length], 2)
    
    value = quotient * M + remainder
    return value

# Example usage:
M = int(input("Enter The m parameter here"))  # Choose M as a power of 2, for simplicity in this example.
value = int(input("Enter the value you want to encode here"))  # Value to encode and then decode.

encoded = golomb_rice_encode(value, M)
decoded = golomb_rice_decode(encoded, M)

print(encoded,decoded)