class Check():
    def __str__(self):
        return "\n\n\nTable()\nPot: "+str(self.t.pot)+"\nDealer: "+str(self.t.dealer)+"\nLimp: "+str(self.t.limp)+"\nLimpCount: "+str(self.t.limp_count)+"\nBets: "+str(self.t.bets)+"\nBetPos: "+str(self.t.bets_pos)+"\nTo call: "+str(self.t.to_call)+"\nPot odds %: "+str(self.t.pot_odds_per)+"\nAllin Count: "+str(self.t.allin_count)+"\n\nBoard()\nBoardSuitVal: "+str(self.b.suit_check)+"\nBoardStrVal: "+str(self.b.str_check)+"\nBoardPairVal: "+str(self.b.pair_check)+"\nBoardSuitIndex: "+str(self.b.suit_index)+"\nBoardStrIndex: "+str(self.b.str_index)+"\nBoardPairIndex: "+str(self.b.pair_index)+"\nBoardFull: "+str(self.b.board)+"\n\nPlayer()\nposition: "+str(self.p.position)+"\n\nHole()\nHoleFull: "+str(self.h.hole_full)+"\nHoleSuit: "+str(self.h.hole_suit)+"\nHoleCard: "+str(self.h.hole_card)+"\nHole_%: "+str(self.h.hole_percent)+"\nHandRank: "+str(self.h.hand_rank)+"\nHandOuts: "+str(self.h.hand_outs)+"\nFlushNaipe: "+str(self.h.flush_naipe)+"\nStrMinCard: "+str(self.h.str_min_card)+"\nPairCard: "+str(self.h.pair_card)+"\nOuts%: "+str(self.h.outs_por)

        
    def __init__(self, t, p, b, h):
            # t.pot = POT AMMOUNT
            # t.dealer = DEALER POSITION
            # t.to_call = TO CALL AMMOUNT
            # t.pot_odds_per = POT ODDS %
            # t.allin_count
            # t.limp = Bool if there is limps/calls
            # t.limp_count = how many limp/calls
            # t.bets = Bool if there is bets/reraise
            # t.bets_pos = earliest bet position
            # t.players_in_hand = in_hand after hand_order()
        self.t = t

            
            # b.suit_check = {0:'RAINBOW', 1:'BACKDOOR', 2:'DOUBLE BACKDOOR', 3:'FSH DRAW 2 NEEDED', 4:'FSH DRAW 1 NEEDED', 5:'FLUSH MADE'}
            # b.str_check = {0:'NOTHING', 1:'BACKDOOR', 2:'GUTSHOT', 3:'1 SIDE STR DRAW', 4:'UPDOWN STR DRAW', 5:'STRAIGHT MADE'}
            # b.pair_check = {0:'NOTHING', 1:'PAIR', 2:'2 PAIRS', 3:'TRIPLE', 4:'FULLHOUSE', 5:'QUAD'}
    
            # b.suit_index = {0:'c', 1:'d', 2:'s', 3:'h'}
            # b.str_index = {0:'A', 1:'2', 2:'3', 3:'4', 4:'5', 5:'6', 6:'7', 7:'8', 8:'9', 9:'T', 10:'J', 11:'Q', 12:'K', 13:'A'}
            # b.pair_index = {0:'A', 1:'2', 2:'3', 3:'4', 4:'5', 5:'6', 6:'7', 7:'8', 8:'9', 9:'T', 10:'J', 11:'Q', 12:'K', 13:'A'}
        
            # b.board = ['', '', '', '', ''] Board Cards
        self.b = b
            
            
            # p.position = 0=BB 9=UTG
            # POSITION_DICT = {0:'BB', 1:'SB', 2:'BU', 3:'CO', 4:'HJ', 5:'MP+1', 6:'MP', 7:'UTG+1', 8:'UTG'}
            # p.setor = blinds, late, mid, early
            # p.can_call
            # p.can_fold
            # p.can_check
            # p.can_raise
        self.p = p
        
            
            # h.hole_full = ['', '']  HOLE CARDS FULL STRING 'Ad'
            # h.hole_suit = ['', '']  HOLE CARDS SUIT ONLY. 'd'
            # h.hole_card = ['', '']  HOLE CARDS CARD ONLY. 'A'
            # h.hole_percent = HAND % (27o  0 - 100 AA )
            # h.hand_rank = HAND's RANK  {0:'NOTHING', 1:'PAIR', 2:'2 PAIRS', 3:'TRIPLE', 4:'STRAIGHT', 5:'FLUSH', 6:'FULLHOUSE', 7:'QUAD', 8:'STRAIGHT FLUSH', 9:'ROYAL FLUSH'}
            # h.hand_outs = HOW MANY OUTS WE HAVE
            # h.flush_naipe = FMAX_INDEX NAIPE OF THE HAND
            # h.str_min_card = MIN CARD FROM STRAIGHT - IF NOT STRAIGHT, USELESS
            # h.pair_card = CARD THAT PAIRED
            # h.outs_por = % of hitting outs
        self.h = h
    
    def ToCallBB(self):
        try:
            return int(int(self.t.to_call)/int(self.t.bb))
        except:
            return 0
   
    def FullHole(self):
        r = ''
        DIC = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':10,'Q':11,'K':12,'A':13}   

        if DIC[self.h.hole_card[0]] > DIC[self.h.hole_card[1]]:
            r += self.h.hole_card[0]
            r += self.h.hole_card[1]
        else:
            r += self.h.hole_card[1]
            r += self.h.hole_card[0]

        if self.h.hole_suit[0] == self.h.hole_suit[1]:
            r += 's'
        else:
            r += 'o'

        return r

    def InBlinds(self):
        if self.p.setor == 'BLINDS':
            return True
        else:
            return False

    def InLate(self):
        if self.p.setor == 'LATE':
            return True
        else:
            return False

    def InMid(self):
        if self.p.setor == 'MID':
            return True
        else:
            return False

    def InEarly(self):
        if self.p.setor == 'EARLY':
            return True
        else:
            return False  
    # Hole Cards Check List
    def IsPocketPair(self):
        if self.h.hole_card[0] == self.h.hole_card[1]:
            return True
        else:
            return False
    
    def IsSuited(self):
        if self.h.hole_suit[0] == self.h.hole_suit[1]:
            return True
        else:
            return False
    
    def IsConnected(self):
        s = (CARDS_DIC[self.h.hole_card[0]] - CARDS_DIC[self.h.hole_card[1]])
        if s == 1 or s == -1:
            return True
        elif self.h.hole_card[0] == 'A' or self.h.hole_card[1] == 'A':
            if self.h.hole_card[0] == '2' or self.h.hole_card[1] == '2':
                return True
            else:
                return False

    def IsBroadway(self):
        if CARDS_DIC[self.h.hole_card[0]] >= CARDS_DIC['T'] and CARDS_DIC[self.h.hole_card[1]] >= CARDS_DIC['T']:
            return True
        else:
            return False
    
    def IsOverpair(self):
        if self.h.hand_rank > 0 and CARDS_DIC[self.b.pair_index] > self.b.MaxCard():
            return True
        else:
            return False
    
    def HaveOneOverCard(self):
        if CARDS_DIC[self.h.hole_card[0]] > self.b.MaxCard() or CARDS_DIC[self.h.hole_card[1]] > self.b.MaxCard():
            return True
        else:
            return False
    
    def HaveTwoOverCards(self):
        if CARDS_DIC[self.h.hole_card[0]] > self.b.MaxCard() and CARDS_DIC[self.h.hole_card[1]] > self.b.MaxCard():
            return True
        else:
            return False
    
    def HowManyAboveMyHole(self):
        c, s = break_cards(self.b.board)
        counter = 0
        for x in c:
            if x != ''and CARDS_DIC[x] > CARDS_DIC[self.h.hole_card[0]] or CARDS_DIC[x] > CARDS_DIC[self.h.hole_card[1]]:
                counter += 1
                
        return counter

    def InPosition(self):
        Pos = [2, 1, 9, 8, 7, 6, 5, 4, 3] # Pos > == BETTER position
        max = 0
        max_seat = 0 # SEAT NUMBER IN THE TABLE 
        
        for p in self.t.players_in_hand:
            if Pos[self.t.pl[p].position] > max and p != SELF_SEAT:
                max = Pos[self.t.pl[p].position]
                max_seat = p
        
        if Pos[self.t.pl[SELF_SEAT].position] > max:
            return True
        else:
            return False

    def FirstAction(self):
        if self.p.action[self.t.breakcounter] == 'None':
            return True
        else:
            return False

    def CanCheck(self):
        if self.p.can_check:
            return True
        else:
            return False

    def CanCall(self):
        if self.p.can_call:
            return True
        else:
            return False

    def CanFold(self):
        if self.p.can_fold:
            return True
        else:
            return False

    def SBAgainstBB(self):
        Pos = [2, 1, 9, 8, 7, 6, 5, 4, 3]
        for p in self.t.players_in_hand:
            if Pos[self.t.pl[p].position] > 2 and p != SELF_SEAT and self.t.pl[p].is_playing:
                return True
        else:
            return False
    
    def VillanMoreAggressive(self):
        if self.t.breakcounter > 0 and len(self.t.players_in_hand) > 1:
            for p in self.t.players_in_hand:
                if p != SELF_SEAT and self.t.pl[p].points[self.t.breakcounter] > self.t.pl[p].points[self.t.breakcounter-1]:
                    return True
            
            return False

    def AnyAllin(self):
        for p in self.t.players_in_hand:
            if self.t.pl[p].is_allin:
                return True
                
        return False

    def HowManyInHand(self):
        return len(self.t.players_in_hand)-1
    # Board Check List
    def StrImproved(self):
        if self.t.breakcounter >= 2:   # only checks on turn or river.
            if self.b.str_check[self.t.breakcounter] > self.b.str_check[self.t.breakcounter-1]:
                return True
            else:
                return False
                
    def FlsImproved(self):
        if self.t.breakcounter >= 2:   # only checks on turn or river.
            if self.b.suit_check[self.t.breakcounter] > self.b.suit_check[self.t.breakcounter-1]:
                return True
            else:
                return False
   
    def PairImproved(self):
        if self.t.breakcounter >= 2:   # only checks on turn or river.
            if self.b.pair_check[self.t.breakcounter] > self.b.pair_check[self.t.breakcounter-1]:
                return True
            else:
                return False

    def PossibleFlushDraw(self):
        if self.b.suit_check[self.t.breakcounter] >= 3:
            return True
        else:
            return False

    def PossibleStrDraw(self):
        if self.b.str_check[self.t.breakcounter] >= 3:
            return True
        else:
            return False

    def PairOnBoard(self):
        if self.b.pair_check[self.t.breakcounter] >= 1:
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
        if self.t.pot_odds_per <= self.h.outs_por and not self.p.can_check:
            return True
        else:
            return False

    def StrDraw(self):
        if self.b.str_check[self.t.breakcounter] == 3 or self.b.str_check[self.t.breakcounter] == 4:
            return True
        else:
            return False
    
    def FshDraw(self):
        if self.t.suit_check == 3 or self.t.suit_check == 4:
            return True
        else:
            return False

    def HaveFshDraw(self):
        if self.b.suit_check[self.t.breakcounter] == 3 or self.b.suit_check[self.t.breakcounter] == 4 and self.b.suit_index == self.h.flush_naipe:
            return True
        else:
            return False

    def HaveStrDraw(self):
        pass


            
    # why = ''
    # acao = {'passive':'', 'normal':'', 'agressive':''}
    
    # {'fold', 'call', 'bet', '3x', '40%', '45%', '55%', '65%'}
    
    
    
    # Position Check
    # POSITION_DICT = {0:'BB', 1:'SB', 2:'BU', 3:'CO', 4:'HJ', 5:'MP+1', 6:'MP', 7:'UTG+1', 8:'UTG'}
# CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES 
# CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES 