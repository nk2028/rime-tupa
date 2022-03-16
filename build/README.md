## Build rime-tshet

```sh
npm install
mkdir -p cache
node build/generate_map.js
python build/build.py
python build/build_unspaced.py
```
