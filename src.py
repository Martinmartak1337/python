def bilbo(comp, player):
    t = [[2, 0, 1], [1, 2, 0], [0, 1, 2]]
    v = ["smart_monkey", "stupid_monkey", "draw_monkey"]
    i = t[comp][player]
    print(v[i])


k = 0
n = 1
p = 2

bilbo(p, n)
