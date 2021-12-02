import cv2
import numpy as np
from PIL import ImageGrab, Image
import time
import glob
import os
import random
import copy


time.sleep(1)
print('STARTING...')
t = Table()
print("table set")
start = time.time()
t.fnkfile = 'logs/'+str(int(time.time()))+'.fnk'
t.dealer_old = t.dealer
t.hand_num_old = 0
t.hand_num_old = copy.deepcopy(t.hand_num)
hand_list = []
AddHandList(hand_list, t.hand_num)
t.breakcounter = -1
while True: # LOOP TOTAL
    t.UpdateHandNum()
    #print(hand_list)
    #print('Hand number ',t.hand_num,' - ',t.hand_num_old)
    if t.breakcounter is -1:
        print('Esperando proxima mao')
        # print('Time: ',(time.time()-start))
    t.breakcounter = 0        # counter pras streets
    
    if t.hand_num not in hand_list: # ESPERA PROXIMO DEALER. PRA NAO COMECAR NO MEIO DA MAO
        #print('GOT In')
        #os.system('cls')
        t.UpdateDealer()
        t.board.ResetBoard()
        t.hand_num_old = copy.deepcopy(t.hand_num)
        AddHandList(hand_list, t.hand_num)
        t.dealer_old = t.dealer
        card_count = 0
        
        while card_count < 2:   # ESPERA DEALER DAR CARTAS
            card_count = 0
            t.pl = ['', '', '', '', '', '', '', '', '', '']
            for x in range(1,(NPLAYERS+1)): # loop all players
                t.pl[x] = Player(x)
                t.pl[x].CheckCards()
                if t.pl[x].have_cards:     # break na primeira vez q achar hole cards
                    card_count += 1
        
        zoombreak = False
        in_hand = []
        t.players_in_hand = []
        t.pl = ['', '', '', '', '', '', '', '', '', '']
        
        for x in range(1,(NPLAYERS+1)):   # SETA TODOS PLAYERS
            t.pl[x] = Player(x)
            t.pl[x].CheckCards()     # ALTERA SELF.CARDS

            if t.pl[x].have_cards:              # SE tiver cards.
                in_hand.append(x)
                t.pl[x].is_allin = False
     
        #print(t.dealer)
        #print(in_hand)
        #print('-'*20)
        in_hand = hand_order(t.dealer, in_hand) # ordena a mao
        in_use = 0                              # list in use
        position_counter = 0
        
        t.players_in_hand = list(in_hand[in_use])
        for x in in_hand[in_use][::-1]:
            # POSITION_DICT = {0:'BB', 1:'SB', 2:'BU', 3:'CO', 4:'HJ', 5:'MP+1', 6:'MP', 7:'UTG+1', 8:'UTG'}
            # 0-1 == Blinds     2 - 3 == Late       4 - 6 == mid        7-8 == Early
            t.pl[x].position = position_counter
            t.pl[x].setor = SETOR_DICT[position_counter]
            position_counter += 1

        jump = 99                               # jump pra qndo arrumar lista

        t.ResetData()
        

        #print('SETUP COMPLET')
        while len(in_hand[1]) > 1 and t.breakcounter <= 3 and t.allin_count <= (len(in_hand[1])-1):    # t.breakcounter [0] = pre-flop / [1] = flop / [2] = turn / [3] = river / [4+] = hands over     
            t.ResetStreet()
            t.UpdateDealer()      # update dealer
            
            if t.hand_num == t.hand_num_old:        # CHECKA PRA VER SE ESTA AINDA NA MESMA MAO
                while True:             # so sai desse loop com break
                    for index in range(0,len(t.players_in_hand)):          # loop de cada street   
                        if t.players_in_hand[index] != jump and len(in_hand[1]) > 1 and t.pl[t.players_in_hand[index]].is_playing == True and t.pl[t.players_in_hand[index]].is_allin == False:    
                            t.ResetStreet()
                            t.UpdatePot()
                            os.system('cls')
                            print('Hand number ',t.hand_num,' - ',t.hand_num_old)
                            print('$'*20,' ',STREET[t.breakcounter],' ','$'*20)
                            print(t)
                            print('Pot: ',t.pot)
                            print('limps ',t.limp,' - ',t.limp_count)
                            print('bets ',t.bets,' - ',t.bets_pos)
                            #print('\n\n',t.players_in_hand,'\n\n')
                            
                            
                            

                            if SELF_PLAYING and t.pl[SELF_SEAT].is_playing: # if im playing
                                t.pl[SELF_SEAT].cards.HolePercent()
                                print('Hole Cards: ',t.pl[SELF_SEAT].cards.hole_full[0],' - ',t.pl[SELF_SEAT].cards.hole_full[1],'  ',t.pl[SELF_SEAT].cards.hole_percent,'\n')
                                
                                if t.breakcounter > 0 and t.breakcounter < 3 and t.pl[SELF_SEAT].is_playing: #nao calcula odds no pre flop
                                        giving_hand = [t.pl[SELF_SEAT].cards.hole_full[0], t.pl[SELF_SEAT].cards.hole_full[1]]
                                        for x in range(1,t.breakcounter+3):
                                            giving_hand.append(t.board.board[x])
                                            
                                        t.pl[SELF_SEAT].cards.hand_rank, t.pl[SELF_SEAT].cards.outs_hand, t.pl[SELF_SEAT].cards.flush_naipe, t.pl[SELF_SEAT].cards.str_min_card, t.pl[SELF_SEAT].cards.pair_card = hand_outs(giving_hand)
                                        t.pl[SELF_SEAT].cards.UpdateOutsPercent(t.breakcounter)
                                        print('HAND RANK ',DICT_FINAL[t.pl[SELF_SEAT].cards.hand_rank])
                                        print('OUTS ',t.pl[SELF_SEAT].cards.outs_hand,' = ',t.pl[SELF_SEAT].cards.outs_por,'%')
                                    
                            if t.breakcounter > 0:# and t.players_in_hand[index] == SELF_SEAT:
                                t.board.UpdateBoardStats(t)
                                print('BOARD RANK STR', DICT_STR[t.board.str_check[t.breakcounter]],' ',t.board.str_check[t.breakcounter])
                                print('BOARD RANK FSH', DICT_FSH[t.board.suit_check[t.breakcounter]],' ',t.board.suit_check[t.breakcounter])
                                print('BOARD RANK PAIR', DICT_PAIR[t.board.pair_check[t.breakcounter]],' ',t.board.pair_check[t.breakcounter])
                            
                            #print 'ALLIN COUNTER: ',t.allin_count
                            
                            if ZOOM and t.pl[SELF_SEAT].cards.hole_percent < MIN_RANGE and Action() and t.pl[SELF_SEAT].position > 0 and AUTOPLAYING:
                                if Action():
                                    while Action():
                                        SendFastFold()
                                        print('FastFoldSending.....')
                                        time.sleep(0.5)
 
                                    
                                zoombreak = True
                                break 
                                
                            else:    
                                print('\nPlayer\tAction\tPosition')
                                for x in range(0,len(t.players_in_hand)):
                                    #if t.pl[t.players_in_hand[x]].have_cards:
                                    if index == x:
                                        print('--> ',t.pl[t.players_in_hand[x]])
                                    else:
                                        print(t.pl[t.players_in_hand[x]] )

                                jump = 99
                                print('\tesperando ',POSITION_DICT[t.pl[t.players_in_hand[index]].position])
                                
                                
                                
                                if SELF_PLAYING:
                                    check = Check(t, t.pl[SELF_SEAT], t.board, t.pl[SELF_SEAT].cards)
                                    t.pl[t.players_in_hand[index]].WaitAction(t, check)          # wait for action
                                else:
                                    check = ''
                                    t.pl[t.players_in_hand[index]].WaitAction(t, check)          # wait for action

                                #print('in hand len ',len(in_hand[1]))
                                #print('allin ',t.allin_count)
                             
                                
                                
                                
                                if ZOOM and t.players_in_hand[index] == SELF_SEAT and t.pl[t.players_in_hand[index]].action[t.breakcounter] == 'fold' and SELF_PLAYING: 
                                    zoombreak = True
                                    break

                                if t.pl[t.players_in_hand[index]].action[t.breakcounter] == 'fold' or t.pl[t.players_in_hand[index]].action[t.breakcounter] == 'empty' or t.pl[t.players_in_hand[index]].action[t.breakcounter] == 'sitout':
                                    in_hand[0].remove(t.players_in_hand[index])
                                    in_hand[1].remove(t.players_in_hand[index])
                                    #print(in_hand,' inhandn after remove')
                                    t.pl[t.players_in_hand[index]].is_playing = False
                                    t.pl[t.players_in_hand[index]].have_cards = False
                                    if SELF_PLAYING and t.players_in_hand[index] == SELF_SEAT:
                                        t.pl[t.players_in_hand[index]].reset()
                                        zoombreak = True        # set zoombreak as true to end this hand and wait for the next.(dont waste time/less bug)
                                        break

                                if t.pl[t.players_in_hand[index]].action[t.breakcounter] == 'call':
                                    t.limp = True
                                    t.limp_count += 1
                                    #print('allin check when calling')
                                    t.pl[t.players_in_hand[index]].AllinCheck(t.breakcounter)
                                    #print('allin check when calling ',t.pl[t.players_in_hand[index]].is_allin)
                                    
                                    if t.pl[t.players_in_hand[index]].is_allin == True:
                                        t.allin_count += 1

                                elif(t.pl[t.players_in_hand[index]].action[t.breakcounter] == 'raise' or t.pl[t.players_in_hand[index]].action[t.breakcounter] == 'bet' or t.pl[t.players_in_hand[index]].action[t.breakcounter] == 'allin'):
                                    t.bets = True
                                    t.bet_quantia += 1
                                    
                                    if t.bets_pos < t.pl[t.players_in_hand[index]].position:
                                        t.bets_pos = t.pl[t.players_in_hand[index]].position
                                    
                                    jump = t.players_in_hand[index]       # seta jumper pro proximo FOR LOOP
                                    t.pl[t.players_in_hand[index]].AllinCheck(t.breakcounter)
                                    
                                    if t.pl[t.players_in_hand[index]].is_allin == True:
                                        t.allin_count += 1

                                    index_temp = t.players_in_hand[index]
                                    t.players_in_hand = arruma_list(t.players_in_hand[index], list(in_hand[in_use])) 
                                    index = t.players_in_hand.index(index_temp)
                                    del index_temp
                                    break           # break pra comecar o index do comeco. break o for loop e nao o while.
                        
                        #print(in_hand,' inhand')
                        
                    if zoombreak:
                        break
                        
                    if len(in_hand[1]) <= 1: # so tem um players na mao
                        break
                                                                                    # dava bug qndo eu contra + 1 e villan called allin, ficava esperando minha acao.
                    if t.allin_count >= (len(in_hand[1])-1) and t.allin_count >= 1: # and not t.pl[SELF_SEAT].is_playing: # pl > 1.
                        zoombreak = True
                        break
                        
                        
                    if t.players_in_hand[index] == t.players_in_hand[-1]:       # BREAK DEPOIS DO ULTIMO PLAYER. SE ELE NAO RAISE / BET 
                        t.breakcounter += 1
                        t.board.UpdateBoard(t.breakcounter)
                        for x in range(0,len(t.players_in_hand)):
                            if t.pl[t.players_in_hand[x]].have_cards:
                                t.pl[t.players_in_hand[x]].reset()

                        in_use = 1
                        t.players_in_hand = list(in_hand[in_use])

                        break           # break o while True loop.
                
                if zoombreak:
                    break
            
            else:   # A MAO ACAOU. DEALER != OLD DEALER.
                break            # break while len(t.players_in_hand) > 1
                

        del in_hand
        del t.players_in_hand
        del jump
        del in_use          
        zoombreak = False