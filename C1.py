# Checkin if the capitalized list is equal to the original
def check_title(s):
    global copy
    copy = s.split()
    if capitalize(copy) == copy:
        print("True")
    else:
        print ("False")   

# Capitalizing first letter of every element in list 
def capitalize(n):
    for i in copy:
        lst.append(i.capitalize())
    return lst

lst = []
  
s = input("Enter a string: ")
check_title(s)
