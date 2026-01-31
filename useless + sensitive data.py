print("Cows eat monkeys")
sensitivedata = {"name": "James Shirefeld", "Social Security #": "132-53-6421", "Credit Card Number": "1324 4586 5364 5732", "Address": "432 Ridge St, OH, USA"}
#DO NOT LEAK THIS DATA
def protectdata():
  repetition = 0
  while repetition < 200:
    print(sensitivedata)
    repetition = repetition + 1
print("oops")
