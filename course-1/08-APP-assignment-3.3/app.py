score = float(input("Enter Score: "))

if score> 1 or score < 0:
    print("Error")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")