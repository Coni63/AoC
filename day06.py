with open('input06.txt') as f:
    lines = f.readlines()

times = [int(x) for x in lines[0].split(":")[1].split()]
distances = [int(x) for x in lines[1].split(":")[1].split()]

print(times, distances)

ans = 1
for time, distance in zip(times, distances):
    ans *= sum((time * hold) - (hold**2) > distance for hold in range(time))

print(ans)