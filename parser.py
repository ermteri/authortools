#!/usr/bin/env python3
import argparse
import sys
import re


def get_text(file):
    with open(file, 'r') as text_file:
        content = text_file.read()
    return content


def run(args):
    parser = argparse.ArgumentParser(description='Checks if a text file contains misspelled worlds/phrases')
    parser.add_argument('-t', '--text', type=str, required=True,
                        help="The text file to read.")
    parser.add_argument('-f', '--faulty', type=str, required=True,
                        help="List of misspelled words.")

    args = parser.parse_args()
    content = get_text(args.text)
    faulty = get_text(args.faulty).splitlines()
    for word in faulty:
        matches = re.findall('\s' + word + '\s', content)
        if matches:
            print('found: {}, ({})'.format(word, len(matches)))


if __name__ == '__main__':
    run(sys.argv)
