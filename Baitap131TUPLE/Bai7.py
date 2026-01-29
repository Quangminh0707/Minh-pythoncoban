students = (
    ("An", 8.5),
    ("Bình", 7.0),
    ("Chi", 9.2)
)

for s in students:
    print(s[0], "-", s[1])

best_student = max(students, key=lambda x: x[1])
print("Học sinh có điểm cao nhất:", best_student)