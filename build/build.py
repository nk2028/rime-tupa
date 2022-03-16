with open('cache/kyonh.txt') as f:
    kyonh2descr = dict(line.rstrip('\n').split('\t')[::-1] for line in f)

with open('cache/tshet.txt') as f:
    descr2tshet = dict(line.rstrip('\n').split('\t') for line in f)

def do(fin, fout, ferr):
    # header
    for line in fin:
        line = line.rstrip('\n')

        if line == '...':
            print(line, file=fout)
            break

        line = line.replace('kyonh', 'tshet')
        print(line, file=fout)

    # data
    for line in fin:
        line = line.rstrip('\n')

        if not line:
            print(file=fout)
            continue

        word, romans, *extras = line.split('\t')

        try:
            romans = ' '.join(descr2tshet[kyonh2descr[roman]] for roman in romans.split(' '))
            print(word, romans, *extras, sep='\t', file=fout)
        except KeyError:
            for c, roman in zip(word, romans.split(' ')):
                if roman not in kyonh2descr:
                    print(roman, c, file=ferr)


with open('cache/unhandled2.txt', 'w') as ferr:
    with open('../rime-kyonh/kyonh.dict.yaml') as fin, open('tshet.dict.yaml', 'w') as fout:
        do(fin, fout, ferr)
    with open('../rime-kyonh/kyonh.words.dict.yaml') as fin, open('tshet.words.dict.yaml', 'w') as fout:
        do(fin, fout, ferr)
