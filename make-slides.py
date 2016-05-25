#!/usr/bin/env python3

import convert
import template
import os
import re


def is_markdown_file(file_name):
    _, ext = os.path.splitext(file_name)
    return ext == '.md'


def list_markdown_files():
    return [file_name for file_name in os.listdir(os.getcwd())
            if is_markdown_file(file_name)]


def first(elements):
    return elements[0]


def second(elements):
    return elements[1]


def sort_slides(file_names):
    def parse_slide_number(file_name):
        slide_number_string, _ = os.path.splitext(file_name)
        slide_number = int(slide_number_string)
        return slide_number
    slide_numbers_and_file_names = [(parse_slide_number(file_name), file_name)
            for file_name in file_names]
    slide_numbers_and_file_names = sorted(slide_numbers_and_file_names, key=first)
    return [second(slide_number_and_file_name)
            for slide_number_and_file_name in slide_numbers_and_file_names]


def make_slide_file_name(slide_number):
    return 'slide-{}.html'.format(slide_number)


def parse_slide_title(markdown_file_name):
    with open(markdown_file_name, 'r') as markdown_file:
        lines = markdown_file.readlines()
        title_line = first(lines).strip()
        match = re.match('^#\s+(.+)$', title_line)
        return match.group(1)


def make_slide(slide_number, markdown_file_name, slide_count):
    content_file_name = 'content.html'
    convert.main(markdown_file_name, content_file_name)
    template_file_name = 'template.html'
    slide_file_name = make_slide_file_name(slide_number)
    next_slide_number = slide_number + 1 if slide_number < slide_count else 1
    next_slide_file_name = make_slide_file_name(next_slide_number)
    previous_slide_number = slide_number - 1 if slide_number > 1 else slide_count
    previous_slide_file_name = make_slide_file_name(previous_slide_number)
    title = parse_slide_title(markdown_file_name)
    template.main(template_file_name, slide_file_name, title,
            next_slide_file_name, previous_slide_file_name)


def main():
    markdown_file_names = list_markdown_files()
    markdown_file_names = sort_slides(markdown_file_names)
    slide_count = len(markdown_file_names)
    for slide_index, markdown_file_name in enumerate(markdown_file_names):
        slide_number = slide_index + 1
        make_slide(slide_number, markdown_file_name, slide_count)


if __name__ == '__main__':
    main()
