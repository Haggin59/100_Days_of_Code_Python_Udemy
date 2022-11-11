class User:
    def __init__(self,username,id):  #constructor for initialisation
        #print("New user created")
        self.username = username
        self.id = id
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("haggin","007") 
user_2 = User("Ann","006")
user_3 = User("neon","001")

# user_1.id = "001"
# user_1.username = "Bob"

# print(user_1.username)
# print(user_1.id)
print(user_1.followers)
print(user_2.following)

user_2.follow(user_1)
user_1.follow(user_2)
user_3.follow(user_1)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)




