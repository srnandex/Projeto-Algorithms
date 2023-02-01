def merge(left, right, string):

    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            string[left_idx + right_idx] = left[left_idx]
            left_idx += 1
        else:
            string[left_idx + right_idx] = right[right_idx]
            right_idx += 1

    for left_idx in range(left_idx, len(left)):
        string[left_idx + right_idx] = left[left_idx]

    for right_idx in range(right_idx, len(right)):
        string[left_idx + right_idx] = right[right_idx]

    return string


def merge_sort(string):
    if len(string) <= 1:
        return string
    mid = len(string) // 2
    left, right = merge_sort(string[:mid]), merge_sort(string[mid:])
    return merge(left, right, string.copy())


def is_anagram(first_string, second_string):

    first = "".join(merge_sort(list(first_string.lower())))
    second = "".join(merge_sort(list(second_string.lower())))

    if first_string == "" and second_string == "":
        anagram_is = False
    else:
        anagram_is = first == second
    return (first, second, anagram_is)
