#!/bin/bash
# runs script in docker container
REQ_INSTALL=""
if [ -f './requirements.txt' ]; then
    REQ_INSTALL="pip install -r requirements.txt; "
fi

docker \
    run -it --rm \
    --name test-python-run\
    -v "$PWD":/usr/src/runtime \
    -w /usr/src/runtime \
        python:3 \
            /bin/bash -c \
                "${REQ_INSTALL}python ${1}"
