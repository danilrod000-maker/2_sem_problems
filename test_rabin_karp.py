from rabin_karp import my_strstr

haystack1 = "Hello, World!"
needle1 = "World"
result1 = my_strstr(haystack1, needle1)
assert result1 == 7

haystack2 = "Peuwr tututu"
needle2 = "Peu"
result2 = my_strstr(haystack2, needle2)
assert result2 == 0

haystack3 = "Python"
needle3 = "Python"
result3 = my_strstr(haystack3, needle3)
assert result3 == 0

haystack4 = "awer F"
needle4 = ""
result4 = my_strstr(haystack4, needle4)
assert result4 == -1

haystack5 = "SHHH"
needle5 = "as LKFLKalsfafddg"
result5 = my_strstr(haystack5, needle5)
assert result5 == -1

haystack6 = "Hello"
needle6 = "XYZ"
result6 = my_strstr(haystack6, needle6)
assert result6 == -1

haystack7 = "abcdef"
needle7 = "d"
result7 = my_strstr(haystack7, needle7)
assert result7 == 3

haystack8 = "ababababa"
needle8 = "aba"
result8 = my_strstr(haystack8, needle8)
assert result8 == 0

haystack9 = "a"
needle9 = "a"
result9 = my_strstr(haystack9, needle9)
assert result9 == 0

haystack10 = "Hello World"
needle10 = "world"
result10 = my_strstr(haystack10, needle10)
assert result10 == -1



haystack11 = "a"
needle11 = "b"
result11 = my_strstr(haystack11, needle11)
assert result11 == -1







print(my_strstr("Hello, World!", "World"))  # 7
print(my_strstr("Python", "Py"))  # 0
print(my_strstr("abcdef", "xyz"))  # -1
print(my_strstr("test", ""))  # -1
print(my_strstr("a", "abc"))  # -1