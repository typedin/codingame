def dictFromLength(measurements):
    measurements.insert(0, 0)
    result = dict()

    for i, num_a in enumerate(measurements):
        for num_b in measurements[i:]:
            length = num_b - num_a
            if length in result.keys():
                result[length] += 1
            else:
                result.update({length: 1})

    del result[0]

    return result


def solution(lines):
    x_lengths = [int(num) for num in lines[1].split()]
    x_lengths.append(int(lines[0].split()[0]))

    y_lengths = [int(num) for num in lines[2].split()]
    y_lengths.append(int(lines[0].split()[1]))

    dict_x = dictFromLength(x_lengths)
    dict_y = dictFromLength(y_lengths)

    square_nb = 0
    for y_key in dict_y.keys():
        if y_key in dict_x.keys():
            square_nb += dict_y[y_key] * dict_x[y_key]

    return square_nb
