for i in range(1, 32):
    with open(f'day{i:02d}.py', 'w') as f:
        t = f"with open('input{i:02d}.txt') as f:\n    lines = f.readlines()\n    for line in lines:\n        pass\n"
        f.write(t)

    with open(f'input{i:02d}.txt', 'w') as f:
        f.write('')