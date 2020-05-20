# def lcw(u,v):
#     for r in range(len(u)+1):
#         lcw[r][len(v)+1]=0
#     for c in range(len(v)+1):
#         lcw[len(u)+1][c]=0
#     maxLCW=0

#     for c in range(len(v)+1,-1,-1):
#         for r in range(len(u)+1,-1,-1):
#             if u[r] == v[c]:
#                 lcw[r][c]=1+lcw[r+1][c+1]
#             else:
#                 lcw[r][c]=0
#             if lcw[r][c] > maxLCW:
#                 maxLCW=lcw[r][c]

#     return(maxLCW)


####################################dp

def lcs(u,v):
    for r in range(len(u)+1):
       lcs [r][len(v)+1]
    for c in range(len(v)+1):
        lcs[len(u)+1][c]

    for c in range(len(v),-1,-1):
        for r in range(len(u),-1,-1):
            if (u[r]== v[c]):
                lcs[r][c]=1+lcs[r+1][c+1]
            else:
                lcs[r][c]=max(lcs[r+1][c],lcs[r][c+1])

    return (lcs[0][0])            




       
