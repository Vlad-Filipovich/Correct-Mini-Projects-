start_list = ['88', '32', '22', '16', '17']
for power in range(1, 11):
    answer_list = []
    for i in range(5):
        n = start_list[i]
        a = len(n) - 1
        total = 0
        for i in range(len(n)):
            total += int(n[i]) * (power ** a)
            a -= 1
        answer_list.append(total)
    if answer_list[0] == sum(answer_list[1:]):
        break
print(power)
print(answer_list)