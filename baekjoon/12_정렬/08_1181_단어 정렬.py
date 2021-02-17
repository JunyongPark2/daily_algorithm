N = int(input())
words = []
for _ in range(N):
    word = input()
    if word not in words:
        words.append(word)
sorted_words = sorted(words, key=lambda x : (len(x),x))
for word in sorted_words:
    print(word)