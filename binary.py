def bsearch(seq,v,l,r):
    if (r-l)==0:
        return False

    mid=(l+r)//2

    if (v==seq[mid]):
        return True

    if (v<seq[mid]):
            return(bsearch(seq,v,l,mid)) 

    else:
            return((seq,v,mid+1,r))


a=[1,2,3,4,6,7,8,9]
b=13
l=1
r=9

print(bsearch(a,b,l,r))

# def binary(seq,v,l,r):
#     if (r-l)==0:
#         return False
#     mid=(l+r)//2

#     if (v==seq[mid]):
#         return True

#         if (v > seq[mid]):
#             return(binary(seq,v,mid+1),r) 

#         else:
#             return (binary(seq),v,l,mid)


# a=[1,2,3,5,9,10,15,16,19]
# b=9
# l=1
# r=9

# print(binary(a,b,l,r))
