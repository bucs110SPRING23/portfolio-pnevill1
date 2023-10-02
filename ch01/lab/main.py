import random
# Part A
weeks = 16
print("Variable weeks:", weeks, type(weeks))

classes = 5
print("Variable classes:", classes, type(classes))

tuition = 6000
print("Variable tuition:", tuition, type(tuition))

cost_per_week = (tuition / classes) / weeks
print("Cost per week:", cost_per_week)

classes_per_week = 3
print("Variable classes_per_week:", classes_per_week, type(classes_per_week))

cost_per_class = cost_per_week/classes_per_week
print("Variable cost_per_class:", cost_per_class, type(cost_per_class))
print("Cost per class:", cost_per_class)

# Part B
my_random_list = ["hello", 5, "AAAAAAAAAA", 17, 4.31]

my_random_result = random.choice(my_random_list)
print(my_random_result)