if __name__ == '__main__':
    strlist = list(set(input()))
    # print("%r \n%r \n%r \n%r \n%r" % (s.isalnum(),s.isalpha(),s.isdigit(),s.islower(),s.isupper()))
    # questions has "ANY"
    # print(any(x.isalnum()  for x in ss))
    
    # Ref Thread : https://www.hackerrank.com/challenges/string-validators/forum/comments/346845
    
    # any() is a core library function in Python. 
    # It returns true if at least one value in the sequence is true. 
    # It returns as soon as it finds the first true value.
    
    # prefer just using function references. 
    # Remember that class methods are just functions with an object as the first parameter 
    # - true in any OO language but directly visible and usable from Python.
    
    # objtype ke jagah str/int Ya type(int/str/list/map.dict) bhi koi var main define kr sakte hain
    # but methods uspr lagu hone chahiye shayad maybe like we used methods of str , 
    # to list ke liye list wale methods (obj.sort()) krna padega
    
    objtype=type(strlist[0])
    for Methods_Are_funcs_With_An_Obj_As_1st_Param in [objtype.isalnum, objtype.isalpha, objtype.isdigit, objtype.islower, objtype.isupper] :
        # print(any(x.isalnum()  for x in ss))
        print(any(Methods_Are_funcs_With_An_Obj_As_1st_Param(strelement) for strelement in strlist ))
