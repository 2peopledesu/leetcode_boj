def get_clock_num(num):
    digits = [int(d) for d in num]
    
    min_num = int(num)
    for i in range(1, 4):
        rotated = digits[i:] + digits[:i]
        rotated_num = int(''.join(map(str, rotated)))
        min_num = min(min_num, rotated_num)
    
    return min_num

num = ''.join(input().split())

clock_num = get_clock_num(num)

clock_nums = set()
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                num_str = f"{a}{b}{c}{d}"
                clock_nums.add(get_clock_num(num_str))

clock_nums = sorted(clock_nums)

print(clock_nums.index(clock_num) + 1)