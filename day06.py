def read_input(lines, version=1):
    if version == 1:
        times = [int(x) for x in lines[0].split(":")[1].split()]
        distances = [int(x) for x in lines[1].split(":")[1].split()]
        return times, distances
    else:
        times = [int(lines[0].split(":")[1].replace(" ", "").replace("\n", ""))]
        distances = [int(lines[1].split(":")[1].replace(" ", "").replace("\n", ""))]
        return times, distances
    

with open('input06.txt') as f:
    lines = f.readlines()

times, distances = read_input(lines, version=2)
print(times, distances)

ans = 1
for time, distance in zip(times, distances):
    ans *= sum((time * hold) - (hold**2) > distance for hold in range(time))

print(ans)
