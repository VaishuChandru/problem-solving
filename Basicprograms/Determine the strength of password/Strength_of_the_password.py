/*
@inputl:string(password)
@output:will return strength(weak,medium,good,strong)
*/

def check_Strength_Of_Pwd(ip):
    cond_1, cond_2, cond_3 = 0, 0, 0
    strength = 0
    if 6 <= len(ip) < 18:
        strength += 1
    for i in range(len(ip)):
        if cond_1 == 0:
            if ord(ip[i]) in range(65, 91):
                cond_1 = 1
                strength += 1
                continue
        if cond_2 == 0:
            if ip[i] in str(list(range(0, 10))):
                cond_2 = 1
                strength += 1
                continue
        if cond_3 == 0:
            if ip[i] in ['!', '@', '#', '$', '&', '*']:
                cond_3 = 1
                strength += 1
    if strength == 4:
        return "Strong"
    elif strength == 3:
        return "Good"
    elif strength == 2:
        return "Medium"
    else:
        return "Weak"

password = input("Hey, enter ur password to know its strength")
print(check_Strength_Of_Pwd(password))
