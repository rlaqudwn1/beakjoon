# 각 종류별로 최대 1가지 의상만 착용할 수 있다. 동그란 안결과 검정 선글라스를 동시에 착용할 수 없다.
# 착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법?
def solution(clothes):
    group_items={}
    answer=1
    for item, category in clothes:
        if category not in group_items:
            group_items[category]=0
    # 기존 옷들을 종류별로 딕셔너리에 종류별로 개수를 저장
        group_items[category]+=1
    # 각 옷들의 종류+1 (입지 않을 경우) * 다른옷들의 종류 = 전체 조합 +1 (모두 안입는 경우)
    for i in group_items.values():
        answer = (i+1) * answer
    
    return answer-1 # 모두 안입는 경우를 뺀 전체 집합 반환