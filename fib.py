import time
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b, a+b
    
    
# to print first 100 fibonacci number
g=fib()
# for x in g:
#     if x > 100:
#         break
#     print(x)
#     time.sleep(1)

# to print firsy 5 fib numbers

# count=1
# n=int(input('enter the first 5 numbrs of fib :'))
# for x in g:
#     if count>10:
#         break
#     print(x)
#     count=count+1
#     time.sleep(1)


#  to print n number of values in fib serioes


# count=1
# n=int(input('enter the first 5 numbrs of fib :'))
# for x in g:
#     if count> n :
#         break
#     print(x)
#     count=count+1
#     time.sleep(1)


# to in between 25 to 75 fib series numbers
for x in g:
    if x > 25 and x < 75:
        print(x)
        
        if x > 75:
            break
        time.sleep(1)
        

