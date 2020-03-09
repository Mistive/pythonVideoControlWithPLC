def calcLRC(data):
    #Add the RTU Value
    RTU_sum = ((sum(data) & 0xff) ^ 0xff) + 0x01

    lrc = [RTU_sum >> 4, RTU_sum & 0xf]

    return lrc


def hexToAscii(data):
    ret = []
    for d in data:
        ret.append(ord(format(d, 'X')))

    return ret

def main():
    LRC = calcLRC([0x11, 0x03, 0x00, 0x6B, 0x00, 0x03])
    data2 = hexToAscii(LRC)
    print(LRC)
    print(data2)

if __name__ == '__main__':
    main()