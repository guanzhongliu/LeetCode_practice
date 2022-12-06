'''
Given two strings a and b we need to add ith elements from both. Time limit 0.5secs (AFAIR). 
(Input size limits I do not remember)
Eg1:
a = "99"
b = "99"
ans = "1818"
Eg2:
a = "9"
b = "11"
ans = "110"
'''

def add_numbers(a :str, b :str):
    la = len(a)
    lb = len(b)
    if la < lb:
        a, b = b, a
        la, lb = lb, la
    ans = ""
    for i in range(1, la+1):
        if i <= lb:
            ans += str(int(a[-i]) + int(b[-i]))
        else:
            ans = a[-i] + ans
    return ans


print(add_numbers("99", "99"))
print(add_numbers("9", "11"))
print(add_numbers("99", "9"))
