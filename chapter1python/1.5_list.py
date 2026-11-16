scores = [85, 92, 78, 95, 88]
print(scores)
scores.append(100)
print(scores)
scores.sort()
print(scores)

i = 0 
scores_new=[1,2,3,4,5,6]
while i<len(scores):
    scores_new[i]=scores[len(scores)-1-i]
    i=i+1
print(scores_new)