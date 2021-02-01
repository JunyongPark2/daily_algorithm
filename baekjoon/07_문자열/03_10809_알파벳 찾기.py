S = input()
for i in range(97, 123):
    # .find() method는 없을시 -1 return, .index()는 없을시 에러발생
    print(S.find(chr(i)), end=" ")