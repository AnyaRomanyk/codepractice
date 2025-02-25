reports = []

with open("input.txt") as file:
    for line in file:
        numbers = line.split()
        report = [int(num) for num in numbers]
        reports.append(report)

def is_safe(report):
    increasing = True
    decreasing = True
    valid_differences = True
    
    for i in range(len(report) - 1):
        if report[i] >= report[i + 1]:
            increasing = False
        if report[i] <= report[i + 1]:
            decreasing = False
        if not (1 <= (report[i] - report[i + 1]) * ((report[i] - report[i + 1]) >= 0) <= 3):
            valid_differences = False
    
    return (increasing or decreasing) and valid_differences

safe_count = sum(1 for report in reports if is_safe(report))
print("Number of safe reports:", safe_count)
#result: 106