RS = int(input("Enter the number of red shirt: "))
BS = int(input("Enter the number of blue shirt: "))
WS = int(input("Enter the number of White shirt: "))

total = RS + BS + WS

prob_a = BS / total
prob_b = RS / total

prob_bga = prob_b
prob_a_and_b = prob_a * prob_b
print("Probability that the second shirt is red given that the first shirt is blue: ")
print(round(prob_bga, 3))

print("Probability of getting 1st blue and 2nd red shirt: ")
print(round(prob_a_and_b, 3))