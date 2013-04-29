#!/usr/bin/env python3
# coding: utf-8
INDEX_DIR = '.index'
import json


def main(search_query):
    from whoosh.index import open_dir
    from whoosh.qparser import QueryParser

    ix = open_dir(INDEX_DIR)
    parser = QueryParser("content", ix.schema)
    q = parser.parse(search_query)

    with ix.searcher() as searcher:
        results = searcher.search(q)
        entries = [r.fields() for r in results]
        print(json.dumps({'results': entries}))


if __name__ == '__main__':
    from sys import argv, exit, stderr

    if len(argv) != 2:
        stderr.write('usage: search <search_query>\n')
        exit(1)
    main(argv[1])
