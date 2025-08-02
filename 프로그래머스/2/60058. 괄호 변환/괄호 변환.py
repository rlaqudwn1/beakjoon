# 올바른 괄호 문자열인지 확인하는 함수
def correct(p):
    stack=[]
    for ch in p:
        if(ch==')'):
            if not stack:
                return False
            else:
                stack.pop()
        else:
            stack.append(ch)
    return True
def reverse(p):
    answer=""
    for i in p:
        if i=='(':
            answer+=')'
        else:
            answer+='('
    return answer
def solution(p):
    answer=""
    if correct(p):
        return p
    # 1.입력이 빈 문자열인 경우 빈 문자열을 반환한다
    if not p:
        return ""
    #2. 문자열 w를 두 균형잡힌 문자열 u,v 로 분리 u 는 균형잡힌 괄호 문자열로 더 이상 분리될 수 없어야 하며, v는 빈 문자열이 될 수 있다.
    left =0
    right=0
    u=""
    v=""
    for i in range(len(p)):
        if(p[i]=='('):
            u+=p[i]
            left+=1
        else:
            u+=p[i]
            right+=1
        if(left and right and(left==right)):
            v=p[i+1:]
            print(f"u:{u}, v:{v}")
            #3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
            if(correct(u)):
            #3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
                return u+solution(v)
            else:
                #4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
                blank=""
                blank+="("
                blank+=solution(v)
                blank+=")"
                return blank+reverse(u[1:-1])
    return answer
