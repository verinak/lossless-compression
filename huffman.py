import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(message):
    frequency = Counter(message)
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_huffman_mapping(node, code='', mapping=defaultdict(str)):
    if node.char is not None:
        mapping[node.char] = code
    else:
        build_huffman_mapping(node.left, code + '0', mapping)
        build_huffman_mapping(node.right, code + '1', mapping)
    return mapping

def huffman_encode(message, mapping):
    encoded_message = ''.join(mapping[char] for char in message)
    return encoded_message

def calculate_bits(message):
    return len(message) * 8  # Assuming 8 bits per character

def calculate_compression_ratio(before_bits, after_bits):
    return before_bits / after_bits

# Example usage
message = input("Enter your message here")
tree = build_huffman_tree(message)
mapping = build_huffman_mapping(tree)
encoded_message = huffman_encode(message, mapping)

before_bits = calculate_bits(message)
after_bits = len(encoded_message)

compression_ratio = calculate_compression_ratio(before_bits, after_bits)

print("Original Message:", message)
print("Encoded Message:", encoded_message)
print("Total bits before encoding:", before_bits)
print("Total bits after encoding:", after_bits)
print("Compression ratio:", compression_ratio)
