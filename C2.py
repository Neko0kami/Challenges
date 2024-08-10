import re

def countSmileys(arr):
    count = 0
    smiles = r"[:;][-~]?[)D]"
    for i in arr:
        if re.search(smiles,i):
            count +=1
    print(count)
def main():
    test = [
        [";D", ":-(", ":-)", ";~)"],
        [":)", ";(", ";}", ":-D"],
        [";]", ":[", ";*", ":$", ";-D"]
    ]
    for i in test:
        countSmileys(i)

if __name__=="__main__":
    main()





    
    
    
