def checkValue(n):
    if n%2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
        
checkValue(7)

### Question 33
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.

Solution
​```python
def printDict():
    d=dict()
    d[1]=1
    d[2]=2**2
    d[3]=3**2
    print(d)
        
printDict()
