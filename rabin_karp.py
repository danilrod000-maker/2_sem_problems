def my_strstr(haystack, needle):
    if needle == "":
        return -1

    n = len(haystack)
    m = len(needle)
    if m > n:
        return -1
    d = 256
    q = 101

    hash_needle, hash_haystack = 0, 0

    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    # Вычисляем хеш для needle и первого окна в haystack
    for i in range(m):
        hash_needle = (d * hash_needle + ord(needle[i])) % q
        hash_haystack = (d * hash_haystack + ord(haystack[i])) % q

    #cкользящее окно по строке haystack
    for i in range(n - m + 1):
        if hash_needle == hash_haystack:
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    break
            return i

        # Вычисляем хеш для следующего окна
        if i < n - m:
            hash_haystack = (d * (hash_haystack - ord(haystack[i]) * h) + ord(haystack[i + m])) % q

            if hash_haystack < 0:
                hash_haystack = hash_haystack + q
    return -1

print(my_strstr(input(),input()))
