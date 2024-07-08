import random
captcha_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
name=""
for i in range(5):
    random_character = random.choice(captcha_characters)
    name= name+random_character
    
print(name)
