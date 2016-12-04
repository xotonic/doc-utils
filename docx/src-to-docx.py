#!/usr/bin/python
# -*- coding: utf-8 -*-

import fnmatch
import getopt
import os
import sys
import time
import random

s = "  _    _                                        \n | |  | |      /\                               \n | |  | |_ __"\
    " /  \   _ __  _   _ ___            \n | |  | | '__/ /\ \ | '_ \| | | / __|           \n | |__| | | / ____ \| | | "\
    "| |_| \__ \           \n  \____/|_|/_/    \_\_| |_|\__,_|___/     _     \n |  __ \                               "\
    "  | |    \n | |__) |___  ___  ___  __ _ ___ _ __ ___| |__  \n |  _  // _ \/ __|/ _ \/ _` / __| '__/ __| '_ \ \n |"\
    " | \ \  __/\__ \  __/ (_| \__ \ | | (__| | | |\n |_|  \_\___||___/\___|\__,_|___/_|  \___|_| |_|\n | |         | "\
    "|                                \n | |     __ _| |__  ___                         \n | |    / _` | '_ \/ __|    "\
    "                    \n | |___| (_| | |_) \__ \                        \n |______\__,_|_.__/|___/ \n\n"\
    "\t\tPresents\n\t\tSource code 2 DOCX converter {}.{}\n\n".format(random.randint(0, 4), random.randint(0, 9))

help = (
    "This script requires Pandoc package! Google and install it. It is easy.\n\n"
    "Description:\nThe script searches files in directory, merges them into one big markdown\n"
    "and then uses Pandoc to convert .MD file to .DOCX\n\n"
    "Usage:\n"
    "-h : shows this help\n"
    "-d --directory : path for searching source files\n"
    "-o --output : output file name ( with .docx extension)\n"
    "-l --language : language key for searching from list below\n"
    "   - java\n"
    "   - python\n"
    "   - c-headers\n"
    "   - c-code\n"
    "   - cpp-headers\n"
    "   - cpp-code\n"
    "   - csharp\n"
)

def main(argv):
    search_path = "."
    output_file = "out.docx"
    temd_md = "temp.md"
    title_prefix = "Файл"
    lang_key = "java"

    langs = {
        'java': ('*.java', 'java'),
        'python': ('*.py', 'python'),
        'c-headers': ('*.h', 'c'),
        'c-code': ('*.h', 'c'),
        'cpp-headers': ('*.h', 'c++'),
        'cpp-code': ('*.cpp', 'c++'),
        'csharp': ('*.cs', 'cs'),
    }

    print(s)
    time.sleep(2)

    try:
        opts, args = getopt.getopt(argv, "hd:o:l:", ["directory=", "output=", "language="])
    except getopt.GetoptError:
        print(help)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help)
            sys.exit()
        elif opt in ("-d", "--directory"):
            search_path = arg
        elif opt in ("-o", "--output"):
            output_file = arg
        elif opt in ("-l", "--language"):
            lang_key = arg

    if lang_key not in langs:
        print('ERROR No such language "{}"\n'.format(lang_key))
        exit(1)

    pattern = langs[lang_key][0]
    markdown_keyword = langs[lang_key][1]

    print("\tLanguage   : {}".format(lang_key))
    print("\tSearch path: {}".format(search_path))
    print("\tOutput file: {}".format(output_file))
    print("\tPattern    : {}".format(pattern))
    print("\tMarkdown keyword : {}".format(markdown_keyword))
    print("\n\n")

    markdown_temp = open(temd_md, 'a')

    print("Files found:")

    for root, dirnames, filenames in os.walk(search_path):
        for filename in fnmatch.filter(filenames, pattern):
            print(filename)
            path = os.path.join(root, filename)
            src = open(path, 'r')
            markdown_temp.write("**{} {}**\n".format(title_prefix, filename))
            markdown_temp.write("```{}\n".format(markdown_keyword))
            markdown_temp.writelines(src.readlines())
            markdown_temp.write("```\n\n")
            src.close()

    markdown_temp.close()

    os.system("pandoc {} -f markdown -t docx -o {}".format(temd_md, output_file))
    os.remove(temd_md)
    print("Done!")


if __name__ == "__main__":
    main(sys.argv[1:])
