import re

with open('cache/kyonh.txt') as f:
    kyonh2descr = dict(line.rstrip('\n').split('\t')[::-1] for line in f)

with open('cache/tupa.txt') as f:
    descr2tupa = dict(line.rstrip('\n').split('\t') for line in f)


class MissingDescription(Exception):
    pass


FIXES = {
    # 來自審音討論 https://github.com/ayaka14732/rime-tshet/discussions/2
    # 後起字
    '來開陽入': (
        ('撂', '來蕭去'),
    ),
    '生合脂平': (
        ('摔', '生合眞入'),
    ),
    '生合支上': (
        ('甩', '生合眞入'),
    ),
    '心開清上': (
        ('擤', '曉開二庚上'),
    ),
    '並肴平': (
        ('跑', '滂肴上', True),
    ),
    '孃尤平': (
        ('妞', '孃尤上'),
    ),
    # 合音字
    '孃侵平': (
        ('您', '孃侵上'),
    ),
    '影覃上': (
        ('俺', '疑覃上'),
    ),
    '莊侵上': (
        ('怎', '!tsoimq'),  # 切韻音系外地位
    ),
    '書開三麻上': (
        ('啥', '常開三麻上'),
    ),
    '見開二麻平': (
        ('旮', '見江入'),
    ),
    '來開二麻平': (
        ('旯', '來開唐入'),
    ),
    '心談平': (
        ('仨', '心開一歌平'),
    ),
    '心談入': (
        ('仨', '心開一歌平'),
    ),

    # 其他
    # 後起字
    '疑開B仙去': (
        ('這', '章開三麻上', True),  # 僅於詞中修正
    ),
    '幫耕平': (
        ('拼', '滂青平',  # 僅調整列出的詞
         ('拼力', '拼命', '拼死', '拼火', '拼爭', '拼鬥', '血拼', '拼到底')),
        ('拼', '幫A清平', True)
    ),
    # unt 校訂地位（部分）
    '羣開佳上': (
        ('箉', '定開佳上'),
        (None, '見合佳上'),
    ),
    '見開B仙入': (
        ('孑訐𨥂趌𡤼', '見開A仙入'),
    ),
    '影開蒸入': (
        ('抑𡊁𢬃𡊶', '!qyik'),  # qieyun-js 外地位（0.13 將修正）
    ),
    '溪尤平': (
        ('𠁫𰀧㲃恘惆𣪘', '!khyiw'),  # qieyun-js 外地位（0.13 將修正）
    ),
    # 其他錯音
    '曉開齊上': (
        (None, '匣開齊上'),
    ),
}


def convert(ch, roman_kyonh, word):
    try:
        descr = kyonh2descr[roman_kyonh]
    except KeyError:
        raise MissingDescription
    for chs, fix, *ext in FIXES.get(descr, ()):
        if chs is not None and ch not in chs:
            continue
        if len(ext) > 0:
            if type(ext[0]) == bool:
                if ext[0] != (len(word) > 1):
                    continue
            elif isinstance(ext[0], (list, tuple)):
                if word not in ext[0]:
                    continue
        descr = fix if fix is not None else descr
        if descr.startswith('!'):
            return descr[1:]
        break
    return descr2tupa[descr]


ADDITIONAL = '''
拼\tpiaeng
韻\tuinh
跑\tphaewq\t95%
咱\tdza
咋\ttsaq\t90%
間\tkeen
'''.lstrip()


def do(fin, fout, ferr, additional=None):
    # header
    for line in fin:
        line = line.rstrip('\n')

        if line == '...':
            print(line, file=fout)
            break

        line = line.replace('kyonh', 'tupa')
        print(line, file=fout)

    # data
    for line in fin:
        line = line.rstrip('\n')

        if not line:
            print(file=fout)
            continue

        word, romans_str, *extras = line.split('\t')
        romans = romans_str.split(' ')
        assert len(word) == len(romans)

        try:
            romans = ' '.join(convert(c, roman, word)
                              for c, roman in zip(word, romans))
            print(word, romans, *extras, sep='\t', file=fout)
        except MissingDescription:
            for c, roman in zip(word, romans):
                if roman not in kyonh2descr:
                    print(roman, c, file=ferr)

    if additional:
        print(additional, end='', file=fout)


with open('cache/unhandled2.txt', 'w') as ferr:
    with open('../rime-kyonh/kyonh.dict.yaml') as fin, open('tupa.dict.yaml', 'w') as fout:
        do(fin, fout, ferr, ADDITIONAL)
    with open('../rime-kyonh/kyonh.words.dict.yaml') as fin, open('tupa.words.dict.yaml', 'w') as fout:
        do(fin, fout, ferr)
