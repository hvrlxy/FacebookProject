class User:

    #__init__: string, string, list-Of-String
    def __init__ (self, user, email):
        self.user = user
        self.email = email
        self.friendlist = []

    #accessor method

    #getName: void -> string
    def getUser (self):
        return self.user

    #getEmail: void -> string
    def getEmail (self):
        return self.email

    #getFriendlist: void -> string
    def getFriendlist (self):
        return self.friendlist

    #mutator method

    #setName: string -> void
    def setUser (self, newUser):
        self.user = newUser

    #setEmail: string -> void
    def setEmail (self, newEmail):
        self.email = newEmail

    #setFriendlist: string -> void
    def setFriendlist (self, newFriend):
        self.friendlist = newFriend

    #addFriend: friend -> void
    def addFriend (self, user):
        self.friendlist.append(user)

    #isFriend: string -> boolean
    def isFriend (self, user):
        if user in self.friendlist:
            return True
        else:
            return False

    # __str__: -> string
    def __str__ (self):
        userInfo = str(self.user) + ' ' + '(' + str(self.email) +')' + '\n'
        friendInfo = ''
        acc = ''
        for i in self.friendlist:
            acc = acc + str(i.getUser()) + ', '
        friendInfo = 'Friends: ' + acc [:-2]
        return userInfo + friendInfo
            
    
        
