with open('D:\\Kodowanie\\Personal\\removal.txt', 'r') as f1:
    lines_to_remove = f1.readlines()
with open('D:\\Kodowanie\\Personal\\decklist.txt', 'r') as f2:
    lines_to_modify = f2.readlines()
with open('D:\\Kodowanie\\Personal\\ver2.txt', 'w') as f3:
    for line1 in lines_to_modify:
        i = 0
        for line2 in lines_to_remove:
            if line1.strip("\n") == line2.strip("\n"):
                i += 1        
        if i == 0:
            f3.write(line1)

with open('D:\\Kodowanie\\Personal\\ver3.txt', 'w') as f4:
    lines_of_result = set(lines_to_modify)-set(lines_to_remove)
    result = list(lines_of_result)
    result.sort()
    for line in result:
        f4.write(line)