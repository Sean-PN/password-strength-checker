import string

def password_strength(password):
    
    score = 0
    length = len(password)

    upper_case = any(c.isupper() for c in password)
    lower_case = any(c.islower() for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c.isdigit() for c in password)

    #character type score
    characters = [upper_case, lower_case, special, digits]

    #Length score
    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 20:
        score += 1

    #char diversity string
    score += sum(characters) - 1

    #score check
    if score < 4:
        return "Weak", score
    elif score == 4:
        return "Okay", score
    elif 4 < score < 6:
        return "Good", score
    else:
        return "Strong", score

while True:
    
    #loop until a strong password is entered
    password = input("Enter password: ")
    strength, score = password_strength(password)
    print(f"Password strength: {strength} (score: {score})")
    
    if strength == "Strong":
        print("Good job! Password accepted.")
        break

