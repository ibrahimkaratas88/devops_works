def box(n):
    times = 0
    if n == 1:
        print("#")
    else:
        top = "#" * n
        mid = "#" + " " * (n-2) + "#"
        
    print(top)
    while times < (n-2):
        print(mid)
        times += 1
    print(top)
box(7)
box(3)
for i in range(3):
    box(3)        

    

      