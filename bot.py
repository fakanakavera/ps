from check import Check
class Bot(Check):
    def __init__(self):
        time.sleep(1)
        print('STARTING...')
        self.table = Table()
        print("table set")
        self.start = time.time()
        self.table.fnkfile = 'logs/'+str(int(time.time()))+'.fnk'
        self.table.dealer_old = self.table.dealer
        self.table.hand_num_old = 0
        self.table.hand_num_old = copy.deepcopy(self.table.hand_num)
        self.hand_list = [self.table.hand_num]
        self.table.breakcounter = -1
        self.constants = []

    def HandPrint(self):
        print(self.table)

    def AddHandList(self):
        if len(self.hand_list) > 5:
            self.hand_list.pop(0)
        self.hand_list.append(self.table.hand_num)

    def WaitDealerDealCards(self):
        card_count = 0    
        while card_count < 2:   # ESPERA DEALER DAR CARTAS
            card_count = 0
            self.table.players = ['', '', '', '', '', '', '', '', '', '']
            for x in range(1,(NPLAYERS+1)): # loop all players                  ***** change NPLAYERS --> self.constants['NPLAYERS']???
                self.table.players[x] = Player(x)
                self.table.players[x].CheckCards()
                if self.table.players[x].have_cards:     # break na primeira vez q achar hole cards
                    card_count += 1

    def SetPlayersObjects(self):
        for x in range(1,(NPLAYERS+1)):   # SETA TODOS PLAYERS
            self.table.players[x] = Player(x)
            self.table.players[x].CheckCards()     # ALTERA SELF.CARDS

            if self.table.players[x].have_cards:              # SE tiver cards.
                self.table.in_hand.append(x)
                self.table.players[x].is_allin = False

    def InHandLoop(self):
        while True:             # so sai desse loop com break
            for index in range(0,len(self.table.players_in_hand)):          # loop de cada street   
                if self.table.players_in_hand[index] != self.jump and len(self.table.in_hand[1]) > 1 and self.table.players[self.table.players_in_hand[index]].is_playing == True and self.table.players[self.table.players_in_hand[index]].is_allin == False:    
                    self.table.ResetStreet()
                    self.table.UpdatePot()
                    self.HandPrint()
                    #print('\n\n',self.table.players_in_hand,'\n\n')
                    
                    
                    

                    if SELF_PLAYING and self.table.players[SELF_SEAT].is_playing: # if im playing
                        self.table.players[SELF_SEAT].cards.HolePercent()
                        print('Hole Cards: ',self.table.players[SELF_SEAT].cards.hole_full[0],' - ',self.table.players[SELF_SEAT].cards.hole_full[1],'  ',self.table.players[SELF_SEAT].cards.hole_percent,'\n')
                        
                        if self.table.breakcounter > 0 and self.table.breakcounter < 3 and self.table.players[SELF_SEAT].is_playing: #nao calcula odds no pre flop
                                giving_hand = [self.table.players[SELF_SEAT].cards.hole_full[0], self.table.players[SELF_SEAT].cards.hole_full[1]]
                                for x in range(1,self.table.breakcounter+3):
                                    giving_hand.append(self.table.board.board[x])
                                    
                                self.table.players[SELF_SEAT].cards.hand_rank, self.table.players[SELF_SEAT].cards.outs_hand, self.table.players[SELF_SEAT].cards.flush_naipe, self.table.players[SELF_SEAT].cards.str_min_card, self.table.players[SELF_SEAT].cards.pair_card = hand_outs(giving_hand)
                                self.table.players[SELF_SEAT].cards.UpdateOutsPercent(self.table.breakcounter)
                                print('HAND RANK ',DICT_FINAL[self.table.players[SELF_SEAT].cards.hand_rank])
                                print('OUTS ',self.table.players[SELF_SEAT].cards.outs_hand,' = ',self.table.players[SELF_SEAT].cards.outs_por,'%')
                            
                    if self.table.breakcounter > 0:# and self.table.players_in_hand[index] == SELF_SEAT:
                        self.table.board.UpdateBoardStats(t)
                        print('BOARD RANK STR', DICT_STR[self.table.board.str_check[self.table.breakcounter]],' ',self.table.board.str_check[self.table.breakcounter])
                        print('BOARD RANK FSH', DICT_FSH[self.table.board.suit_check[self.table.breakcounter]],' ',self.table.board.suit_check[self.table.breakcounter])
                        print('BOARD RANK PAIR', DICT_PAIR[self.table.board.pair_check[self.table.breakcounter]],' ',self.table.board.pair_check[self.table.breakcounter])
                    
                    #print 'ALLIN COUNTER: ',self.table.allin_count
                    
                    if ZOOM and self.table.players[SELF_SEAT].cards.hole_percent < MIN_RANGE and Action() and self.table.players[SELF_SEAT].position > 0 and AUTOPLAYING:
                        if Action():
                            while Action():
                                SendFastFold()
                                print('FastFoldSending.....')
                                time.sleep(0.5)

                            
                        self.zoombreak = True
                        break 
                        
                    else:    
                        print('\nPlayer\tAction\tPosition')
                        for x in range(0,len(self.table.players_in_hand)):
                            #if self.table.players[self.table.players_in_hand[x]].have_cards:
                            if index == x:
                                print('--> ',self.table.players[self.table.players_in_hand[x]])
                            else:
                                print(self.table.players[self.table.players_in_hand[x]] )

                        self.jump = 99
                        print('\tesperando ',POSITION_DICT[self.table.players[self.table.players_in_hand[index]].position])
                        
                        
                        
                        if SELF_PLAYING:
                            check = Check(t, self.table.players[SELF_SEAT], self.table.board, self.table.players[SELF_SEAT].cards)
                            self.table.players[self.table.players_in_hand[index]].WaitAction(t, check)          # wait for action
                        else:
                            check = ''
                            self.table.players[self.table.players_in_hand[index]].WaitAction(t, check)          # wait for action

                        
                        if ZOOM and self.table.players_in_hand[index] == SELF_SEAT and self.table.players[self.table.players_in_hand[index]].action[self.table.breakcounter] == 'fold' and SELF_PLAYING: 
                            self.zoombreak = True
                            break

                        if self.table.players[self.table.players_in_hand[index]].action[self.table.breakcounter] == 'fold' or self.table.players[self.table.players_in_hand[index]].action[self.table.breakcounter] == 'empty' or self.table.players[self.table.players_in_hand[index]].action[self.table.breakcounter] == 'sitout':
                            self.table.in_hand[0].remove(self.table.players_in_hand[index])
                            self.table.in_hand[1].remove(self.table.players_in_hand[index])
                            #print(in_hand,' inhandn after remove')
                            self.table.players[self.table.players_in_hand[index]].is_playing = False
                            self.table.players[self.table.players_in_hand[index]].have_cards = False
                            if SELF_PLAYING and self.table.players_in_hand[index] == SELF_SEAT:
                                self.table.players[self.table.players_in_hand[index]].reset()
                                self.zoombreak = True        # set self.zoombreak as true to end this hand and wait for the nexself.table.(dont waste time/less bug)
                                break

                        if self.table.players[self.table.players_in_hand[index]].action[self.table.breakcounter] == 'call':
                            self.table.limp = True
                            self.table.limp_count += 1
                            #print('allin check when calling')
                            self.table.players[self.table.players_in_hand[index]].AllinCheck(self.table.breakcounter)
                            #print('allin check when calling ',self.table.players[self.table.players_in_hand[index]].is_allin)
                            
                            if self.table.players[self.table.players_in_hand[index]].is_allin == True:
                                self.table.allin_count += 1

                        elif(self.table.players[self.table.players_in_hand[index]].action[self.table.breakcounter] == 'raise' or self.table.players[self.table.players_in_hand[index]].action[self.table.breakcounter] == 'bet' or self.table.players[self.table.players_in_hand[index]].action[self.table.breakcounter] == 'allin'):
                            self.table.bets = True
                            self.table.bet_quantia += 1
                            
                            if self.table.bets_pos < self.table.players[self.table.players_in_hand[index]].position:
                                self.table.bets_pos = self.table.players[self.table.players_in_hand[index]].position
                            
                            self.jump = self.table.players_in_hand[index]       # seta self.jumper pro proximo FOR LOOP
                            self.table.players[self.table.players_in_hand[index]].AllinCheck(self.table.breakcounter)
                            
                            if self.table.players[self.table.players_in_hand[index]].is_allin == True:
                                self.table.allin_count += 1

                            index_temp = self.table.players_in_hand[index]
                            self.table.players_in_hand = arruma_list(self.table.players_in_hand[index], list(self.table.in_hand[self.in_use])) 
                            index = self.table.players_in_hand.index(index_temp)
                            del index_temp
                            break           # break pra comecar o index do comeco. break o for loop e nao o while.
                
                #print(in_hand,' inhand')
                
            if self.zoombreak:
                break
                
            if len(self.table.in_hand[1]) <= 1: # so tem um players na mao
                break
                                                                            # dava bug qndo eu contra + 1 e villan called allin, ficava esperando minha acao.
            if self.table.allin_count >= (len(self.table.in_hand[1])-1) and self.table.allin_count >= 1: # and not self.table.players[SELF_SEAT].is_playing: # pl > 1.
                self.zoombreak = True
                break
                
                
            if self.table.players_in_hand[index] == self.table.players_in_hand[-1]:       # BREAK DEPOIS DO ULTIMO PLAYER. SE ELE NAO RAISE / BET 
                self.table.breakcounter += 1
                self.table.board.UpdateBoard(self.table.breakcounter)
                for x in range(0,len(self.table.players_in_hand)):
                    if self.table.players[self.table.players_in_hand[x]].have_cards:
                        self.table.players[self.table.players_in_hand[x]].reset()

                self.in_use = 1
                self.table.players_in_hand = list(self.table.in_hand[self.in_use])

                break           # break o while True loop.

    def MainLoopReset(self):
        del self.table.in_hand
        del self.table.players_in_hand
        del self.jump
        del self.in_use          
        self.zoombreak = False

    def MainLoop(self):
        while True: # LOOP TOTAL
            self.table.UpdateHandNum()
            if self.table.breakcounter == -1:
                print('Esperando proxima mao')
            self.table.breakcounter = 0        # counter pras streets
            
            if self.table.hand_num not in hand_list: # ESPERA PROXIMO DEALER. PRA NAO COMECAR NO MEIO DA MAO
                self.table.UpdateDealer()
                self.table.board.ResetBoard()
                self.table.hand_num_old = copy.deepcopy(self.table.hand_num)
                self.AddHandList()
                self.table.dealer_old = self.table.dealer
                
                self.WaitDealerDealCards()
                
                self.zoombreak = False
                self.table.in_hand = []
                self.table.players_in_hand = []
                self.table.players = ['', '', '', '', '', '', '', '', '', '']       # RESET METHOD?
                
                self.SetPlayersObjects()
            
                self.table.UpdateHandOrder() # ordena a mao
                self.in_use = 0                              # list in use
                self.position_counter = 0
                
                self.table.players_in_hand = list(self.table.in_hand[self.in_use])
                for x in self.table.in_hand[self.in_use][::-1]:
                    # POSITION_DICT = {0:'BB', 1:'SB', 2:'BU', 3:'CO', 4:'HJ', 5:'MP+1', 6:'MP', 7:'UTG+1', 8:'UTG'}
                    # 0-1 == Blinds     2 - 3 == Late       4 - 6 == mid        7-8 == Early
                    self.table.players[x].position = self.position_counter
                    self.table.players[x].setor = SETOR_DICT[self.position_counter] #useless?
                    self.position_counter += 1

                self.jump = 99                               # self.jump pra qndo arrumar lista

                self.table.ResetData()
                # SETUP COMPLETED


                while len(self.table.in_hand[1]) > 1 and self.table.breakcounter <= 3 and self.table.allin_count <= (len(self.table.in_hand[1])-1):    # self.table.breakcounter [0] = pre-flop / [1] = flop / [2] = turn / [3] = river / [4+] = hands over     
                    self.table.ResetStreet()
                    self.table.UpdateDealer()
                    
                    if self.table.hand_num == self.table.hand_num_old:        # CHECKA PRA VER SE ESTA AINDA NA MESMA MAO
                        self.InHandLoop()
                        if self.zoombreak:
                            break

                    else:   # A MAO ACAOU. DEALER != OLD DEALER.
                        break            # break while len(self.table.players_in_hand) > 1
                        
                
                self.MainLoopReset()
