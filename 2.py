class Device:
    def __init__(self,device_id,model):
        self.device_id = device_id
        self.model = model
    def displ(self):
        print(f"{self.device_id} with model {self.model}")
class Flyer:
    def fly(self):
        print("THE DRONE IS FLYING")
class Drone(Device,Flyer):
       def __init__(self, device_id, model):
            super().__init__(device_id, model)
       def capture(self):
            print("THE DRONE IS CAPTURING THE PICTURES")
drone = Drone("D091","HIOEW")
drone.displ()
drone.fly()        
