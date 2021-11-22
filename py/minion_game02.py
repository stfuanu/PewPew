def minion_game(string):
    # your code goes here
    Stuart = 0
    Kevin = 0
    strr =  list(string)
    strrlen = len(strr)
    # Sstrr = strr.copy()
    # Kstrr = strr.copy()
    
    # print(strr)
    vow = ["A","E","I","O","U"]
    # index_tarrlist = []

    # ['B', 'A', 'N', 'A', 'N', 'A']
    
    # comment : https://www.hackerrank.com/challenges/the-minion-game/forum/comments/663364
    # timed out :/
    i = 0
    
    # wused = list(set(strr))
    for letter in strr :
        # letter = len
        # // kevin :
        if letter in vow :
            # Index_Target_Letter = strr.index(letter)
            # target_list = 
            # for i in range(len(target_list)) :
            # // need nothing xuz , possible substr(in order) string is it's length
            # Kevin = Kevin + len(strr[i:])
            Kevin = Kevin + (strrlen-i)                   
            # // change the string so we don't find the same letter/at index again
            # but takes time , changed evrythinG fuuu
            # strr = strr[Index_Target_Letter+1:]
            # print(target_list,Kevin)
        elif letter not in vow :
            # Index_Target_Letter = strr.index(letter)
            # target_list = strr[Index_Target_Letter:]
            # for i in range(len(target_list)) :
            # // need nothing xuz , possible substr(in order) string is it's length
            # Stuart = Stuart + len(strr[i:])
            Stuart = Stuart + (strrlen-i)
            # // change the string so we don't find the same letter/at index again
            # strr = strr[Index_Target_Letter+1:]
            # print(target_list,Kevin)   
        
        i = i+1
    
    if Stuart > Kevin :
        print("Stuart",Stuart)
    elif Stuart < Kevin :
        print("Kevin",Kevin)
    elif Stuart == Kevin :
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
