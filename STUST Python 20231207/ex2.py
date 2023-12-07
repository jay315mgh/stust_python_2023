class Sports:
    def __init__(self,name):
        self._name = name
        
    @property
    def sports_name(self):
        return self._name
    
    @sports_name.setter
    def sports_name(self, value):
        self._name = value
        
class LandSports(Sports):
    def __init__(self,name, field):
        super().__init__(name)
        self._field = field
        
    @property
    def landsports_field(self):
        return self._field
    
    def practice(self):
        print("doing land spports practice")
        
        
class WaterSports(Sports):
    def __init__(self,name, activity):
        super().__init__(name)
        self._activity = activity
        
if __name__ == "__main__":
    
    baseball = LandSports("baseball","basball field")
    print(baseball.sports_name)
    print(baseball.landsports_field)
    
    water_skiing = WaterSports("Water Skiing","")