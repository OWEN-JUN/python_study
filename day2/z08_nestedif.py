#중첩 nested if

# A == B, B == C, A == C
A = 20; B=20; C=10;
if A == B:
    if B == C:
        print("A == C")
    else:
        print("A == B, B != C")
else:
    print("A != B")

