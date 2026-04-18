#!/usr/bin/env python3

import re
"""
Find inheritance-related words and write line numbers + words to a file.
"""

import re


def find_words(input_file, output_file, pattern):
    with open(input_file, 'r') as in_stream:
        with open(output_file, 'w') as out_stream:

            for line_number, line in enumerate(in_stream, start=1):

                matches = pattern.findall(line)

                for match in matches:
                    out_stream.write(f"{line_number}\t{match}\n")


if __name__ == '__main__':
    herit_pattern_str = r'\w*herit\w*'
    herit_pattern = re.compile(herit_pattern_str, re.IGNORECASE)

    input_file = 'origin.txt'
    output_file = 'results.txt'

    find_words(input_file, output_file, herit_pattern)

    print("Done! Check results.txt")
