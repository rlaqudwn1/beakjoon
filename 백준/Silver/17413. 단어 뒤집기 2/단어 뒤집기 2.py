import sys
s = sys.stdin.readline().rstrip()

result = []
word = []
in_tag = False

for ch in s:
    if ch == '<':
        # 단어 버퍼 비우기
        if word:
            result.append(''.join(word[::-1]))
            word.clear()
        in_tag = True
        result.append(ch)
    elif ch == '>':
        in_tag = False
        result.append(ch)
    elif in_tag:
        result.append(ch)
    elif ch == ' ':
        result.append(''.join(word[::-1]))
        word.clear()
        result.append(' ')
    else:
        word.append(ch)

if word:
    result.append(''.join(word[::-1]))

print(''.join(result))
