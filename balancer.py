def balancer():
    global balance
    balance = 45
    iter = 10000
    w = 0
    l = 0
    for a in range(1, iter):
        enemy.hp = 100
        hero.hp = 100
        result = main()
        if result is 1:
            w += 1
        if result is 0:
            l += 1
    print("W: {}%  L: {}%".format(((w / iter) * 100), ((l / iter) * 100)))

balancer()
