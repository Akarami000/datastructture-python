
# def findpos(l,v):

#     (found,i)=(False,0)
#     while i<len(l):
#        if not found and l[i]==v:
#            (found,i)=(True,i)
#        if not found:
#            pos=-1
#         return (pos)            


# a=[3,5,6,9,2,0]
# d=6
# print(findpos(a,d))


# def findpos(v,l):
    
#     for i in range(len(l)):
#         if l[i]==v:
#             pos=i
#             break
#         else:
#             pos=-1 

#     return(pos)

# a=4
# b=[3,5,7,4,8,2]
# print(findpos(a,b))



def findpos(v,l):
    for i in range(len(l)):
        if l[i]==v:
            pos=i
            break
        else:
            pos=-1
        
    return(pos)

a=4
b=[3,5,6,7,8,9,4]

print(findpos(a,b))

