"""Database models"""
from app import db
class todoList(db.Model):
    """this class represent the todotask table"""
    __tablename__ = "todoTask"
    
    id = db.Column(db.Integer, primary_key=True,unique=True)
    title = db.Column(db.String(225))
    description = db.Column(db.Text)
    done = db.Column(db.Boolean())

    def __init__(self,title,description,done):
        # self.id = id
        self.title = title
        self.description = description
        self.done = done
    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    @staticmethod    
    def get_all():
        return todoList.query.all()    


