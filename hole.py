class Hole():
    def __init__(self):
        self.hole_percent = 0
        self.hole_full = ['', '']
        self.hole_suit = ['', '']
        self.hole_card = ['', '']
        self.pos = hole_pos()

        self.hand_val = 0

        
        self.hand_rank = 0
        self.hand_outs = 0
        self.outs_por = 0
        
        self.flush_naipe = 0
        self.str_min_card = 0
        self.pair_card = 0

    def HolePercent(self):
        s = list()
        c = list()
        
        if CARDS_DIC[self.hole_full[0][0]] > CARDS_DIC[self.hole_full[1][0]]:
            c.append(self.hole_full[0][0])
            c.append(self.hole_full[1][0])
        else:
            c.append(self.hole_full[1][0])
            c.append(self.hole_full[0][0])

        s.append(self.hole_full[0][1])
        s.append(self.hole_full[1][1])

        f_hand = ''
        f_hand += c[0]
        f_hand += c[1]
        if s[0] == s[1]:
            f_hand += 's'
        else:
            f_hand += 'o'
        
        f_hand = np.where(HOLE_RANK == f_hand)  
        
        self.hole_percent = int(100 - (f_hand[0][0] * 0.5952))

    def UpdateOutsPercent(self, breakcounter):
        self.outs_por = (float(self.hand_outs)/float(CARDS_LEFT[breakcounter]))*100
 
