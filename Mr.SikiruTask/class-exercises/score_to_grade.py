score = int(input("Enter student score: "))s
    if score >= 75:
        return "A"
    elif score >= 65 and score < 75:
        return "B"
    elif score >= 50 and score < 65:
        return "C"
    elif score >= 40 and score < 50:
        return "D"
    else:
        return "E"

 