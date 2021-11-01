import os 

clear = lambda: os.system("cls")

clear()

remainder= lambda num:num%2

print(remainder(5))

def testfunc(num):
    print(num)
    return lambda x: x* num

result10 = testfunc(10)
result100= testfunc(100)

#result10= lambda x:x*10
# print(result10(9))
# print(result100(9))




def myfunc(n):

    return lambda a: a*n 

mydoubler=myfunc(2)
mytripler=myfunc(3)


# print(mydoubler(2))


number_list = [2,6,8,10,11,14,4,2,5,6]

filter_list= list(filter(lambda num:(num>7), number_list))

# print(filter_list)

mapped_list= list(map(lambda num:num%2, number_list))

# print(mapped_list)

def addition(n):
    return n+n
numbers=[1,2,3,4]
result=map(addition,numbers)


print(list(result))

result=map(lambda n:n+n,numbers)

print(list(result))





