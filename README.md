docsearch
=========

Command-line index and search over technical documents.

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
