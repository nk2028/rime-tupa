#!/bin/sh

set -e

node scripts/generate_map.js
python scripts/build.py
python scripts/build_unspaced.py
python scripts/uniqsort.py
