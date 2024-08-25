def print_n_to_1(n):

    #base case
    if n == 0:
        return
    
    #print(n)  #for ulta 

#recursive case
    print_n_to_1(n-1)
    print(n)
print(print_n_to_1(5))    