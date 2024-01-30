#!/usr/bin/env python3
import argparse
import sys
import re



def get_text(file):
    with open(file, 'r') as text_file:
        content = text_file.readlines()
    return content


def run(args):
    parser = argparse.ArgumentParser(description='Checks if a text file contains long dialog')
    parser.add_argument('-t', '--text', type=str, required=True,
                        help="The text file to read.")

    args = parser.parse_args()
    content = get_text(args.text)
    for line in content:
        matches = re.findall('^–', line)
        if matches:
            if len(line) > 200:
                print('{}: {}'.format(len(line), line))
                print('###################################')


if __name__ == '__main__':
    run(sys.argv)
