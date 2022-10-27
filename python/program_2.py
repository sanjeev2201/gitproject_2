print("i am using second own branch.")
class Cex_Driver:
    def __init__(self,name,status) -> None:
        self.name=name
        self.status=status
    def get_disp(self):
        print(f"{self.name} is {self.status} now")
        
n=0
while True:
    Cex=Cex_Driver("Sanjeev","active")
    Cex.get_disp()
    n+=1
    if n==2:
        break
print(f".................")   
print("Bye")
