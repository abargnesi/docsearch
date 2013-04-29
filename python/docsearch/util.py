# coding: utf-8
import epub
from bs4 import BeautifulSoup
from itertools import chain


def read_epub_metadata(path):
    with epub.open_epub(path) as book:
        metadata = book.opf.metadata
        res = {
            'description': empty_guard(metadata.description),
            'subject': empty_guard(",".join(metadata.subjects)),
            'publisher': empty_guard(metadata.publisher)
        }
        titles = list(chain.from_iterable(metadata.titles))
        creators = list(chain.from_iterable(metadata.creators))
        dates = list(chain.from_iterable(metadata.dates))
        if len(titles) > 0:
            res['title'] = empty_guard(titles[0])
        if len(creators) > 0:
            res['author'] = empty_guard(creators[0])
        if len(dates) > 0:
            res['date'] = empty_guard(dates[0])
        return res


def empty_guard(seq):
    if seq and len(seq) > 0:
        return seq
    return None


def read_epub_html(path):
    data = ''
    with epub.open_epub(path) as book:
        opf_values = book.opf.manifest.values()
        for i in filter(lambda x: x.href.endswith('.html'), opf_values):
            bs = BeautifulSoup(str(book.read_item(i)), 'html.parser')
            data += bs.get_text()
    return data
