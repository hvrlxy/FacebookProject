class Comment:
    
    #__init__: List of strings, list of strings -> void

    def __init__(self, commentor, comment):
        self.commentor = commentor
        self.comment = comment

    #getCommentor: void -> string
        
    def getCommentor (self):
        return self.commentor

    #getComment: void -> string
    
    def getComment (self):
        return self.comment

    #setCommentor: string -> void
    
    def setCommentor (self, newCommentor):
        self.commentor = newCommentor

    #setComment: string -> void

    def setComment (self, newComment):
        self.comment = newComment

    #__str__: -> string
        
    def __str__ (self):
        return str(self.commentor) + ': ' + str(self.comment)
        
        
