import Functions
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

def mapping_to_2d_array(mapping):
    """
    Convert mapping dictionary to a 2D array.

    Args:
        mapping (dict): Mapping of characters to Huffman codes.

    Returns:
        list: 2D array containing characters and their Huffman codes.
    """
    mapping_array = []
    for char, code in mapping.items():
        mapping_array.append([char, int(code)])
    return mapping_array



def compression_with_huffman(message):

    tree = build_huffman_tree(message)
    mapping = build_huffman_mapping(tree)
    # print(mapping)
    array_mapping=mapping_to_2d_array(mapping)
    # print(array_mapping)


    prob_table=Functions.calculate_probabilities(message)

    avg_length=Functions.calculate_average_length(mapping,prob_table)
    entropy=Functions.calculate_entropy(message)
    efficiency=(entropy/avg_length)*100

    encoded_message = huffman_encode(message, mapping)  # results
    bits_before=Functions.calculate_bits_before(message)
    bits_after = len(encoded_message)

    Compression_ratio = bits_before / bits_after



    return {
            "result": encoded_message,
            "bits_before": bits_before,
            "bits_after": bits_after,
            "cr": Compression_ratio,
            "entropy": entropy,
            "avg_len": avg_length,
            "efficiency": efficiency,
            "prob_dict": prob_table
        }

if __name__ == "__main__":
    v=compression_with_huffman("aaaabbccdf")
    print(v)

