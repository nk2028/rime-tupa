from glob import glob

def do(file_path):
    headers = []
    chars = set()
    words = set()

    with open(file_path) as f:
        for line in f:
            if line == '...\n':
                headers.append(line)
                break
            headers.append(line)

        for line in f:
            line = line.rstrip('\n')
            if not line:
                continue
            ch, roman, *extras = line.split('\t')
            (chars if len(ch) == 1 else words).add((ch, roman, tuple(extras)))

    chars = sorted(chars, key=lambda xyz: (len(xyz[0]), *xyz))
    words = sorted(words, key=lambda xyz: (len(xyz[0]), *xyz))

    with open(file_path, 'w') as f:
        for line in headers:
            f.write(line)
        f.write('\n')

        if chars:
            for ch, roman, extras in chars:
                print(ch, roman, *extras, sep='\t', file=f)
            f.write('\n')

        for ch, roman, extras in words:
            print(ch, roman, *extras, sep='\t', file=f)


for file_path in glob('*.dict.yaml'):
    do(file_path)
