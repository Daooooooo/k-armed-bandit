import random
import numpy
import numpy.random.mtrand


def slot_machines(num=1):
    if num == 1:
        return int(numpy.random.mtrand.normal(500, 50))
    elif num == 2:
        return int(numpy.random.mtrand.normal(550, 100))


Initial_value = 1000
Action_times = 0
A_times = 0
B_times = 0
sum_value1 = Initial_value
sum_value2 = Initial_value
action_value1 = sum_value1/(A_times+1)
action_value2 = sum_value2/(B_times+1)
while Action_times < 1000000:
    if random.random() < 0.01:
        if action_value1 > action_value2:
            sum_value1 += slot_machines(1)
            A_times += 1
            action_value1 = sum_value1 / A_times
        elif action_value1 < action_value2:
            sum_value2 += slot_machines(2)
            B_times += 1
            action_value2 = sum_value2 / B_times
        elif action_value1 == action_value2:
            random1 = random.randint(1, 2)
            if random1 == 1:
                sum_value1 += slot_machines(1)
                A_times += 1
                action_value1 = sum_value1 / A_times
            elif random1 == 2:
                sum_value2 += slot_machines(2)
                B_times += 1
                action_value1 = sum_value1 / B_times
    else:
        random1 = random.randint(1, 2)
        if random1 == 1:
            sum_value1 += slot_machines(1)
            A_times += 1
            action_value1 = sum_value1 / A_times
        elif random1 == 2:
            sum_value2 += slot_machines(2)
            B_times += 1
            action_value1 = sum_value1 / B_times
    Action_times += 1

print("老虎机A的期望是:%.2f" % action_value1)
print("老虎机A的选择次数是:%.2f" % A_times)
print("老虎机B的期望是:%.2f" % action_value2)
print("老虎机B的选择次数是:%.2f" % B_times)
print("选择次数差:%d" % (A_times-B_times))

