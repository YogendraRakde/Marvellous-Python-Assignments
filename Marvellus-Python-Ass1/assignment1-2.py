def ChkNum(x):
    if x%2==0:                             # if the number is divisible by 2 then its even
        print("number is Even")
    else:
        print("number is Odd")

def Display():
    print("Enter the number:")
    a=int(input())
    ChkNum(a)


if __name__=="__main__":
    Display()
