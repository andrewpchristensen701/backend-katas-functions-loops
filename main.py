def add(x,y):
  return x+y

def multiply(x,y):
  mul=0
  for i in range(0,1):
    mul=add(mul,y)
  return mul

def power(x,n):
 pwr = 1
 for i in range(1,n):
  multiply(pwr,x)
  return

def factorial(x):
  fct = x
  for i in range(2,x):
    fct=multiply(fct,x-1)
  return fct

def fibonacci(n):
  fib=0
  ona = 0
  cci =1
  if n == 0:
    return "Error"
  elif n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    for k in range(0,n):
      fib = add(ona, cci);
      ona = cci
      cci = fib
  return fib