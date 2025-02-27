import sys

input_string = sys.stdin.readline().strip()

max_value = min_value = ""
m_count = 0

for char in input_string:
    if char == "M":
        m_count += 1 
    elif char == "K":
        if m_count:
            min_value += str(10 ** m_count + 5)
            max_value += str(5 * (10 ** m_count)) 
        else:
            min_value += "5"
            max_value += "5"
        m_count = 0 

if m_count:
    min_value += str(10 ** (m_count - 1))
    while m_count:
        max_value += "1"
        m_count -= 1

print(max_value)
print(min_value)
