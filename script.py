class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_nos(self):
    return self.numberOfStudents

  def set_nos(self,new_number):
    self.numberOfStudents = new_number

  def __repr__(self):
    print("A {level} school named {name} with {numberOfStudents} students".format(level = self.level,name = self.name,numberOfStudents = self.numberOfStudents))

class PrimarySchool(School):
  def __init__(self,name,numberOfStudents, pickupPolicy):
    super().__init__(name,"primary",numberOfStudents)
    self.pickupPolicy = pickupPolicy
    
  def get_pick(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + "The pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)


class HighSchool(School):
  def __init__(self,name,numberOfStudents, sportsTeams):
    super().__init__(name,"high",numberOfStudents)
    self.sportsTeams = sportsTeams
    
  def get_sports(self):
    return self.sportsTeams

  def __repr__(self):
    sportsTeams = super().__repr__()
    return sportsTeams + "The sport teams are {sportsTeams}".format(sportsTeams = self.sportsTeams)


s1= School("Hogwarts","primary",300)
print(s1.get_name())
print(s1.get_level())
print(s1.get_nos())
s1.set_nos(200)
print(s1.get_nos())
s1.__repr__()

s2 = PrimarySchool("Hogwarts_Junior",300,"Send by Hogwarts_Express")
print(s1.get_name())
print(s2.get_level())
print(s2.get_nos())
print(s2.get_pick())


s3 = HighSchool("Hogwarts_High",500,["Gryffindor, Slytherin", "Ravenclaw", "Hufflepuff"])
print(s3.get_name())
print(s3.get_level())
print(s3.get_nos())
print(s3.get_sports())
