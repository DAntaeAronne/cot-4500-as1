import math
from decimal import Decimal

#1

def truncate(number, digits) -> float:
    nbDecimals = len(str(number).split('.')[1]) 
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper



MN = "010000000111111010111001"
s = 0
exp = [0] * 11
expCount = 0
mant = [0] * 52
mantCount = 0
c = 0
f = 0
    
for el in range(0,len(MN)):
    if el == 0:
        s = int(el)
    elif el in range (1, 12):
        exp[expCount] = int(MN[el])
        expCount += 1
    else:
        mant[mantCount] = int(MN[el])
        mantCount += 1

i = 10
for num in exp:
    c += num * (2 ** i)
    i -= 1

i = 1
for num in mant:
    if num == 1:
        f += 1 * ((1/2) ** i)
    i += 1
    
val = ((-1) ** s) * (2 ** (c - 1023)) * (1 + f)
 
if len(str(val).split('.')[1]) > 5:
    print(f"{val:.5f}\n")
else:
    print(f"{val}\n")

#2 and 3
dec = len(str(int(val)))
if val < 0:
    dec -= 1
decVal = val / (10 ** dec)

#2
chopVal = truncate(decVal, 3) * (10 ** dec)
print(f"{chopVal}\n")

#3
roundVal = round(decVal, 3) * (10 ** dec)
print(f"{roundVal}\n")

#4
absErr = abs(Decimal(val) - Decimal(roundVal))
print(f"{absErr}")
relErr = Decimal(absErr) / abs(Decimal(val))
print(f"{relErr}\n")

#5
Err = 0
approx = 0
tolerance: float = 10 ** (-4)
k = 1
x = 1
iteration_counter = 0
min_check = 0

func = "(-1**k) * (x**k) / (k**3)"
if "(-1**k) * " in func:
    func = func.replace("(-1**k) * ", "")

if "/ (k**" in func:
    temp = func
    kExp = temp[temp.rindex("**") + 2]
    remPort = "/ (k**" + kExp + ")"
    func = func.replace(remPort, "* k")
    decToExp = (len(str(tolerance).replace("0.",""))) / float(kExp)
    tolerance = 10 ** decToExp

if x == 1:
    func = func.replace("(x**k) * ","")

if func == "k":
    tolerance -= 1

iteration_counter = round(tolerance)
print(f"{iteration_counter}\n")

#6a

tolerance: float = 10 ** (-4)
a = -4
b = 7
i = 0
def f(x) -> float:
    return (x**3) + (4*x**2) - 10

while abs(b - a) > tolerance:
    i += 1
    p = (a + b) / 2

    if (f(a) < 0 and f(p) > 0) or (f(a) > 0 and f(p) < 0):
        b = p
    else:
        a = p

print(f"{i}\n")

#6b
def custom_derivative(value):
    return (3 * value* value) + (8 * value)


def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):
    # remember this is an iteration based approach...
    iteration_counter = 0

    # finds f
    x = initial_approximation
    f = eval(sequence)

    # finds f' 
    f_prime = custom_derivative(initial_approximation)
    
    approximation: float = f / f_prime
    while(abs(approximation) >= tolerance):
        # finds f
        x = initial_approximation
        f = eval(sequence)

        # finds f' 
        f_prime = custom_derivative(initial_approximation)

        # division operation
        approximation = f / f_prime

        # subtraction property
        initial_approximation -= approximation
        iteration_counter += 1

    print(f"{iteration_counter}\n")

# newton_raphson method
initial_approximation: float = -4
tolerance: float = 10 ** (-4)
sequence: str = "(x**3) + (4 * (x**2)) - 10"

newton_raphson(initial_approximation, tolerance, sequence)

        
