
A2 = 0
A = 0
B2 = 0
B = 0
C2 = 0
C = 0
D2 = 0
D = 0
F = 0
# Open the file to access the grades.
with open('LetterGrades.txt', 'r') as f:
    # Make a list of all the grades.
    lines = [line.rstrip() for line in f]
    # Go through them in order to be able to count.
    for line in lines:

        if line == "A+":
            # This will update the count each time a new grade is in the loop.
            A2 += 1
        elif line == "A":
            A += 1
        elif line == "B+":
            B2 += 1
        elif line == "B":
            B += 1
        elif line == "C+":
            C2 += 1
        elif line == "C":
            C += 1
        elif line == "D+":
            D2 += 1
        elif line == "D":
            D += 1
        elif line == "F":
            F += 1

print("%-8s%-9s" % ("grade", "frequency"))  # Normal formatting, done exactly like the Word file.
print("%-9s%-8d" % ("A+", A2))
print("%-9s%-8d" % ("A", A))
print("%-9s%-8d" % ("B+", B2))
print("%-9s%-8d" % ("B", B))
print("%-9s%-8d" % ("C+", C2))
print("%-9s%-8d" % ("C", C))
print("%-9s%-8d" % ("D+", D2))
print("%-9s%-8d" % ("D", D))
print("%-9s%-8d" % ("F", F))



