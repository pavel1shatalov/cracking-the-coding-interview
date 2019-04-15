def palindrome_permutation(string):
    if string is None:
        return True
    bit_vector = [False]*26
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            bit_vector[ord(char) - ord('a')] = not bit_vector[ord(char) - ord('a')]
        if ord('A') <= ord(char) <= ord('Z'):
            bit_vector[ord(char) - ord('A')] = not bit_vector[ord(char) - ord('A')]
    return sum(bit_vector) <= 1

print(palindrome_permutation(input()))