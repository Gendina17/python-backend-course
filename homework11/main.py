import sys


def calculating_distance(string, pattern):
    distance = 0
    if len(string) > len(pattern):
        string, pattern = pattern, string

    while string != pattern:
        if len(string) != 0 and len(pattern) != 0 and string[0] == pattern[0]:
            string = string[1:]
            pattern = pattern[1:]
            continue
        if len(string) < len(pattern):
            pattern = pattern[1:]
        else:
            string = string[1:]
            pattern = pattern[1:]
        distance += 1
    if len(string) == 0:
        distance = distance + len(pattern)
    return distance


if __name__ == '__main__':
    calculating_distance(sys.argv[1], sys.argv[2])