def solution(angle):
    if 0 < angle < 90: return 1
    elif angle == 90: return 2
    elif 180 > angle > 90: return 3
    elif angle == 180: return 4