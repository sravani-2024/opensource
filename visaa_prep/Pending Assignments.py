x, y, z = map(int, input().split())

total_time = x * y

total_allowed_time = 2 * 24 * 60

if total_time <= total_allowed_time:
    print("YES")
else:
    print("NO")
