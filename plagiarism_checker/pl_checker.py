#!/usr/bin/env python3
import argparse
import sys
import re


def get_text(file):
    with open(file, 'r') as text_file:
        content = text_file.read()
    return content


def run(args):
    parser = argparse.ArgumentParser(description='Checks if parts in text file 1 occurs in text file 2')
    parser.add_argument('-o', '--one', type=str, required=True,
                        help="First text file.")
    parser.add_argument('-t', '--two', type=str, required=True,
                        help="Second text file.")
    parser.add_argument('-l', '--len', type=int, default=5,
                        help="Number of words to check")

    args = parser.parse_args()
    textfile1_content = get_text(args.one).split()
    #print(textfile1_content)
    textfile2_content = get_text(args.two)
    for n in range(len(textfile1_content)):
        #print("n:",n)
        words = ' '.join(textfile1_content[n:n+args.len])
        try:
            matches = re.findall(words, textfile2_content)
        except: print('')
        if matches:
            print('found: {}, ({})'.format(words, len(matches)))


if __name__ == '__main__':
    run(sys.argv)
