from collections import deque

def word_ladder_simple(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    queue = deque([[beginWord]])
    result = []
    visited = set([beginWord])
    found = False

    while queue and not found:
        level_visited = set()

        for _ in range(len(queue)):
            path = queue.popleft()
            last = path[-1]

            if last == endWord:
                result.append(path)
                found = True

            for i in range(len(last)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = last[:i] + ch + last[i+1:]

                    if new_word in wordSet and new_word not in visited:
                        level_visited.add(new_word)
                        queue.append(path + [new_word])

        visited.update(level_visited)

    return result
