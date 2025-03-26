
# Patrick Harris
# 3/25/25
# P4HW1
# Use nested loops to get valid grades from user


'''
--------pseudo--------
Outer loop - used to get grades from user
-create variable from input -> num_scores (int)
-create list to store grades -> scores_list = []
-for each in range (num_scores)
    -get grade from user input in every iteration of loop
    -score = int(input(f"enter score number #{each+1}: "))
    -while score < 0 or score > 100:
        -print(invalid score)
        -print(score should be xyz)
        -score = int(input(f"enter score number #{each+1} again: "))
    -scores_list.append(score)
-print scores_list to ensure correctness

-get lowest score in list -> variable (min)
-remove the lowest score from the list

-get average after removing lowest score -> variable
-use avg to determine letter grade -> variable?



'''

num_scores = int(input('How many scores do you want to enter? '))

scores_list = []
for each in range(num_scores):
    score = int(input(f'Enter score #{each+1}: '))
    
    while score < 0 or score > 100:
        print('Invalid score')
        print('Score should be between 0 and 100.')
        score = int(input(f'Enter score #{each+1} again: '))
    scores_list.append(score)

lowest = min(scores_list)
scores_list.remove(min(scores_list))
average = sum(scores_list) / len(scores_list)
print()
print()
print(f'{"-"*13}Results{"-"*13}')
print(f'Lowest score : {lowest:.1f}')
print(f'Modified List : {scores_list}')
print(f'Scores Average : {average}')

if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print(f'Grade : {letter_grade}')
print('-'*34)
