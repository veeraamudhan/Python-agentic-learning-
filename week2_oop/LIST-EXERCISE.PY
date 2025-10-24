#List  
  
# Empty list  
my_list = []  
  
# List with values  
fruits = ["apple", "banana", "mango"]  
numbers = [10, 20, 30, 40]  
mixed = [1, "Veera", 3.14, True]  
  
print(fruits)  
print(numbers)  
print(mixed)  
#Output  
#['apple', 'banana', 'mango']  
#[10, 20, 30, 40]  
#[1, 'Veera', 3.14, True]  
  
  
  
fruits = ["apple", "banana", "mango","a","b"]  
  
print(fruits[0])   # first element  
print(fruits[-1])  # last element  
print(fruits[0:2]) # slice (first two elements)  
print(fruits[2:4])  
#Output  
#apple  
#b  
#['apple', 'banana']  
#['mango', 'a']  
  
  
  
fruits = ["apple", "banana","a","b","c","d"]  
print(fruits)  
fruits.append("mango")     
     # add at end  
print(fruits)  
fruits.insert(1, "orange")    # insert at index 1  
print(fruits)  
fruits.insert(4, "o")  
print(fruits)  
fruits.extend(["grapes", "kiwi"]) # add multiple  
print(fruits)  
fruits.pop()  
print(fruits)  
fruits.remove("o")  
print(fruits)  
  
#Output  
  
#['apple', 'banana', 'a', 'b', 'c', 'd']  
#['apple', 'banana', 'a', 'b', 'c', 'd', 'mango']  
#['apple', 'orange', 'banana', 'a', 'b', 'c', 'd', 'mango']  
#['apple', 'orange', 'banana', 'a', 'o', 'b', 'c', 'd', 'mango']  
#['apple', 'orange', 'banana', 'a', 'o', 'b', 'c', 'd', 'mango', 'grapes', 'kiwi']  
#['apple', 'orange', 'banana', 'a', 'o', 'b', 'c', 'd', 'mango', 'grapes']  
#['apple', 'orange', 'banana', 'a', 'b', 'c', 'd', 'mango', 'grapes']  
  
  

  
numbers = [10, 20, 30, 10, 40]  
  
print(fruits.count("a"))  # count occurrences  
print(fruits.index("orange"))  # index of element  
numbers.sort()            # sort ascending  
print(numbers)  
numbers.reverse()         # reverse order  
print(numbers)  
fruits.reverse()  
print(fruits)  
fruits.sort()  
print(fruits)  
print(numbers)  
  
#OUTPUT  
#1  
#1  
#[10, 10, 20, 30, 40]  
#[40, 30, 20, 10, 10]  
#['grapes', 'mango', 'd', 'c', 'b', 'a', 'banana', 'orange', 'apple']  
#['a', 'apple', 'b', 'banana', 'c', 'd', 'grapes', 'mango', 'orange']  
#[40, 30, 20, 10, 10]  
  
  
  
  
  
fruits = ["apple", "banana", "mango","a","b","c"]  
  
for fruit in fruits:  
    print(fruit)  
  
# Using index  
for i in range(len(fruits)):  
    print(i, fruits[i])  
  
'''apple  
banana  
mango  
a  
b  
c  
0 apple  
1 banana  
2 mango  
3 a  
4 b  
5 c  '''
  
  
'''✅ Mini Challenge  
  
1. Create a list of 5 clients’ names.  
  
  
2. Add 2 more clients.  
  
  
3. Remove the first client.  
  
  
4. Print all clients using a for loop.  '''
  
client_list = ["Veera","aathi","ezhil","kanmani"]  
  
print(client_list)  
  
client_list.append("Amudhan")  
  
print(client_list)  
  
client_list.insert(2, "nanmaran")  
  
print(client_list)  
  
client_list.remove("Veera")  
print(client_list)  
  
  
for client in client_list:  
    print(client)  
  
# Using index  
for i in range(len(client_list)):  
    print(i, client_list[i])  
  
  
'''['Veera', 'aathi', 'ezhil', 'kanmani']  
['Veera', 'aathi', 'ezhil', 'kanmani', 'Amudhan']  
['Veera', 'aathi', 'nanmaran', 'ezhil', 'kanmani', 'Amudhan']  
['aathi', 'nanmaran', 'ezhil', 'kanmani', 'Amudhan']  
aathi  
nanmaran  
ezhil  
kanmani  
Amudhan  
0 aathi  
1 nanmaran  
2 ezhil  
3 kanmani  
4 Amudhan  
  '''
