# For 2 given strings
# take the min of the last 3 values(above current number, before, above and before)

# str_1: 'bao', str_2: 'cab
#       b  a  o
#    0  1  2  3
# c  1  1  2  3
# a  2  2  1  2
# b  3  2  2  2

# Example with this matrix:
# give each letter a number
# start iterating:
#   - look at precedent values, here 0,1,1, take the smallest, see if b and c are different, if so add 1 to 0
#   - continue iteration, the last number is the levenshtein distance
#       b  a  o           b  a  o           b  a  o               b  a  o
#    0  1  2  3        0  1  2  3        0  1  2  3            0  1  2  3
# c  1              c  1(0+1)         c  1  1(1+1)   (...)  c  1  1  2  3
# a  2              a  2              a  2                  a  2  2(1+0)
# b  3              b  3              b  3                  b  3

#  clear explanation here: https://stackabuse.com/levenshtein-distance-and-text-similarity-in-python/


def levenshtein(str_1: str, str_2: str) -> int:
    """
    Function to calculate the levenshtein distance.
    with a matrix from the 2 strings, calculates the difference of each substring.
    """
    if len(str_1) == 0:
        return len(str_2)
    if len(str_2) == 0:
        return len(str_1)
    m = []
    if len(str_2) > len(str_1):
        str_1, str_2 = str_2, str_1

    for i in range(len(str_1) + 1):
        # Initialise the matrix
        if i == 0:
            m.append([j for j in range(len(str_2) + 1)])
            continue
        m.append([i] + [0] * len(str_2))
        # Fill the matrix
        for j in range(len(str_2) + 1):
            if j == 0:
                continue
            last_min = min(m[i-1][j], m[i][j-1], m[i-1][j-1])
            if str_1[i - 1] == str_2[j - 1]:
                m[i][j] = last_min
            else:
                m[i][j] = last_min + 1

    return m[len(str_1)][len(str_2)]
