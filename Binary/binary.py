def ifBinary(a,b):
    dict = {}

    # Range doesn't include the second value
    for n in range(a,b):
        # Converting into Binary using Standard Functions
        x = bin(n).replace('0b','')
        # Using this function, it starts with 0b, so replace with empty string

        list = []

        # To add individual values of the bin number to the list
        for d in x:
            list.append(int(d))

        # Checking the necessary condition
        for i in range(0, len(list) - 1): # As indexing starts from 0 and not 1 
            if ((int(list[i]) and int(list[i+1])) == 1):
                result = True
                break
            else:
                result = False
            i+=1

        # Assigning the value to the key in the dictionary
        dict[n] = result
    print(dict)
    return dict