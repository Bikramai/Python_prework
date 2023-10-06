# Create the function that takes a name as an agrument and 
# return a new string that say hello and then name that was the argument
# use the function and ask the user for their name and tell them hello

print("Bikram")

name = 'Bikram'
print(name)

print("Hello", name)
print("Hello" + " " + name)
hello_Bikram = "Hello" + " " + name
print(hello_Bikram)

print('Are function is defined below')
def say_hello_print(the_users_name):
    print("Hello" + the_users_name )
    return None

print("using out the function with the print statement inside")
say_hello_print(" Bikram")
print(say_hello_print(" Bikram"))


def say_hello_return(the_users_name):
    return "hello " + the_users_name

print("Using our function with the return statement inside and not printing ")
print (say_hello_return("Ram") == "hello Bikram")


print(say_hello_return("Ram"))
hello_Bikram = say_hello_return("Bikram")
print(hello_Bikram)


users_name = input("What is your name? ")
print(users_name)
print(type(users_name))
print(say_hello_return(users_name))