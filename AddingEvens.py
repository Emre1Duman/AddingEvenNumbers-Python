#Adding only even numbers from a range of 1 to 100

sum_of_evans = 0
sum_of_evans2 = 0

#conditional statement method
for number in range(1, 101):
    if number % 2 == 0:
        sum_of_evans += number
print(sum_of_evans)

#Step size method for range()
for number in range(0, 101, 2): #Could start from 0 or 2
    sum_of_evans2 += number
print(sum_of_evans)


