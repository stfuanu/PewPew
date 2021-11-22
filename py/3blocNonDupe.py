def merge_the_tools(string, k):
    # your code goes here
    # print(string,k)
    samosa = list(string)
    i=0
    lenn = len(samosa)
    bloc = []
    for x in samosa :
        i = i +1 
        if x not in bloc :
            bloc.append(x)
        if i == k or len(bloc) == k :
            print("".join(bloc))
            bloc.clear()
            i = 0
        
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
