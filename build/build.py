kyonh2描述 = {}

with open('cache/kyonh.txt') as f:
    for line in f:
        描述, 拼音 = line.rstrip('\n').split('\t')
        kyonh2描述[拼音] = 描述

描述2tshet = {}

with open('cache/tshet.txt') as f:
    for line in f:
        描述, 拼音 = line.rstrip('\n').split('\t')
        描述2tshet[描述] = 拼音

g2 = open('cache/unhandled2.txt', 'w')


def do(input_file, output_file):
    with open(input_file) as f, open(output_file, 'w') as g:
        for line in f:
            if line == '...\n':
                g.write(line)
                break
            line = line.replace('kyonh', 'tshet')
            g.write(line)

        for line in f:
            line = line.rstrip('\n')

            if not line:
                g.write('\n')
                continue

            ch, 拼音們, *extra = line.split('\t')

            try:
                new拼音們 = ' '.join(描述2tshet[kyonh2描述[拼音]] for 拼音 in 拼音們.split(' '))
                print(ch, new拼音們, *extra, file=g, sep='\t')
            except KeyError:
                for c, 拼音 in zip(ch, 拼音們.split(' ')):
                    if 拼音 not in kyonh2描述:
                        print(拼音, c, file=g2)


do('../rime-kyonh/kyonh.dict.yaml', 'tshet.dict.yaml')
do('../rime-kyonh/kyonh.words.dict.yaml', 'tshet.words.dict.yaml')

g2.close()
