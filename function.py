def erick():
    print("new to function")
    erick()

def add():
    num=int(input("Enter First Number:"))
    num2 = int(input("Enter Second Number"))
    print(f"sum of{num} and{num2} is {num+num2}")

def check_is_0dd_even():
    nambari=int(input("weka nambari"))
    if nambari %2==0:
        print(f"{nambari} is even")
    else:
        print(f"{nambari} is odd")

    check_is_0dd_even()


    add()