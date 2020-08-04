from Comment import *
from Status import *
from User import *

class Facebook:

    #__init__: dict, list-Of-Strings, string 
    def __init__ (self):

        #instance variables

        self.UsersDict = {}
        self.statusList = []
        self.currentUser = ''

    #special method

    #registerUser: name, email -> void
    def registerUser (self, name, email):
        if name in self.UsersDict:
            print ('There is already an user with the same name')
        else:
            self.UsersDict[name] = User(name, email)

    #login: name -> void
    def login (self, name):
        if self.currentUser == '':
            self.currentUser = name
        else:
            print('There is already a logged in user')

    #logout: void -> void
    def logout (self):
        if self.currentUser == '':
            print ('There is no user at the moment')
        else:
            self.currentUser = ''

    #addFriend: name -> void
    def addFriend (self, name):
        if self.currentUser == '':
            print ('There is no user logged in at the time')
        elif name not in self.UsersDict:
            print ('There is no user with the given name')
        else:
            self.UsersDict[self.currentUser].addFriend(self.UsersDict[name])
            self.UsersDict[name].addFriend(self.UsersDict[self.currentUser])

    #viewProfile: void -> void
    def viewProfile (self):
        print (self.UsersDict[self.currentUser])
        
    #postStatus: status -> void
    def postStatus (self, status):
        if self.currentUser == '':
            print ('There is no user logged in at the time')
        else:
            statusObject = Status(self.currentUser, status)
            self.statusList.append(statusObject)

    #viewStatus: void -> void
    def viewStatus (self):
        if self.currentUser == '':
            print ('There is no user logged in at the time')
        else:
            for i in self.statusList:
                if self.UsersDict[i.getName()].isFriend(self.UsersDict[self.currentUser]) == True or i.getName() == self.currentUser:
                    print ('(' + str(self.statusList.index(i)) + ') ' + str(i))

    #likeStatus: status-ID-number -> void
    def likeStatus (self, statusIDnum):
        if self.currentUser == '':
            print ('There is no user logged in at the time')
        elif self.UsersDict[self.statusList[statusIDnum].getName()].isFriend(self.UsersDict[self.currentUser]) == True or self.statusList[statusIDnum].getName() == self.currentUser:
            self.statusList[statusIDnum].addLike(self.currentUser)
        else:
            print('Cannot like this status')

    #commentOnStatus: int, str -> void
    def commentOnStatus (self, statusIDnum, comment):
        if self.currentUser == '':
            print ('There is no user logged in at the time')
        elif self.UsersDict[self.statusList[statusIDnum].getName()].isFriend(self.UsersDict[self.currentUser]) == True or self.statusList[statusIDnum].getName() == self.currentUser:
            commentObject = Comment(self.currentUser, comment)
            self.statusList[statusIDnum].addComment(commentObject)
        else:
            print ('Cannot comment on this status')
        
    
            
        
        
        
        
