
def check_title(s):
    count = 0
    str = ""
    copy = s.split()
    
    for i in copy:
        x = str.join(i)
        
        if x[0] in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            count += 1
        else:
            break
            
    if count == len(copy):
        print("True")
    else:
        print("False")
  
s = input("Enter a string: ")
check_title(s)


    
