class Check():
    def __str__(self):
        return "\n\n\nTable()\nPot: "+str(self.table.pot)+"\nDealer: "+str(self.table.dealer)+"\nLimp: "+str(self.table.limp)+"\nLimpCount: "+str(self.table.limp_count)+"\nBets: "+str(self.table.bets)+"\nBetPos: "+str(self.table.bets_pos)+"\nTo call: "+str(self.table.to_call)+"\nPot odds %: "+str(self.table.pot_odds_per)+"\nAllin Count: "+str(self.table.allin_count)+"\n\nBoard()\nBoardSuitVal: "+str(self.board.suit_check)+"\nBoardStrVal: "+str(self.board.str_check)+"\nBoardPairVal: "+str(self.board.pair_check)+"\nBoardSuitIndex: "+str(self.board.suit_index)+"\nBoardStrIndex: "+str(self.board.str_index)+"\nBoardPairIndex: "+str(self.board.pair_index)+"\nBoardFull: "+str(self.board.board)+"\n\nPlayer()\nposition: "+str(self.players.position)+"\n\nHole()\nHoleFull: "+str(self.hole.hole_full)+"\nHoleSuit: "+str(self.hole.hole_suit)+"\nHoleCard: "+str(self.hole.hole_card)+"\nHole_%: "+str(self.hole.hole_percent)+"\nHandRank: "+str(self.hole.hand_rank)+"\nHandOuts: "+str(self.hole.hand_outs)+"\nFlushNaipe: "+str(self.hole.flush_naipe)+"\nStrMinCard: "+str(self.hole.str_min_card)+"\nPairCard: "+str(self.hole.pair_card)+"\nOuts%: "+str(self.hole.outs_por)
        
    def __init__(self):
        pass
    
    def ToCallBB(self):
        try:
            return int(int(self.table.to_call)/int(self.table.bb))
        except:
            return 0
   
    def FullHole(self):
        r = ''
        DIC = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':10,'Q':11,'K':12,'A':13}   

        if DIC[self.hole.hole_card[0]] > DIC[self.hole.hole_card[1]]:
            r += self.hole.hole_card[0]
            r += self.hole.hole_card[1]
        else:
            r += self.hole.hole_card[1]
            r += self.hole.hole_card[0]

        if self.hole.hole_suit[0] == self.hole.hole_suit[1]:
            r += 's'
        else:
            r += 'o'

        return r

    def InBlinds(self):
        if self.players.setor == 'BLINDS':
            return True
        else:
            return False

    def InLate(self):
        if self.players.setor == 'LATE':
            return True
        else:
            return False

    def InMid(self):
        if self.players.setor == 'MID':
            return True
        else:
            return False

    def InEarly(self):
        if self.players.setor == 'EARLY':
            return True
        else:
            return False  
    # Hole Cards Check List
    def IsPocketPair(self):
        if self.hole.hole_card[0] == self.hole.hole_card[1]:
            return True
        else:
            return False
    
    def IsSuited(self):
        if self.hole.hole_suit[0] == self.hole.hole_suit[1]:
            return True
        else:
            return False
    
    def IsConnected(self):
        s = (CARDS_DIC[self.hole.hole_card[0]] - CARDS_DIC[self.hole.hole_card[1]])
        if s == 1 or s == -1:
            return True
        elif self.hole.hole_card[0] == 'A' or self.hole.hole_card[1] == 'A':
            if self.hole.hole_card[0] == '2' or self.hole.hole_card[1] == '2':
                return True
            else:
                return False

    def IsBroadway(self):
        if CARDS_DIC[self.hole.hole_card[0]] >= CARDS_DIC['T'] and CARDS_DIC[self.hole.hole_card[1]] >= CARDS_DIC['T']:
            return True
        else:
            return False
    
    def IsOverpair(self):
        if self.hole.hand_rank > 0 and CARDS_DIC[self.board.pair_index] > self.board.MaxCard():
            return True
        else:
            return False
    
    def HaveOneOverCard(self):
        if CARDS_DIC[self.hole.hole_card[0]] > self.board.MaxCard() or CARDS_DIC[self.hole.hole_card[1]] > self.board.MaxCard():
            return True
        else:
            return False
    
    def HaveTwoOverCards(self):
        if CARDS_DIC[self.hole.hole_card[0]] > self.board.MaxCard() and CARDS_DIC[self.hole.hole_card[1]] > self.board.MaxCard():
            return True
        else:
            return False
    
    def HowManyAboveMyHole(self):
        #c, s = break_cards(self.board.board)
        c, s = self.board.BreakBoardCards()
        counter = 0
        for x in c:
            if x != ''and CARDS_DIC[x] > CARDS_DIC[self.hole.hole_card[0]] or CARDS_DIC[x] > CARDS_DIC[self.hole.hole_card[1]]:
                counter += 1
                
        return counter

    def InPosition(self):
        Pos = [2, 1, 9, 8, 7, 6, 5, 4, 3] # Pos > == BETTER position
        max = 0
        max_seat = 0 # SEAT NUMBER IN THE TABLE 
        
        for p in self.table.players_in_hand:
            if Pos[self.table.pl[p].position] > max and p != SELF_SEAT:
                max = Pos[self.table.pl[p].position]
                max_seat = p
        
        if Pos[self.table.pl[SELF_SEAT].position] > max:
            return True
        else:
            return False

    def FirstAction(self):
        if self.players.action[self.table.breakcounter] == 'None':
            return True
        else:
            return False

    def CanCheck(self):
        if self.players.can_check:
            return True
        else:
            return False

    def CanCall(self):
        if self.players.can_call:
            return True
        else:
            return False

    def CanFold(self):
        if self.players.can_fold:
            return True
        else:
            return False

    def SBAgainstBB(self):
        Pos = [2, 1, 9, 8, 7, 6, 5, 4, 3]
        for p in self.table.players_in_hand:
            if Pos[self.table.pl[p].position] > 2 and p != SELF_SEAT and self.table.pl[p].is_playing:
                return True
        else:
            return False
    
    def VillanMoreAggressive(self):
        if self.table.breakcounter > 0 and len(self.table.players_in_hand) > 1:
            for p in self.table.players_in_hand:
                if p != SELF_SEAT and self.table.pl[p].points[self.table.breakcounter] > self.table.pl[p].points[self.table.breakcounter-1]:
                    return True
            
            return False

    def AnyAllin(self):
        for p in self.table.players_in_hand:
            if self.table.pl[p].is_allin:
                return True
                
        return False

    def HowManyInHand(self):
        return len(self.table.players_in_hand)-1
    # Board Check List
    def StrImproved(self):
        if self.table.breakcounter >= 2:   # only checks on turn or river.
            if self.board.str_check[self.table.breakcounter] > self.board.str_check[self.table.breakcounter-1]:
                return True
            else:
                return False
                
    def FlsImproved(self):
        if self.table.breakcounter >= 2:   # only checks on turn or river.
            if self.board.suit_check[self.table.breakcounter] > self.board.suit_check[self.table.breakcounter-1]:
                return True
            else:
                return False
   
    def PairImproved(self):
        if self.table.breakcounter >= 2:   # only checks on turn or river.
            if self.board.pair_check[self.table.breakcounter] > self.board.pair_check[self.table.breakcounter-1]:
                return True
            else:
                return False

    def PossibleFlushDraw(self):
        if self.board.suit_check[self.table.breakcounter] >= 3:
            return True
        else:
            return False

    def PossibleStrDraw(self):
        if self.board.str_check[self.table.breakcounter] >= 3:
            return True
        else:
            return False

    def PairOnBoard(self):
        if self.board.pair_check[self.table.breakcounter] >= 1:
            return True
        else:
            return False

    def CallOnce(self):
        if self.FirstAction():
            return 'call'
        else:
            return 'fold'

    def RaiseOnce(self, r):
        if self.FirstAction():
            return str(r)
        else:
            return 'fold'

    def HavePotOddsToCall(self):
        if self.table.pot_odds_per <= self.hole.outs_por and not self.players.can_check:
            return True
        else:
            return False

    def StrDraw(self):
        if self.board.str_check[self.table.breakcounter] == 3 or self.board.str_check[self.table.breakcounter] == 4:
            return True
        else:
            return False
    
    def FshDraw(self):
        if self.table.suit_check == 3 or self.table.suit_check == 4:
            return True
        else:
            return False

    def HaveFshDraw(self):
        if self.board.suit_check[self.table.breakcounter] == 3 or self.board.suit_check[self.table.breakcounter] == 4 and self.board.suit_index == self.hole.flush_naipe:
            return True
        else:
            return False

    def HaveStrDraw(self):
        pass

