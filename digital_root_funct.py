def digital_root(n):
    x=0
    while True:
        for y in str(n):
            x+=int(y)
        n=x
        if len(str(x))==1:
            break
        x=0

    return x

