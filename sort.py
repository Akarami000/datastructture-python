#selection sort#########################################3333333
# def selectionsort(l):
#     for start in range(len(l)):
#         minpos=start

#         for i in range(start,len(l)):
#             if l[i]<l[minpos]:
#                 minpos=i

#         (l[minpos],l[start])=(l[start],l[minpos])
#     return(l)


# a=[12,45,76,89,32,78,56]
# print(selectionsort(a))                


##############insertion sort#########################33

# def insertionsort(l):
#     for slicend in range(len(l)):

#         pos = slicend
#         while pos>0 and l[pos]<l[pos-1]:
#             (l[pos],l[pos-1])=(l[pos-1],l[pos]) 
#     return l

# a=[21,78,56,54,43,79] 
# print(insertionsort(a))           

###################################