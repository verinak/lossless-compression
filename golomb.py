import Functions
import math

def golomb_cod(x,m):
    c = int(math.ceil(math.log(m,2)))
    remin = x % m
    quo =int(math.floor(x / m))
    #print "quo is",quo
    #print "reminder",remin
    #print "c",c
    div = int(math.pow(2,c) - m)
    #print "div",div
    first = ""
    for i in range(quo):
        first = first + "1"
    #print first

    if (remin < div):
        b = c - 1
        a = "{0:0" + str(b) + "b}"
        #print "1",a.format(remin)
        bi = a.format(remin)
    else:
        b = c
        a = "{0:0" + str(b) + "b}"
        #print "2",a.format(remin+div)
        bi = a.format(remin+div)

    final = first + "0" +str(bi)
    #print "final",final
    return final


def golomb(n,m):
    n=n
    m=m
    golocode = golomb_cod(n,m)
    bits_before=len(bin(n)[2:])
    bits_after=len(golocode)
    Compression_ratio=bits_before/bits_after

    result = { 
            "result": golocode,
            "bits_before": bits_before,
            "bits_after": bits_after,
            "cr": Compression_ratio,
        }

    return result


# x=golomb(42,6)
# print(x)

#######################handel if user entered binary(tari2et el dr)####################################################################

def binary_to_list(binary_string): ## binary to list of numbers
    encoded_message = []

    # start counting with the first charcter in the message
    letter = binary_string[0]
    count = 0
    # iterate over each character in the message
    for char in binary_string:
        # if character is found at current index, count++
        if(char == letter):
            count = count + 1
        # else (different character found at current index)
        # append current count to encoded message
        # then start counting the new character
        else:
            encoded_message.append(count)
            letter = char
            count = 1

    encoded_message.append(count)        
    # append count of the last character to encoded message
    return encoded_message

# Example usage
# binary_string = "00000000100000000000100001111111111111111000000001111111010000000011"
# result_list = binary_to_list(binary_string)
# print(result_list)  

 
def calculate_golomb_and_stats(binary_string):   #calculate golumb for list of numbers , di elfunction eli hanadiha lw user da5al binary 
    m_list = []
    result_list = binary_to_list(binary_string)
    bits_before_total = 0
    bits_after_total = 0
    
    for num in result_list:
        m_list.append(round(math.sqrt(num)))
    
    golomb_results = []
    for i in range(len(result_list)):
        golocode = golomb(result_list[i], m_list[i])["result"]
        #print(golocode)
        bits_before_total = len(binary_string)  # Total bits before compression
        bits_after = len(golocode)  # Total bits after compression
        bits_after_total += bits_after
        golomb_results.append(golocode)
    
    compression_ratio = bits_before_total / bits_after_total
    
    return {
        "result": ''.join(golomb_results),
        "bits_before": bits_before_total,
        "bits_after": bits_after_total,
        "cr": compression_ratio
    }
