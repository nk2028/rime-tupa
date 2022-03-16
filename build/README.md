## Build rime-tshet

```sh
npm install
rm -rf cache *.dict.yaml
mkdir -p cache
node build/generate_map.js
python build/build.py
python build/uniqsort.py
python build/build_unspaced.py
```
