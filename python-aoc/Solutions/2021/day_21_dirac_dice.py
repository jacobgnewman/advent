p1, p2, p1score, p2score, dieroll, die = 5, 8, 0, 0, 0, 1
while True:
    sumdi = 0
    for i in range(3):
        sumdi += die
        die +=1
        if die == 101:
            die = 1
    dieroll +=3
    p1 += sumdi
    if p1%10 == 0:
        p1score += 10
        p1 = 10
    else:
        p1score += p1%10
        p1 = p1%10
    if p1score >=1000:
        print(p2score*dieroll)
        break
    sumdi = 0
    for i in range(3):
        sumdi += die
        die +=1
        if die == 101:
            die = 1
    dieroll +=3
    p2 += sumdi
    if p2%10 == 0:
        p2score += 10
        p2 = 10
    else:
        p2score += p2%10
        p2 = p2%10
    if p2score >=1000:
        print(p1score*dieroll)
        break
p1, p2, p1score, p2score, memo = 5, 8, 0, 0, {}

possrolls = []
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            possrolls.append(i+j+k)
optim = []
for i in range(3,10):
    optim.append([i, possrolls.count(i)])

memo = {}
    
def getwinner(p1,p2,p1score, p2score, turn, dieroll):
    if turn == 0:
        p1 += dieroll
        if p1%10 == 0:
            p1score += 10
            p1 = 10
        else:
            p1score += p1%10
            p1 = p1%10
        if p1score >=21:
            return [1,0]
        else:
            outcome = [0,0]
            for roll, mu in optim:
                if (p1,p2,p1score, p2score, 1, roll) not in memo:
                    memo[(p1,p2,p1score, p2score, 1, roll)] = getwinner(p1,p2,p1score, p2score, 1, roll)
                outcome[0] += memo[(p1,p2,p1score, p2score, 1, roll)][0]*mu
                outcome[1] += memo[(p1,p2,p1score, p2score, 1, roll)][1]*mu
            return outcome
    else:
        p2 += dieroll
        if p2%10 == 0:
            p2score += 10
            p2 = 10
        else:
            p2score += p2%10
            p2 = p2%10
        if p2score >=21:
            return [0,1]
        else:
            outcome = [0,0]
            for roll, mu in optim:
                if (p1,p2,p1score, p2score, 0, roll) not in memo:
                    memo[(p1,p2,p1score, p2score, 0, roll)] = getwinner(p1,p2,p1score, p2score, 0, roll)
                outcome[0] += memo[(p1,p2,p1score, p2score, 0, roll)][0]*mu
                outcome[1] += memo[(p1,p2,p1score, p2score, 0, roll)][1]*mu
            return outcome

total = [0,0]
for roll, mul in optim:
    x, y = getwinner(p1,p2,p1score, p2score, 0, roll)
    total[0] += x * mul
    total[1] += y * mul
print(total)