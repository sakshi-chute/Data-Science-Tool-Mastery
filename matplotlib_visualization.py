import matplotlib.pyplot as plt

subjects = ['Python', 'Java', 'DBMS', 'Statistics']
marks = [85, 75, 90, 80]

plt.bar(subjects, marks)

plt.title("Student Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()