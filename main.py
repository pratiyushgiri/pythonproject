import backend

def main():
    user =  input("Enter name: ")
    greet = backend.hello_world(user)
    print(greet)

main()

