from glob import iglob

def do(file_path):
    headers = []
    data_char = set()
    data_word = set()

    with open(file_path) as f:
        # header
        for line in f:
            line = line.rstrip('\n')

            if line == '...':
                headers.append(line)
                break

            headers.append(line)

        # data
        for line in f:
            line = line.rstrip('\n')

            if not line:
                continue

            word, romans, *extras = line.split('\t')
            (data_char if len(word) == 1 else data_word).add((word, romans, tuple(extras)))

    data_char = sorted(data_char, key=lambda xyz: (len(xyz[0]), *xyz))
    data_word = sorted(data_word, key=lambda xyz: (len(xyz[0]), *xyz))

    with open(file_path, 'w') as f:
        # header
        for line in headers:
            print(line, file=f)
        print(file=f)

        # data
        if data_char:
            for ch, roman, extras in data_char:
                print(ch, roman, *extras, sep='\t', file=f)
            print(file=f)

        for ch, roman, extras in data_word:
            print(ch, roman, *extras, sep='\t', file=f)


for file_path in iglob('*.dict.yaml'):
    do(file_path)
