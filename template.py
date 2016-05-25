#!/usr/bin/env python3

from jinja2 import FileSystemLoader
from jinja2.environment import Environment
from argparse import ArgumentParser
import os


def parse_options():
    parser = ArgumentParser()
    parser.add_argument('--in', dest='template_file_name')
    parser.add_argument('--out', dest='out_file_name')
    parser.add_argument('--title', dest='title')
    parser.add_argument('--next', dest='next_slide')
    parser.add_argument('--previous', dest='previous_slide')
    options = parser.parse_args()
    return options.template_file_name, options.out_file_name, options.title, \
            options.next_slide, options.previous_slide


def main(template_file_name, out_file_name, title, next_slide, previous_slide):
    env = Environment()
    env.loader = FileSystemLoader(os.getcwd())
    template = env.get_template(template_file_name)
    html = template.render({
        'title': title,
        'next': next_slide,
        'previous': previous_slide
    })
    with open(out_file_name, 'w') as out_file:
        out_file.write(html)


if __name__ == '__main__':
    template_file_name, out_file_name, title, next_slide, previous_slide = \
            parse_options()
    main(template_file_name, out_file_name, title, next_slide, previous_slide)
