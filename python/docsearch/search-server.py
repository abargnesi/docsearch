#!/usr/bin/env python3
# coding: utf-8
INDEX_DIR = '.index'


if __name__ == '__main__':
    from whoosh.index import open_dir
    from whoosh.qparser import QueryParser
    import json
    import zmq

    # establish query parser
    ix = open_dir(INDEX_DIR)
    parser = QueryParser("content", ix.schema)

    # bind REQUEST_REPLY socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://*:9000')

    # process queries
    while True:
        request = socket.recv_string()
        q = parser.parse(request)
        with ix.searcher() as searcher:
            results = searcher.search(q)
            entries = [r.fields() for r in results]
            reply = json.dumps({'results': entries})
            socket.send_unicode(reply)
