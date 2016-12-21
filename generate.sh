#!/bin/bash
set -e
export PATH=$PATH:~/.composer/vendor/bin
mkdir -p generate/static
daux generate --format=html --source=docs --destination=generate/static
for f in $(find generate/static -name '*.html'); do python group_code_block.py "$f"; done
