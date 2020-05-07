class Player:
    
    def _init_(self,nom:str):
        self.nom = nom
        self.npunts = 0
        
    def get_nom(self)->str:
        return self.nom
    
    def get_points(self)->int:
        return self.npunts
    
    def is_equal(self,player)->bool:
        return self.nom == player.nom
    
    def add_point(self)->None:
        self.npunts = self.npunts+1
        
