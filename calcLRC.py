def calcLRC(Msg):
    chs = list(Msg)

    print(chs)
    ch = [hex(c) for c in chs]
    uchLRC = sum(ch)
    print(uchLRC)
    uchLRC = uchLRC & 0xff
    print(uchLRC)
    out = twos_comp(uchLRC, 8)
    print(out)

def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is


def main():
    calcLRC("1103006B0003")



if __name__ == '__main__':
    main()