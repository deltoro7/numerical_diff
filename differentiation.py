def derivative(f, a, max_h):
    for i in range(max_h):
        h = 1 / (10**i)
        estimate = (f(a+h) - f(a)) / h
        output =  " value of h =", h,  "estimate derivative = ",estimate
        print(output)
