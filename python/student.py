def __init__(self, fname, lname, id, energy_level = 10):
    self.fname =fname
    self.lname=lname
    self.id =id
    self.energy_level= energy_level

def __str__(self):
    return f"{self.lname}: {self.id}"

def _greeting_ (self):
    return(f"Hi, My name is {self.fname}{self.lname}!")

def _take_exam_ (self):
    if  self.energy_level > 0:
        self.energy_level-= 1
    else:
       print("energy level is at 0")
       
def get_energy_level(self):
    return self.energy_level


