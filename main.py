from Functions.know_how import recognize

with open('data_1.txt', 'r') as f:
    l = [[int(num) for num in line.split(' ')] for line in f]

recognize(l)