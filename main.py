import random
import time


operators = ["+", "-", "*"]
min_operand = 3
max_operand = 12
total_problems = 10
miss = 0
correct = 10

def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator =random.choice(operators)
    
    expr = str(left) + " " + operator +  " " + str(right)
    answer = eval(expr)
    return expr, answer


input("Press enter to start")
print("--------------------------")

start_time = time.time()

for i in range(total_problems):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " +  expr + " = " )
        if guess == str(answer):
            
            break
        if guess != str(answer):
            correct -= 1
            miss +=1
            
end_time = time.time()
total_time = round(end_time - start_time, 2)            
            
print("--------------------------")            
print("Nice work! You finished in", (total_time), "seconds! Below are your results:")           
print("Correct: " + str(correct))            
print("Miss: " + str(miss))
            