#!/usr/bin/env python
import fileinput

packets = [[[2]], [[6]]]
decoder_key = 1


def compare(left, right) -> str:
    if isinstance(left, int):
        if isinstance(right, int):
            if left < right:
                return '👍'
            if right < left:
                return '👎'
            return '🤷‍♂️'
        elif isinstance(right, list):
            return compare([left], right)
    if isinstance(left, list):
        if isinstance(right, int):
            return compare(left, [right])
        elif isinstance(right, list):
            for i in range(min(len(left), len(right))):
                result = compare(left[i], right[i])
                if result == '👍' or result == '👎':
                    return result
            if len(left) < len(right):
                return '👍'
            if len(right) < len(left):
                return '👎'
            return '🤷‍♂️'


def merge_sort(packet_slice: list[list]) -> list[list]:
    if len(packet_slice) == 1:
        return packet_slice
    sorted_left = merge_sort(packet_slice[:len(packet_slice)//2])
    sorted_right = merge_sort(packet_slice[len(packet_slice)//2:])
    combined = []
    while len(sorted_left) and len(sorted_right):
        if compare(sorted_left[0], sorted_right[0]) == '👍':
            combined.append(sorted_left.pop(0))
        else:
            combined.append(sorted_right.pop(0))
    # append leftovers
    while len(sorted_left):
        combined.append(sorted_left.pop(0))
    while len(sorted_right):
        combined.append(sorted_right.pop(0))
    return combined


for line in fileinput.input():
    if line[0] == '\n':
        continue
    packets.append(eval(line))  # eval ftw

sorted_packets = merge_sort(packets)

for i, packet in enumerate(sorted_packets):
    if packet == [[2]] or packet == [[6]]:
        decoder_key = decoder_key * (i + 1)

print(f'Decoder key: {decoder_key}')
