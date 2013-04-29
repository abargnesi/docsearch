#!/usr/bin/env python3
# coding: utf-8
from docsearch.util import *
INDEX_DIR = '.index'


def main(file_pattern):
    from glob import glob
    from os import mkdir
    from os.path import basename, splitext
    from whoosh.index import create_in
    from whoosh.fields import Schema, ID, TEXT

    files = glob(file_pattern)
    if len(files) == 0:
        stderr.write('no files selected')
        exit(2)

    try:
        mkdir(INDEX_DIR)
    except OSError:
        pass
    schema = Schema(file_name=ID(stored=True), file_path=ID(stored=True),
                    title=TEXT(stored=True), description=TEXT(stored=True),
                    subject=ID(stored=True), author=ID(stored=True),
                    publisher=ID(stored=True), date=ID(stored=True),
                    content=TEXT)
    ix = create_in(INDEX_DIR, schema)
    writer = ix.writer()

    for f in files:
        data = {
            'file_name': basename(f),
            'file_path': f
        }
        ext = splitext(f)[1]
        if ext == '.epub':
            data.update(read_epub_metadata(f))
            data['content'] = read_epub_html(f)
        elif ext == '.pdf':
            content = 'meh, i\'m a pdf'
        else:
            print('%s: unknown file type' % (f))
            continue

        writer.add_document(**data)
    writer.commit()

if __name__ == '__main__':
    from sys import argv, exit, stderr

    if len(argv) != 2:
        stderr.write('usage: index <file_pattern>\n')
        exit(1)
    main(argv[1])
