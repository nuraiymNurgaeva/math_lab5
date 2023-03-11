from sympy import diff, symbols, cos, sin, lambdify, sqrt


e = 0.001
A = [2, 9, 0, -4]
a_b = [-1, 1]
x = symbols('x')
# f = diff(x**3, x)`
# print(lambdify(x, f)(2))

flag = False
for i in range(len(A)-2):
    if flag:
        break
    if i == 0:
        k1 = 3
        k = [2, 1]
    if i == 1:
        k1 = 2
        k = [3, 1]
    if i == 2:
        k1 = 1
        k = [3, 2]
    B = A.copy()
    del B[i]
    ur = 0
    for j in range(len(B)):
        B[j] *= -1
        if j < 2:
            ur += B[j] * x**k[j]
        else:
            ur += B[j]
    print(ur)
    f = diff((ur), x)
    f1 = lambdify(x, f)
    if f1(a_b[0]) <= 1 and f1(a_b[1]) <= 1:
        ur /= A[i]
        ur = ur**(1/k1)
        f2 = lambdify(x, ur)
        x1 = sum(a_b) / 2
        x2 = f2(x1)
        print("x = " + str(ur))
        while abs(x2-x1) > e:
            x1 = x2
            x2 = f2(x1)
            print('x = ', x2)
        flag = True
    else:
        print(f)

print(x2)