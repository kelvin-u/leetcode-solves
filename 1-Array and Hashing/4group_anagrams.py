strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

# word map  key value sorted word: words

word_map = {}

for word in strs:
    sorted_word = "".join(sorted(word))
    if sorted_word not in word_map:
        word_map[sorted_word] = []
    word_map[sorted_word].append(word)

print(list(word_map.values()))
