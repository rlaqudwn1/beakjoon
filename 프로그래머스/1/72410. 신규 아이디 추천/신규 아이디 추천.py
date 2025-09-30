def solution(new_id):
    # 1단계
    new_id = new_id.lower() 

    two = []
        #2단계
    for char in new_id: 
        if char.isalpha() or char.isdigit() or char in ['.', '-', '_']:
            two.append(char)
    #3단계
    three = []
    for char in two:
        if not (char == '.' and three and three[-1] == '.'):
            three.append(char)
    #4단계
    if three and three[0] == '.':
        del three[0]

    if three and three[-1] == '.':
        three.pop()
    #5단계
    if not three:
        three.append('a')
    #6단계
    if len(three)>= 16:
        three = three[:15]
        if three[-1]=='.':
            three.pop()
    while(len(three)<3):
        three.append(three[-1])
            
    answer="".join(three)
    return answer