n = int(input())
hashtags = []

for i in range(n):
    hashtag = input()
    if hashtag.lower() == hashtag:
        hashtags.append(hashtag)

for i in range(len(hashtags)):
    for j in range(i+1, len(hashtags)):
        if hashtags[i] > hashtags[j]:
            hashtags[i], hashtags[j] = hashtags[j], hashtags[i]

for hstg in hashtags:
    print(hstg)