with open('17_12735.txt') as file:
    data = [int(i) for i in file]

maxx_09 = max([i for i in data if i[-2:] == '09'])

ans = []
for i in range(len(data) - 2):
    a1,a2,a3 = data[i], data[i + 1], data[i+2]
    summ = a1+a2+a3

    U1  = a1 % 7 == 0
    U2  = a2 % 7 == 0
    U3  = a3 % 7 == 0
    u = u1 + u2 + u3 == 2

    f1 = (a1[-2:] == '09' or a2[-2:] == '09' or  a3[-2:] == '09') >= 1
    f =