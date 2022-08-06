lines = []  #list comprehending a string for each file line
with open('lezione4/data/origin.txt', 'r') as origin:
    lines = origin.readlines()

line_1 = [int(line.strip('\n')) for line in lines[0].split(',')]    #list of integers
line_2 = [int(line.strip('\n')) for line in lines[1].split(',')]    #list of integers
#print(line_1)
#print(line_2)

#sum = []
sum = [x + y for x, y in zip(line_1, line_2)]
# zip() takes iterable or containers and returns a single iterator object, having mapped values from all the containers. 
#print("sum = {}".format(sum))

#lines = []
with open('homeworks/result.txt', 'w') as target:
    line = []   #list of the numbers to be printed for each line of the matrix
    for row in range(len(sum)):
        for col in range(len(sum)):
            if row == col: line.append(sum[row])
            else: line.append(0)
        #print(','.join(str(n) for n in line))
        target.write(','.join(str(n) for n in line))
        target.write('\n')
        #lines.append(','.join(str(n) for n in line))
        line = []
    #target.writelines(lines)