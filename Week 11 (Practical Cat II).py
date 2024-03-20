import random

questionList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
#print(random.choices(questionList, weights=(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1), k=1))

choiceList = []
for i in range(1,29,1):
  k = random.choices(questionList, weights=(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1), k=1)
  choiceList.append(k)

#print(choiceList)
myChoice = random.choices(questionList, weights=(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1), k=1)
print(myChoice)

#\item In Kenya, we have $47$ counties. create a \textbf{list (named 'myList')} of $9$ counties four of which should be
# counties that have two names. From myList, create another list (named 'myOneList') of counties which have one name and
# another list (named 'myTwoList') which contains counties which have two names.