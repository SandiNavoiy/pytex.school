class User:
    age= 10

    def __init__(self, name):
        self.name = name
        self.email = None
        self.password = "password"


print(User.age)

alice = User("Alice")
print(alice.age)

bob = User("Bob")
print(bob.age)