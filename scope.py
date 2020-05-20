##############Inherit function ############

# def sc():
#     y=x
#     print(y)

# x=7
# sc()    


###########global 
x=200
def sc():
    global x
    x=3000

sc()
print(x)