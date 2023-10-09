def has_valid_palindrome(s):
    def is_palindrome(sub):
        left, right = 0, len(sub) - 1
        while left < right:
            if sub[left] != sub[right]:
                return False
            left += 1
            right -= 1
        return True

    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if len(sub) > 1 and is_palindrome(sub):
                return True
    return False

s = input()
print(has_valid_palindrome(s))
