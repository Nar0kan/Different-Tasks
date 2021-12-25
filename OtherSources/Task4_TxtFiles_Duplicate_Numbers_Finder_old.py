# Initialization of variables
file1 = open('task_4.txt', 'r')
spisok = []
k = 0
p = 0
amount = 0

# Input in list numbers from .txt file
for i in file1:
    spisok.append(i[:-1])
    k+=1
file1.close()
new_spisok = spisok

#First output 
print("Загальна кількість елементів: ", k)
#print(spisok)

# Looping through numbers in the list to find same one's
while p < k:
    for t in range (0, k):
        if int(new_spisok[p]) == int(new_spisok[t]) and p!=t:
            #print(new_spisok[p])
            amount +=1
            del new_spisok[t]
            k-=1
            break
    p+=1

file2 = open('task_4_result.txt', 'w')

# Ordering output loop (bubble method)
for i in range(0, k):
    for j in range(0, k-1):
        if len(new_spisok[j]) == len(new_spisok[j+1]):
            if new_spisok[j] > new_spisok[j + 1]:
                new_spisok[j], new_spisok[j + 1] = new_spisok[j + 1], new_spisok[j]
        elif len(new_spisok[j]) > len(new_spisok[j+1]):
            new_spisok[j], new_spisok[j + 1] = new_spisok[j + 1], new_spisok[j]

# Saving data to file2
for i in range(0, k):
    file2.writelines(new_spisok[i])
    file2.writelines('\n')

file2.close()

# Output the result
print("Кількість елементів, що повторюються: ", amount)
#print(new_spisok)