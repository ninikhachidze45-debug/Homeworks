# 1.
x = float(input())
y = float(input())
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)

# 2.
x = float(input("First diagonal lnegth:"))
y = float(input("Second diagonal length:"))
area = x * y / 2
print("area =", area)

# 3.
m = float(input("Enter value in metres:"))
cm = m * 100
dm = m * 10
mm = m * 1000
mi = m / 1609
print(cm, "cm", dm, "dm", mm, "mm", mi, "mi")

# 4.
h = float(input("Enter height:"))
b = float(input("Enter base:"))
area = h * b / 2
print("Area =", area)

# 5
n = int(input("Enter two-digit number:"))
x = n // 10
y = n % 10
sum = x + y
print(sum)