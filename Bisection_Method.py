def fcn(c):
    return c**4 - c - 10
def abss(n):
    if(n>0):
        return n;
    else:
        return -n;
term = 0.0001
a = 1
b = 2
c = 1.5
count = 0;
while(abss(fcn(c)) > term):
    print(count," : ",int(10000*a),int(10000*b),int(10000*c))
    if(fcn(c)*fcn(a) < 0):
        b = c;
    else:
        a = c;
    count += 1
    c = (a + b) / 2


print("The root of the system with termination scalar 0.001 is" , fcn(1.856))
