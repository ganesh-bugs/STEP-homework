def denominate(num):
    deno = {'2000':2000,'500':500,'200':200,'100':100,'50':50,'20':20,'10':10,'5':5,'1':1}
    while num != 0:
        for i,j in deno.items():
            print(f'Rs. {i} x {num//j}')
            num = num%j