class ShapeCalculator:
    def area(self,ar1,ar2=None):
        pi = 22.5
        if ar2 is None:
            area =  pi*ar1**2
            print(f"THE AREA OF CIRCLE IS {ar1}")
            return area
        else:
            area =ar1*ar2
            print(f"AREA OF REC WITH LEN{ar1} and WIDT{ar2}:")
            return area
cal = ShapeCalculator()
cal.area(5)
cal.area(3,4)