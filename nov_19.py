# QUESTION
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

#SOLUTION
string= input()
k = int(input())

def iterateRecusively(str_arr, substring = ""):
    counterElement = 0
    lenstr = 0
    substr = ""
    for var in str_arr:
        if var in substr:
            substr = substr + var
            lenstr += 1
        else:
            if counterElement >= k:
                str_arr.pop(0)
                if (len(substring) >= len(substr)):
                    pass
                else:
                    substring = substr
                return iterateRecusively(str_arr, substring)
            else:
                substr = substr + var
                lenstr += 1
                counterElement += 1
    if (len(substring) >= len(substr)):
        pass
    else:
        substring = substr
    return substring

print(iterateRecusively(list(string)))