class Student:
  #[assignment] Skeleton class. Add your code here
    def __init__(self, name:str, age:int, track:list, score:float):
        self.name = name
        self.age  = age 
        self.track  = track 
        self.score = score


    def change_name(self,name:str):
        self.name = name
        return self.name  

    def change_age(self, age:int):
        self.age = age
        return self.age 

    def add_track(self, track:list):
        self.track.append(track) 
        return self.track

    def get_score(self, score:float):
        return self.score

Bob = Student(name="Bob",age=26, track=["FE","BE"], score=20.90)


Kayla = Student(name="Kayla", age=21, track=["Html"], score= 7.0) 



 
# Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()



print(Bob.change_name("Kayla"))
print (Bob.change_age(21))
print (Bob.add_track(""))
print(Bob.get_score())
