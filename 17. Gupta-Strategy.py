#TCS TAG Qn #2

'''
🦠📜 The Admission Code of Ms. Gupta 📜🦠

During the dark days of the great pandemic, when classrooms fell silent
and learning moved into the digital realm,
there lived a legendary teacher known as Ms. Gupta.

But she was not an ordinary teacher.

She believed true talent does not shine in every subject —
it only needs to shine in one.

So she announced a challenge.

🌟 The Rule of Enrollment 🌟

Every student would submit their marks
across multiple subjects.

Ms. Gupta would then:

🔹 Step 1: Examine each subject separately.
🔹 Step 2: Compute the average marks of that subject.
🔹 Step 3: Compare every student’s score in that subject with the average.

And here was the twist:

If a student scored strictly greater than the average
in at least ONE subject —

they were considered exceptional.

They would be granted admission
into the prestigious Gupta Masterclass.

No second chances.
No bonus marks.
No rounding.

Just pure comparison.

Your mission is simple:

Given:
- The number of students
- The number of subjects
- The marks scored by each student

Determine how many students
earn their place in the Masterclass.

Remember:
A single moment of excellence is enough.
One subject above average.
That is all it takes.

Now, can you count the chosen ones?
'''

# My Version:-
sub_count, stud_count = map(int, input().split())

subjects = []

for i in range(sub_count):
    subjects.append(list(map(int, input().split())))

enrolled = set()
output = 0

for i in range(sub_count):
    avg = sum(subjects[i]) / len(subjects[i])
    
    for j in range(len(subjects[i])):
        if subjects[i][j] > avg and j not in enrolled:
            output += 1
            enrolled.add(j)
    
    if output == stud_count:
        break

print(output)

#GPT Version

def count_enrolled_students():
    n = int(input())   # number of students
    m = int(input())   # number of subjects

    # Read marks student-wise
    marks = []
    for _ in range(n):
        marks.append(list(map(int, input().split())))

    # Step 1: Calculate subject-wise averages
    averages = []
    for col in range(m):
        total = 0
        for row in range(n):
            total += marks[row][col]
        averages.append(total / n)

    # Step 2: Count eligible students
    enrolled = 0

    for i in range(n):
        for j in range(m):
            if marks[i][j] > averages[j]:  # strictly greater
                enrolled += 1
                break   # only one subject needed

    print(enrolled)