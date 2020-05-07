from src.main.player import Player

class Game:
    
    def _init_ (self,player1:Player,player2:Player):
        self.player1 = player1
        self.player2 = player2
        
    def get_score(self)->str:
        points_p1 = self.player1.get_points()
        points_p2 = self.player2.get_points()
        
        
        if points_p1 == points_p2:
            
          if points_p1 == 3 or points_p1 == 4:
              return "Deuce"
          
          if points_p1 == 2:
              return "Thirty-All"
          
          if points_p1 == 1:
              return "Fifteen-All"
          
          if points_p1 == 0:
              return "Love-All"
          
          
        
        if points_p1>points_p2:
            
            if points_p1 == 3:
                if points_p2 == 0:
                    return "Forty-Love"
                
                if points_p2 == 1:
                    return "Forty-Fifteen"
                
                else:
                    return "Forty-Thirty"
                
            if points_p1 == 2: 
                if points_p2 == 0:
                    return "Thirty-Love"

                else:
                    return "Thirty-Fifteen"
            
            if points_p1 == 1:
                return "Fifteen-Love"
            
            if points_p1 >= 4 and points_p2 == (points_p1-1):
                return "Advantage player1"
            
            else:
                return "Win for player1"
            
            
            
        if points_p2>points_p1:
            
            if points_p2 == 3:
                if points_p1 == 0:
                    return "Love-Forty"
                
                if points_p1 == 1:
                    return "Fifteen-Forty"
                
                else:
                    return "Thirty-Forty"
                
            if points_p2 == 2:
                if points_p1 == 0:
                    return "Love-Thirty"
                
                else:
                    return "Fifteen-Thirty"
                
                
            if points_p2 == 1:
                return "Love-Fifteen"
            
            if points_p2 > 3 and points_p1 == (points_p2-1):
                return "Advantage player2"
            
            else:
                return "Win for player2"
        
              
            
    def won_point(self,player:Player)->None:
        
        if self.player1.is_equal(player):
            self.player1.add_point()
        else:
            self.player2.add_point()
