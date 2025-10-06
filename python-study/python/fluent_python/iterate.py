def count_down(n):
    while n > 0:
        yield n
        n -= 1

it = count_down(3)

for i in it:
    print(i)


import re
import reprlib

RE_WORD = re.compile(r'\w+')


class SentenceV1:

    def __init__(self, text):
        self.text = text
        # 使用正则表达式分割单词
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

s = SentenceV1('"The time has com," the Walrus said,')
print(s)

for word in s:
    print(word, end=" ")
print()
l = list(s)
print(l)

def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i
s = 'ABC'
r = range(3)
l = list(chain(s, r))
print(l)


# 用yield from重新实现chain
def chain(*iterables):
    for i in iterables:
        yield from i
l=list(chain(s, r))
print(l)




