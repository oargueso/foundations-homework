# Grade: 14.5 / 15

# Olaya Argueso
# Homework2

#LISTS
#make a list of numbers
numbers = [22, 90, 0, -10, 3, 22, 48]

#display the list
print(len(numbers))

#display the 4th element
print(numbers[3])

#display the sum of the 2nd and the 4th elements
print(numbers[1] + numbers[3])

#display the second largest value in the list
sorted_numbers = sorted(numbers)
print(sorted_numbers[5])

#display the last element of the original unsorted list
print(numbers[6])

#for loop

# TA-COMMENT: Yasssss! :)

for number in numbers:
    original = number
    if number < 10: # TA-COMMENT: Technically, it would be more consistent to use 'if original < 10' here (like you did in your other if conditions), but since it's your first condition, you have not manipulated number yet (and therefore, it didn't affect your output)
        number = number * 30
        if original % 2 == 0:
            number = number + 6

    if original > 50: # TA-COMMENT: This can be an elif since you know that < 10 and > 50 will not co-occur. And if you use elif, python does not have to check if both conditions are true (and therefore, your code will be slightly faster).

        number = number - 10
    if original != -10:
        number = number - 1
    print(number)

#sum of each number divided by two (not sure if I got right what you wanted here)
divided_numbers = sum(numbers)/2
print(divided_numbers)

#DICTIONARIES
#movie dictionary
movie = {'title': 'Raiders of the Lost Ark', 'year': '1981', 'director': 'Steven Spielberg', 'budget' : 18000000, 'revenue': 390000000}

# TA-COMMENT: (-0.5) We can add entries to a dictionary AFTER making it. We wanted to see syntax such as:
# movie['budget'] = 18000000
# rather than "hard coding" budget and revenue into the initial dictionary.

print("My favourite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])
print(movie['budget']-movie['revenue'])

if movie['revenue'] < movie['budget']:
    print("It was a flop")
elif movie['revenue'] > movie['budget']*5:
    print("That was a good investment")

#Boroughs dictionary
boroughs = {'Manhattan': 1.6, 'Brooklyn': 2.6, 'Bronx': 1.4, 'Queens': 2.3, 'Staten Island': 0.47}
print(boroughs['Brooklyn'])
total_population = sum(boroughs.values()) # TA-COMMENT: Very nice!
print(total_population)
manhattan_population = (boroughs['Manhattan']/total_population)*100
print(manhattan_population)
