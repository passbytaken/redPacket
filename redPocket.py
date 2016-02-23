# coding:utf-8
def redPacket(people, money):
    result = []
    remain = people
    max_money = money / people * 2
    for i in range(people):
        remain -= 1
        if remain > 0:
            m = random.randint(1, min(money - remain, max_money))
        else:
            m = money
        result.append(m / 100.0)
        money -= m
    return result