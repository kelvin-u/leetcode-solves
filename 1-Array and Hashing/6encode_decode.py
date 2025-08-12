strs = ["i", "love", "you"]
output = ["i", "love", "you"]


def encode(strs):
    s = ""
    for word in strs:
        word_length = str(len(word))
        s += word_length + "#" + word


s = "5#idiot4#love3#you"


def decode(s):
    output = []
    i = 0
    while i < len(s):
        j = i
        # basiaclly use j to find where the last digit of the number is
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        output.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length
    print(output)

decode(s)
