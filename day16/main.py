#!usr/bin/env python3.9
import itertools
from collections import Counter, defaultdict, deque


def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


# 8A004A801A8002F478 represents an operator packet (version 4) which contains an operator packet (version 1)
# which contains an operator packet (version 5) which contains a literal value (version 6); this packet has
# a version sum of 16.

# 620080001611562C8802118E34 represents an operator packet (version 3) which contains two sub-packets;
# each sub-packet is an operator packet that contains two literal values. This packet has a version sum of 12.

# C0015000016115A2E0802F182340 has the same structure as the previous example, but the outermost packet uses
# a different length type ID. This packet has a version sum of 23.

# A0016C880162017C3686B18A3D4780 is an operator packet that contains an operator packet that contains an
# operator packet that contains five literal values; it has a version sum of 31.


def gbin(hex):
    return bin(int(hex, 16))


def j(l):
    return "".join(l)


def packet_info(chain):
    chain = j(chain)
    if not chain.strip("0"):
        return 0, 0, []

    packet_version = int(chain[:3], 2)
    packet_type = int(chain[3:6], 2)
    return packet_version, packet_type, chain[6:]


COUNT = 0


def count_packets(chain):
    ver, typ, info = packet_info(j(chain).lstrip("0"))

    if not ver:
        return 0

    global COUNT
    COUNT += ver
    print(ver, typ, info)

    if typ == 4:
        for i in range(0, len(info), 5):
            if int(info[i]) == 0:
                return count_packets(info[i + 5 :]) + 1
    else:
        i, *info = info
        print(i)
        if int(i) == 0:
            # next 15 bits are the length of the next packet
            sub_packet_length = int(j(info[:15]), 2)
            return count_packets(info[15 : 15 + sub_packet_length]) + 1
        else:
            # next 11 bits are the number of sub-packets
            amount_of_sub_packets = int(j(info[:11]), 2)
            return count_packets(info[11:]) + 1


def main():
    chain = gbin("8A004A801A8002F478")[2:]
    # chain = gbin("620080001611562C8802118E34")[2:]
    count_packets(chain)
    print(COUNT)


if __name__ == "__main__":
    main()
