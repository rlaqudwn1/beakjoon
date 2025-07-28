def solution(cacheSize, cities):
    cache = []
    answer = 0

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()  # 대소문자 구분하지 않는 경우

        if city in cache:  # 캐시 히트
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:              # 캐시 미스
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
            answer += 5

    return answer
