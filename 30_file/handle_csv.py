import csv
# 写入
with open('30_file/test.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # 写入表头
    writer.writerow(['Name', 'Age', 'City'])
    # 写入多行数据
    writer.writerows([
        ['Alice', 30, 'New York'],
        ['Bob', 25, 'Los Angeles'],
        ['Charlie', 35, 'Chicago']
    ])
 
# 读取
with open('30_file/test.csv', mode='r') as file:
    reader = csv.reader(file)
    head = next(reader)  # 读取表头
    print("表头:", head)
    for row in reader:
        print("行数据:", row)
