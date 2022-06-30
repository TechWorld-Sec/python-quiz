print ("Welcome to the TechWorld Security Quiz")


playing = input("Do you want to play? " 'Yes or No  ' )

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("The malicious software program, which is detrimental to other computer programs is known as ")
if answer.lower() == "virus":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("Which among the following is the shortcut key to refresh the active window in your computer system? ")
if answer.lower() == "f5":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("Byte is the series of how much bits? ")
if answer.lower() == "5":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("A hacker locks out users and encrypts their personal computer files and data, holding it hostage until they agree to pay to the attacker. What is this practice called? ")
if answer.lower() == "ransomware":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input(" A hacker can use a remote administration Trojan to shutdown an infected computer even if the power is switched off in the victim computer. True or False? ")
if answer.lower() == "false":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("A coffee shop that collects payments from customers by debit / credit cards would be liable under the data privacy law. True or False? ")
if answer.lower() == "true":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("Access privileges granted to a user, program or process is also known as: ")
if answer.lower() == "authorization":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("The concept of using same key for encryption and decryption is called ")
if answer.lower() == "symmetric key system":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("What key is used to generate ciphertext and plain text from the message in symmetric key systems? ")
if answer.lower() == "xor":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("I should put personal information on the internet where anyone can see it. True or False? ")
if answer.lower() == "false":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print()


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 14) * 100) + "%.")


print()


print("Thanks for playing our quiz game! Make sure to follow us on Instagram: @techworld_sec")

print()

print("Hope you learned something new about technology! :) ")