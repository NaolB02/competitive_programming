n = int(input())
value = {"S" : 1, "M" : 2, "L" : 3}

for _ in range(n):
    size1, size2 = input().split()
    
    # checks whether the last size indicators are the same or not
    if size1[-1] != size2[-1]:
        # assigns the order of the size indicators as stated in the dictionary
        ord1 = value[size1[-1]]
        ord2 = value[size2[-1]]

        # compares the two orders
        if ord1 > ord2:
            print(">")
        
        elif ord1 < ord2:
            print("<")

    else:
        # checks whether the size indicator is S or L
        # if the indicator is S, then the one with many X will be of lower order
        if size1[-1] == "S":
            len1 = len(size1)
            len2 = len(size2)

            if len1 > len2:
                print("<")

            elif  len1 < len2:
                print(">")
            
            else:
                print("=")
        
        # if the indicator is L, then the one with many X will be of higher order
        elif size1[-1] == "L":
            len1 = len(size1)
            len2 = len(size2)

            if len1 > len2:
                print(">")

            elif  len1 < len2:
                print("<")
            
            else:
                print("=")

        else:
            print("=")
