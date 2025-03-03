def cal_value(line):
    digits = ""
    for char in line:
        if char.isdigit():
            digits += char

    if digits:
        return int(digits[0] + digits[-1]) 
    
    return 0

with open("input3.txt", "r", encoding="utf-8") as file:
    total_sum = sum(cal_value(line) for line in file)

print("Сума всіх калібрувальних значень:", total_sum)

#result: 55538