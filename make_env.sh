#!/usr/bin/env bash
if [ ! -d _env ] || [ 'scripts/requirements' -nt _env ]; then
    echo 'rebuilding environment'
    rm -fr _env
    cd scripts
    python3 bootstrap.py ../_env
    cd ..
fi
