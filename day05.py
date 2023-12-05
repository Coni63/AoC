import random
import matplotlib.pyplot as plt


class Ranger:
    def __init__(self, source, target, num_items):
        self.source = source
        self.target = target
        self.num_items = num_items

    def contains(self, value):
        return self.source <= value < self.source + self.num_items

    def get_target(self, value):
        offset = value - self.source
        return self.target + offset


def get_location_for_seed(seed: int) -> int:
    soil = seed
    for ranger in seed_soil_map:
        if ranger.contains(seed):
            soil = ranger.get_target(seed)
            break

    fertilizer = soil
    for ranger in soil_fertilizer_map:
        if ranger.contains(soil):
            fertilizer = ranger.get_target(soil)
            break

    water = fertilizer
    for ranger in fertilizer_water_map:
        if ranger.contains(fertilizer):
            water = ranger.get_target(fertilizer)
            break

    light = water
    for ranger in water_light_map:
        if ranger.contains(water):
            light = ranger.get_target(water)
            break

    temperature = light
    for ranger in light_temperature_map:
        if ranger.contains(light):
            temperature = ranger.get_target(light)
            break

    humidity = temperature
    for ranger in temperature_humidity_map:
        if ranger.contains(temperature):
            humidity = ranger.get_target(temperature)
            break

    location = humidity
    for ranger in humidity_location_map:
        if ranger.contains(humidity):
            location = ranger.get_target(humidity)
            break
    return location


def generator_from(seeds):
    n = len(seeds) // 2
    for _ in range(50_000):
        idx = random.randint(0, n - 1)
        start, length = seeds[2 * idx], seeds[2 * idx + 1]
        pos = random.randint(0, length-1)
        yield start + pos


with open("input05.txt", "r") as f:
    lines = f.readlines()


lines = [x.replace("\n", "").strip() for x in lines]


seed_soil_map = []
soil_fertilizer_map = []
fertilizer_water_map = []
water_light_map = []
light_temperature_map = []
temperature_humidity_map = []
humidity_location_map = []


stage = 0

for i, line in enumerate(lines):
    if line == "":
        continue

    if i == 0:
        seeds = [int(x) for x in line.replace("seeds: ", "").split(" ")]
        continue

    if line == "seed-to-soil map:":
        stage = 1
        continue

    elif line == "soil-to-fertilizer map:":
        stage = 2
        continue

    elif line == "fertilizer-to-water map:":
        stage = 3
        continue

    elif line == "water-to-light map:":
        stage = 4
        continue

    elif line == "light-to-temperature map:":
        stage = 5
        continue

    elif line == "temperature-to-humidity map:":
        stage = 6
        continue

    elif line == "humidity-to-location map:":
        stage = 7
        continue

    target, source, offset = [int(x) for x in line.split()]

    if stage == 1:
        seed_soil_map.append(Ranger(source, target, offset))
    elif stage == 2:
        soil_fertilizer_map.append(Ranger(source, target, offset))
    elif stage == 3:
        fertilizer_water_map.append(Ranger(source, target, offset))
    elif stage == 4:
        water_light_map.append(Ranger(source, target, offset))
    elif stage == 5:
        light_temperature_map.append(Ranger(source, target, offset))
    elif stage == 6:
        temperature_humidity_map.append(Ranger(source, target, offset))
    elif stage == 7:
        humidity_location_map.append(Ranger(source, target, offset))


# V1
lowest = 1e25
for seed in seeds:
    location = get_location_for_seed(seed)
    lowest = min(lowest, location)
print(lowest)

# V2

X = []
Y = []
lowest = 1e25

# for seed in generator_from(seeds):
for seed in range(4_042_000_000, 4_042_500_000):
    location = get_location_for_seed(seed)
    X.append(seed)
    Y.append(location)
    lowest = min(lowest, location)

print(lowest)


plt.figure(figsize=(10, 10))
plt.scatter(X, Y, s=1)
plt.show()
