def solution(readings):
    arrays_of_ones = readings.split('0')
    count = 1

    for i in range(len(arrays_of_ones) - 1):
        count = max(count,
                    len(arrays_of_ones[i] + arrays_of_ones[i+1]) + 1
                    )
    return count
