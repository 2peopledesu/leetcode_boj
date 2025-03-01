import sys

input = sys.stdin.readline

def valid_check(sequence):
    check_length = len(sequence)
    
    for i in range(1, check_length + 1):
        first_part = sequence[check_length - i * 2: check_length - i]
        last_part = sequence[check_length - i: check_length]

        if first_part == last_part:
            return False
    
    return True

def generate_sequence(sequence, length):
    global result
    if (length == n):
        print(sequence)
        return True

    for i in range(1, 4):
        sequence += str(i)
        if valid_check(sequence):
            if generate_sequence(sequence, length + 1):
                return True
        sequence = sequence[:-1]
    
    return False
        

n = int(input())

generate_sequence("", 0)