def gym_trainer_budget(x, y, z):
    if x <= z and x + y <= z:
        return 2
    elif x <= z:
        return 1
    else:
        return 0
x, y, z = map(int, input().split())
result = gym_trainer_budget(x, y, z)
print(result)
