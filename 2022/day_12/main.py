file_number = 1
with open(f'in/{file_number}.txt') as f:
    lines = [a.split() for a in f.read().rstrip().split('\n')]

lines

