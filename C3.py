def waldo(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
       
          if arr[0][0] == arr[0][1]:
              not_waldo = arr[0][0]
          else:
              not_waldo = arr[0][2]
    find_waldo(arr,not_waldo)
    


def find_waldo(arr,a):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != a:
                print(f"Waldo found at ({i+1}, {j+1})")
                return
    print("Waldo not found")

def main():
    test =[
      [
        ["A", "A", "A"],
        ["A", "A", "A"],
        ["A", "B", "A"]
      ],
      [
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"],
        ["O", "O", "O", "O"],
        ["P", "O", "O", "O"],
        ["O", "O", "O", "O"]
      ],
      [
        ["c", "c", "c", "c"],
        ["c", "c", "c", "d"]
      ]
    ]
    for i in test:
        waldo(i)
    

if __name__=="__main__":
    main()
