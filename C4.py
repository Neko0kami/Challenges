# programme to convert minutes to seconds

def minutesToSeconds(min):
    # creating array
    arr = min.split(":")
    if int(arr[-1]) >= 60:
        print(-1)
    else:
        #converting min into sec
        print(f"{min} is {(int(arr[0]) * 60) + int(arr[-1])} seconds")

def main():
    #Tests
    test = ["01:00","13:56","10:60","121:49"]

    for i in test:
        minutesToSeconds(i)

if __name__ =="__main__":
    main()

