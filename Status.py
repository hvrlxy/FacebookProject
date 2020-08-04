from Comment import *
class Status:

    #__init__: string, string, list-Of-Strings, list-Of-String
    def __init__ (self, name, status):
        self.name = name
        self.status = status
        self.like = []
        self.Comment = []

    #accessor method

    #getName: void -> string
        
    def getName (self):
        return self.name

    #getStatus: void -> string
    
    def getStatus (self):
        return self.status

    #getLike: void -> string
    
    def getLike (self):
        return self.like

    #getComment: void -> string
    
    def getComment (self):
        return self.Comment

    #mutator method

    #setName: string -> void

    def setName (self, newName):
        self.name = newName

    #setStatus: string -> void

    def setStatus (self, newStatus):
        self.status = newStatus

    #setLike: string -> void

    def setLike (self, newLike):
        self.like = newLike

    #setComment: string -> void

    def setComment (self, newComment):
        self.Comment = newComment

    #addLike: name who like -> void

    def addLike (self, newLike):
        self.like.append(newLike)

    #addComment: comment -> void

    def addComment (self, newComment):
        if newComment == '':
            print ('You cannot add this comment')
        else:
            self.Comment.append(newComment)

    # __str__: -> string

    def __str__ (self):
        statusInfo = str(self.name) + ' ' + str(self.status) + '\n'
        likeInfo = ''
        commentInfo = ''
        acc1 = ''
        acc2 = ''
        for i in self.like:
            if len(self.like) == 1:
                likeInfo = self.like[0] + ' likes this' + '\n'
            else:
                acc1 = acc1 + str(i) + ' ,'
                likeInfo = acc1[:-2] + ' like this' + '\n'
        for i in self.Comment:
            acc2 = acc2 + str(i) + '\n'
            commentInfo = acc2
        return statusInfo + likeInfo + commentInfo
        
        
