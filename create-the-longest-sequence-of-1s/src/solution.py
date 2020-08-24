import pdb


def solution(readings="01010"):
    chars = [char for char in readings]

    max_sequ = 1
    count = 1
    flip_used = False
    flip_used_index = -1

    for i in range(len(chars)):
        if chars[i] == "1":
            pdb.set_trace()
            count += 1
            max_sequ = max(count, max_sequ)
            continue
        if i + 1 < len(chars):
            pdb.set_trace()
            if (chars[i + 1] == "1"):
                if count > 0:
                    if not flip_used:
                        flip_used = True
                        flip_used_index = i
        else:
            pdb.set_trace()
            if flip_used_index >= 0 and flip_used:
                i = flip_used_index
            count = 1
            flip_used = False

    return max_sequ
