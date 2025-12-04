#!/usr/bin/env python3

with open('day06.example', 'r') as input:
    fish = list(map(int, input.readline().split(',')))

day = 0
while True:
    #print('fish', fish)
    new = []
    for i in range(len(fish)):
        fish[i] -= 1
        if fish[i] < 0:
            fish[i] = 6
            new.append(8)
    #print(new)
    fish.extend(new)
    #print(f'{len(fish)} lanternfish')
    day += 1
    print(day, len(fish))
    if day == 256: break

print(f'{len(fish)} lanternfish after {day} days')
