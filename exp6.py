L1=list(map(int,input("enter the 1st list of integer(space_seperated):").split()))
L2=list(map(int,input("enter the 2nd list of integer(space_seperated):").split()))
if len(L1)==len(L2):
    print("the rwo list are of the same length")
else:
    print("the two lists are not same length")
    if sum(L1)==sum(L2):
        print("the two lists sum is not same value")
    else:
        print("sum is not same")
common_value=set(L1).intersection(set(L2))
if common_value:
            print(f"common value between the lists:{common_value}")
else:
            print("no common values between the lists")
