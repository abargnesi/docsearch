docsearch
=========

Command-line index and search over documents.

requirements
------------

- python3
- virtualenv

libraries used
--------------

- whoosh: to index/search documents
- epub: to read epub format
- beautifulsoup4: parse html
- pyzmq: process queries over socket

scripts
-------

- **make_env.sh**: builds virtual environment using libraries in
                   **scripts/requirements**
- **index.sh**: script to index using glob pattern (i.e. /home/blah/*.epub)
- **search.sh**: script to search using whoosh query syntax
- **search-server.sh**: loads index and listens for whoosh query over a zeromq
                        socket; reply with results in JSON format
- **search-client.sh**: read from stdin and send whoosh query over a zeromq
                        socket; print JSON results that return
