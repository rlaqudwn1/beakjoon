def solution(friends, gifts):
    friends_len = len(friends)
    friend_to_idx = {friend: idx for idx, friend in enumerate(friends)}
    
    friends_list = [[0] * friends_len for _ in range(friends_len)]
    gift_num = [0] * friends_len
    gift_list = [0] * friends_len

    for gift in gifts:
        sender, reciver = gift.split()
        idy = friend_to_idx[sender]
        idx = friend_to_idx[reciver]
        friends_list[idy][idx] += 1
        gift_num[idy] += 1
        gift_num[idx] -= 1

    for i in range(friends_len):
        for j in range(i+1, friends_len):
            if friends_list[i][j] > friends_list[j][i]:
                gift_list[i] += 1
            elif friends_list[i][j] < friends_list[j][i]:
                gift_list[j] += 1
            else:
                if gift_num[i] > gift_num[j]:
                    gift_list[i] += 1
                elif gift_num[i] < gift_num[j]:
                    gift_list[j] += 1

    answer = max(gift_list)
    return answer
