dir_sizes = {}
stack = []

with open("input.txt") as file:
    for line in file:
        parts = line.strip().split()  

        if parts[0] == "$" and parts[1] == "cd":
            if parts[2] == "/":
                stack = ["/"]  
            elif parts[2] == "..":
                stack.pop()  
            else:
                stack.append(parts[2])  

        elif parts[0].isdigit():
            size = int(parts[0]) 
            path = "/".join(stack)  

            for i in range(len(stack)):
                parent_path = "/".join(stack[0:i+1])  
                dir_sizes[parent_path] = dir_sizes.get(parent_path, 0) + size  

result = sum(size for size in dir_sizes.values() if size <= 100000)

print("Сума розмірів директорій ≤ 100000:", result)
#result: 1453349