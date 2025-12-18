def findSubstring(s, words):
    if not s or not words:
        return []

    word_len = len(words[0])
    total_len = word_len * len(words)
    result = []

    for i in range(len(s) - total_len + 1):
        temp = words.copy()
        j = i

        while temp:
            word = s[j:j + word_len]
            if word in temp:
                temp.remove(word)
                j += word_len
            else:
                break

        if not temp:
            result.append(i)

    return result

# ---- Input ----
s = "barfoothefoobarman"
words = ["foo", "bar"]

# ---- Output ----
print(findSubstring(s, words))