def get_time(times):
    if(times% 100 >=50):
        return times+50
    else:
        return times+10
def solution(schedules, timelogs, startday):
    arrive=[]
    arrive.clear()
    answer = 0

    for i in schedules:
        arrive.append(get_time(i))
    peoples= len(schedules)
    now_day=0
    check=True
    for i in range(peoples):
        #평일일 경우
        for j in range(7):
            now_day=startday+j
    # 토요일과 일요일의 출근시간은 영향 X % 7 = 6 or 0 은 해당하지않음,
            if not (now_day%7==0 or now_day%7==6):
                if(timelogs[i][j]<=arrive[i]):
                    check=True
                else:
                    check=False
                    break
        if check:
            answer+=1
        check==False

            
    return answer