class Board():
    def __init__(self):
        self.suit_check = [0, 0, 0, 0]              # suit_check    -   suit_check
        self.suit_index = [0, 0, 0, 0]              # suit_index  -   suit_index
        self.str_check = [0, 0, 0, 0]               # str_check     -   str_check
        self.str_index = [0, 0, 0, 0]               # str_index   -   str_index
        self.pair_check = [0, 0, 0, 0]              # pair_check          -   pair_check
        self.pair_index = [0, 0, 0, 0]              # pair_index        -   pair_index
        self.board = ['', '', '', '', '', '']
        self.board_pos = board_pos()
    
    def UpdateBoard(self, breakcounter):
        if breakcounter == 1:
            for x in range(1,4):   
                while(self.board[x] == False or self.board[x] == ''):
                    self.board[x] = read_hole(crop_img(GetFrame(coor=TABLECOOR), self.board_pos[x]))
                    
        if breakcounter > 1 and breakcounter < 4:
            x = breakcounter + 2
            print('board ',x)
            while(self.board[x] == False or self.board[x] == ''):
                self.board[x] = read_hole(crop_img(GetFrame(coor=TABLECOOR), self.board_pos[x]))
    
    def UpdateBoardStats(self, t):
        count = 0
        pair_check = 0
        pair_index = 0
        suit_check = 0
        board_cards, board_suit = break_cards(self.board)
        suit_count = [0, 0, 0, 0]
        pair_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        cards_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        board_str_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        board_cards_val = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        gutshot = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        
        if True:                            # BOARD SUIT VALUES.
            for x in board_suit:
                if x != '':
                    suit_count[SUIT_DIC[x]] += 1
                    count += 1
            
            if count == 3:                # FLOP
                if suit_count.count(1) == 3:
                    suit_check = 0
                elif suit_count.count(2) == 1:
                    suit_check = 1
                elif suit_count.count(3) == 1:
                    suit_check = 3
            
            if count == 4:                # TURN
                if suit_count.count(2) == 2:
                    suit_check = 2
                elif suit_count.count(3) == 1:
                    suit_check = 3
                elif suit_count.count(4) == 1:
                    suit_check = 4
                elif suit_count.count(2) == 1:
                    suit_check = 1
                else:
                    suit_check = 0
                    
            if count == 5:                # RIVER
                if suit_count.count(5) == 1:
                    suit_check = 5
                elif suit_count.count(4) == 1:
                    suit_check = 4
                elif suit_count.count(3) == 1:
                    suit_check = 3
                else:
                    suit_check = 0
        # BOARD SUIT VALUES END.
        
        if True:                            # BOARD CARDS VALUES.
            for x in board_cards:
                if x != '':
                    cards_count[CARDS_DIC[x]] += 1
                    if x == 'A':
                        cards_count[0] += 1
                    
            for x in range(len(cards_count)):
                count = 0
                if cards_count[x] > 0:
                    board_str_counter[x] += 1 
                    while True:
                        count += 1
                        if (x+count) < 13:
                            if cards_count[x+count] > 0:
                                board_str_counter[x] += 1   
                            elif cards_count[x+count+1] > 0 and not gutshot[x]:
                                board_str_counter[x] += 2 
                                count += 1
                                gutshot[x] = True
                            else:
                                break
                        elif (x+count) == 13:
                            if cards_count[x+count] > 0:
                                board_str_counter[x] += 1 
                        else:
                            break
                            
            max = fmax(board_str_counter)

            for x in range(len(board_str_counter)):
                if board_str_counter[x] >= 5:
                    if not gutshot[x]:
                        board_cards_val[x] = 5
                    if gutshot[x]:
                        board_cards_val[x] = 2
     
                elif board_str_counter[x] == 4:
                    if not gutshot[x]: 
                        if x < 11 and x > 0:
                            board_cards_val[x] = 4   
                        else:
                            board_cards_val[x] = 3
                    elif len(self.board) < 4:
                        board_cards_val[x] = 1
                    else:
                        board_cards_val[x] = 0
                        
                        
                elif board_str_counter[x] == 3 and not gutshot[x]: # > 0 and < 11 == espaco pra up down    
                    board_cards_val[x] = 1   
        # BOARD CARDS VALUES END.
        
        if True:                            # BOARD PAIRS VALUES.   pair_check
            for x in board_cards:
                if x != '':
                    pair_count[CARDS_DIC[x]] += 1
                    if x == 'A':
                        pair_count[0] += 1
                        
            if fmax(pair_count) == 4:
                pair_check = 7            # quad
                pair_index = fmax_index(pair_count)
            
            elif fmax(pair_count) == 3 and fmax(pair_count, 2) == 2:
                pair_check = 6            # FULLHOUSE
                pair_index = fmax_index(pair_count)
            elif fmax(pair_count) == 3:
                pair_check = 3            # TRIPLE
                pair_index = fmax_index(pair_count)
            
            elif fmax(pair_count) == 2 and pair_count.count(2) == 2:
                pair_check = 2            # 2 PAIRS
                pair_index = fmax_index(pair_count)
            
            elif fmax(pair_count) == 2 and pair_count.count(2) == 1:
                pair_check = 1               # 1 PAIR
                pair_index = fmax_index(pair_count)
            
            else:
                pair_check = 0            # NOTHING
                pair_index = False

                
        #                   MAX INDEX 13
        #       STRAIGHT                    SUITS    
        # 0 = RAINBOW                   RAINBOW
        # 1 = BACKDOOR                  BACKDOOR
        # 2 = GUTSHOT                   DOUBLE BACKDOOR
        # 3 = STRAIGHT DRAW 1 SIDE      FLUSHDRAW 2 NEEDED
        # 4 = UPDOWN STRAIGHT DRAW      FLUSHDRAW 1 NEEDED
        # 5 = STRAIGHT MADE             FLUSH MADE

        if fmax(board_cards_val) == -1:
            board_cards_val[fmax_index(board_str_counter)] = 0
        
        self.suit_check[t.breakcounter] = suit_check
        self.suit_index[t.breakcounter] = fmax_index(suit_count)
        self.str_check[t.breakcounter] = board_cards_val[fmax_index(board_str_counter)]
        self.str_index[t.breakcounter] = fmax_index(board_str_counter)
        self.pair_check[t.breakcounter] = pair_check
        self.pair_index[t.breakcounter] = pair_index
    
    def ResetBoard(self):
        self.suit_check = [0, 0, 0, 0]
        self.suit_index = [0, 0, 0, 0]
        self.str_check = [0, 0, 0, 0]
        self.str_index = [0, 0, 0, 0]
        self.pair_check = [0, 0, 0, 0]
        self.pair_index = [0, 0, 0, 0]
        self.board = ['', '', '', '', '', '']
   
    def MaxCard(self): # return CARDS_DIC code
        c, s = break_cards(self.board)
        max = 0
        for x in c:
            if x != '':
                if CARDS_DIC[x] > max:
                    max = CARDS_DIC[x]
                
        return max