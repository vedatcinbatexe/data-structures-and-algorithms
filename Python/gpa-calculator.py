print('Welcome to the GPA Calculator!')
print('Please enter your grades for each course separated by commas (e.g., A,B,C,D,F):')
print('Enter a blank line to designate the end of input.')

points = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0.0
}

num_courses = 0
total_points = 0.0
done = False

while not done:
    grade = input()
    if grade == '':
        done = True
    elif grade not in points:
        print('Invalid grade entered. Please enter a valid grade (A+, A, A-, B+, B, B-, C+, C, C-, D+, D, F).')
    else:
        num_courses += 1
        total_points += points[grade]

if num_courses > 0:
    print(f'Your GPA is: {total_points / num_courses:.2f}')