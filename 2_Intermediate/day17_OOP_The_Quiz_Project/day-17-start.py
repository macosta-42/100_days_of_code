# class User:
#     pass
#
#
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Matthieu"
#
# print(user_1.username)

#######################################################################################################################

class User:

    # Constructor
    def __init__(self, user_id, username):
        print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Matthieu")
user_2 = User("002", "Thomas")

print(user_1)
print(user_1.id)
print(user_1.username)
print(user_1.followers)
print(vars(user_1))

print("initial state")
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
user_1.follow(user_2)
print("user 1 follow user 2")
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)