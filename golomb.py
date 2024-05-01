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

    return {
            "result": golocode,
            "bits_before": bits_before,
            "bits_after": bits_after,
            "cr": Compression_ratio,
        }


x=golomb(21,5)
#print(x)
