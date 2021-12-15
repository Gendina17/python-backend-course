import sys


def calculating_distance(string, pattern):
    if string == pattern:
        return 0

    matrix = [[0 for j in range(len(pattern)+1)] for i in range(len(string)+1)]
    matrix[0] = [i for i in range(len(pattern)+1)]
    for j in range(len(string)+1):
        matrix[j][0] = j

    for string_index in range(1, len(string)+1):
        for pattern_index in range(1, len(pattern)+1):
            additional_value = 0 if string[string_index-1] == pattern[pattern_index-1] else 1
            matrix[string_index][pattern_index] = min([
                matrix[string_index - 1][pattern_index] + 1, matrix[string_index][pattern_index - 1] + 1,
                matrix[string_index - 1][pattern_index - 1] + additional_value
            ])
    return matrix[-1][-1]


if __name__ == '__main__':
    calculating_distance(sys.argv[1], sys.argv[2])
