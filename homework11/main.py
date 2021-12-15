import sys


def calculating_distance(string, pattern):
    if string == pattern:
        return 0
    string = ' ' + string
    pattern = ' ' + pattern
    width = len(string)
    height = len(pattern)
    matrix = [[0 for j in range(height)] for i in range(width)]
    matrix[0] = [i for i in range(height)]
    for j in range(width):
        matrix[j][0] = j
    print(matrix)

    for string_index in range(1, width):
        for pattern_index in range(1, height):
            additional_value = 0 if string[string_index] == pattern[pattern_index] else 1
            matrix[string_index][pattern_index] = sorted([
                matrix[string_index - 1][pattern_index] + 1, matrix[string_index][pattern_index - 1] + 1,
                matrix[string_index - 1][pattern_index - 1] + additional_value
            ])[0]
    print(matrix)
    print(matrix[-1][-1])
    return matrix[-1][-1]


if __name__ == '__main__':
    # calculating_distance(sys.argv[1], sys.argv[2])
    calculating_distance('машка', 'миша')
