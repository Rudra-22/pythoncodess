class Appliance:
    def __init__(self,name):
        self.name = name
    def status(self):
        print(f"{self.name} is on ")
class Fan (Appliance):
    def status(self):
        print(f"{self.name} is on high speed ")
class Light(Appliance):
     def status(self):
        print(f"{self.name} is on  ")
class AC(Appliance):
    def status(self):
        print(f"{self.name} is not working propely with low cooling")
app =[Fan ("orphic celling fan"),
      Light ("WALL LIGHT "),
      AC ("WHIRPOOL AC")]
for appliance in app:
    appliance.status()


