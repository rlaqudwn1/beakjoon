def is_valid(structures):
    for x, y, kind in structures:
        if kind == 0:  # 기둥
            if (
                y == 0 or  # 바닥 위
                (x, y - 1, 0) in structures or  # 아래 기둥
                (x - 1, y, 1) in structures or  # 왼쪽 보 끝 위
                (x, y, 1) in structures         # 오른쪽 보 끝 위
            ):
                continue
            return False
        else:  # 보
            if (
                (x, y - 1, 0) in structures or          # 왼쪽 끝 아래 기둥
                (x + 1, y - 1, 0) in structures or      # 오른쪽 끝 아래 기둥
                (
                    (x - 1, y, 1) in structures and
                    (x + 1, y, 1) in structures         # 양쪽 보 연결
                )
            ):
                continue
            return False
    return True

def solution(n, build_frame):
    structures = set()

    for x, y, kind, op in build_frame:
        structure = (x, y, kind)
        if op == 1:  # 설치
            structures.add(structure)
            if not is_valid(structures):
                structures.remove(structure)
        else:  # 삭제
            structures.remove(structure)
            if not is_valid(structures):
                structures.add(structure)

    answer = sorted(structures, key=lambda x: (x[0], x[1], x[2]))
    return answer
