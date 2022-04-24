# age = 19
# # guests = 0
# isBirthday= True

# if age >= 21:
#     print("You can drink")
#     if isBirthday:
#         print("Happy Birthday, here's a free martini")
# elif age >= 18:
#     print("You can come in but no drinking!")
#     if isBirthday:
#         print("Happy Birthday, here is a free apple juice")
# else:
#     print("Sorry go home kid!")



# loops

# num = 0

# while num <= 100:
#     print(num)
#     num = num + 10

# print("All done")


# target = 37
# guess = None

# while guess != target:
#     guess = input("Please enter a guess...")
#     if guess == 'q' or guess == 'quit':
#         break
#     guess = int(guess)
    
#     print("All Done")


# colors = ['red', 'blue', 'green', 'yellow']
# for color in colors:
#     print(color)

    # for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    #     print(char)

# for num in "abcde":
#     print("Hello")

# for n in range(10):
#     print(n)



# def greet(person):
#     return f"Hello there, {person}"

# def divide(a,b):
#     if type(a) is int and type(b) is int:
#         return a/b
#     return 'a and b must be integers'


def send_email(to_email, from_email, subject, body):
    email = f"""
        to: {to_email}
        from: {from_email}
        subject: {subject}
        ------------------
        body: {body}
        """
    print(email)

send_email(subject= "Meow", to_email="blue@gmail.com", 
            from_email="cat@mail.com", body="Hello there")