from sympy import mod_inverse   
from math import gcd

def pollards_rho_task(p, a, b):
     
    c = 1
    u, v = 0, 0
    steps = []   
    order = p - 1   

    def f(c, u, v, p):
         
        if c < p // 2:  
            return (a * c) % p, (u + 1) % order, v
        else:   
            return (b * c) % p, u, (v + 1) % order

    seen = {}

    while c not in seen:
         
        seen[c] = (u, v)
        steps.append((c, u, v))

         
        c, u, v = f(c, u, v, p)

     
    c_collision = c
    u1, v1 = seen[c]
    u2, v2 = u, v

     
    u_diff = (u1 - u2) % order
    v_diff = (v2 - v1) % order

     
    divisor = gcd(u_diff, order)
    if divisor != 1:
        raise ValueError(f"Решение не существует, так как gcd({u_diff}, {order}) = {divisor}.")

     
    inv_u_diff = mod_inverse(u_diff, order)
    x = (v_diff * inv_u_diff) % order

     
    import pandas as pd
    steps_table = pd.DataFrame(steps, columns=["c", "u", "v"])
    return x, steps_table


 
p = 107   
a = 10    
b = 64    

 
try:
    x, steps_table = pollards_rho_task(p, a, b)
    print(f"Решение: x = {x}")
    print("Таблица шагов:")
    print(steps_table)
except ValueError as e:
    print(str(e))
  