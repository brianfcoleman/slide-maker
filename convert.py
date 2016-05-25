#!/usr/bin/env python3

from markdown import Markdown
from argparse import ArgumentParser


def parse_options():
    parser = ArgumentParser()
    parser.add_argument('--in', dest='in_file_path')
    parser.add_argument('--out', dest='out_file_path')
    options = parser.parse_args()
    return options.in_file_path, options.out_file_path


def main(in_file_path, out_file_path):
    with open(in_file_path, 'r') as in_file, \
            open(out_file_path, 'w') as out_file:
        converter = Markdown(output_format='html5')
        markdown = in_file.read()
        html = converter.convert(markdown)
        out_file.write(html)


if __name__ == '__main__':
    in_file_path, out_file_path = parse_options()
    main(in_file_path, out_file_path)
