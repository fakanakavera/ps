class Table(): # NEW
    def __init__(self):
        # self.board = Board()
        #self.in_hand = 0
        pass

    def __str__(self):
        os.system('cls')
        print('Hand number ',self.table.hand_num,' - ',self.table.hand_num_old)
        print('$'*20,' ',STREET[self.table.breakcounter],' ','$'*20)
        print("Board\nFlop: %s %s %s\nTurn: %s\nRiver: %s\n" % (self.board.board[1], self.board.board[2], self.board.board[3], self.board.board[4], self.board.board[5]))
        print('Pot: ',self.table.pot)
        print('limps ',self.table.limp,' - ',self.table.limp_count)
        print('bets ',self.table.bets,' - ',self.table.bets_pos)
    
    def UpdateHandOrder(self):
        # Update self.in_hand here
        pass

    def GetFrame(self):
        pass
        
    def UpdatePot(self):
        pass
        
    def UpdateDealer(self): 
        pass
    
    def UpdateHandNum(self):
        pass

    def GetHandNum(self):
        pass

    def WaitForCards(self):
        pass

    def ResetAllinCount(self):
        pass

    def ResetData(self):
        pass

    def ResetStreet(self):
        pass
          
    def WaitFastFold(self):
        pass
          
    def UpdateToCall(self): # (1096, 886, 201, 42) to allin call
        pass

    def UpdatePotOdds(self):
        pass
 