class Player(): # NEW
    def __init__(self, p):
        self.p = p
        self.position = False                                   # position of the player in the hand. 0=bb, 9=utg
        self.setor = ''                                         # position of the player in the hand. early, mid, late, blinds
        self.last_action = 0                                    # timer since last action
        self.action = ['None','None','None','None']             # timer since last action
        self.points = ['None','None','None','None']             # timer since last action
        self.points_total = 1                                   # calc point of actions
        self.decisao_calculada = ''
        
        
        self.is_allin = False                                   #se all in pula a tomada de decisao.
        self.have_cards = False                                 #se all in pula a tomada de decisao.
        self.is_playing = False                                 #se all in pula a tomada de decisao.
        
        
        self.cards_pos = cards_pos(p)                   # POSITIONS
        self.action_pos = action_pos(p)                 # POSITIONS
        self.hud_pos = hud_pos(p)                       # POSITIONS
        self.allin_pos = allin_pos(p)                   # POSITIONS
        
    
        if self.p == SELF_SEAT and SELF_PLAYING == True:     # SELF ESPECIAL VARS
            self.cards = Hole()
            self.can_fold = False
            self.can_check = False
            self.can_call = False
            self.can_raise = False
            self.raise_size_pos = raise_size_pos()

    def __str__(self):
        return "%s\t%s\t\t%s\t%s" % (self.p, self.action, self.points, POSITION_DICT[self.position])        
            
    def UpdateHole(self):
        if self.p == SELF_SEAT and SELF_PLAYING == True:
            self.cards.hole_full = [False, False]
            temp = False
            
            while temp == False or temp == 'nada':
                frame = GetFrame(coor=TABLECOOR)
                temp = read_hole(crop_img(frame, self.cards.pos[0]))
            
            self.is_playing = True
            self.have_cards = True
            self.cards.hole_full[0] = temp
            self.cards.hole_full[1] = read_hole(crop_img(frame, self.cards.pos[1]))
            
    def CheckCards(self):
        result = FindTemplate(template_input=DIR+CHECKCARDS, frame=crop_img(GetFrame(coor=TABLECOOR), self.cards_pos), wanted='filename_or_nada')

        if SELF_PLAYING:
            if self.p != SELF_SEAT:
                if result != 'nada':
                    self.have_cards = True
                    self.is_playing = True
                else:
                    self.have_cards = False
                    self.is_playing = False
                
            elif self.cards.hole_full[0] == '':
                self.UpdateHole()
                self.cards.hole_card, self.cards.hole_suit = break_hole(self.cards.hole_full)
                self.have_cards = True
                self.is_playing = True
        
        else: # if NOT SELF_PLAYING:
            if result != 'nada':
                self.have_cards = True
                self.is_playing = True
            else:
                self.have_cards = False
                self.is_playing = False
                
    def reset(self):
        #self.allin_count = 0
        self.limp = False
        self.limp_count = 0
        self.bet = False
        self.bet_ammount = 0
        self.bet_position = -1
    
    def AllinCheck(self, breakcounter):
        if FindTemplate(frame=crop_img(GetFrame(coor=TABLECOOR), self.allin_pos), template_input=DIR+'template/allin/*.png', wanted='filename_or_nada') == 'allin':
            self.is_allin = True
            self.action[breakcounter] = 'allin'        
    
    def UpdatePossibleActions(self):
        if DecisionRead(0) == 'fold':
            self.can_fold = True
            self.can_check = False
            self.can_call = True
            
        if DecisionRead(1) == 'check':
            self.can_check = True
            self.can_call = False

        
        self.can_raise = True
        print('\n\n\nFold: ',self.can_fold,'\nCheck: ',self.can_check,'\nCall: ',self.can_call)
        
    def WaitAction(self, t, check):
        ti = time.time() 
        
        if self.p != SELF_SEAT or not SELF_PLAYING:         # if its not SELF
            if pl_thinking() == self.p:
                wait_pl_think(self.p)


            frame = self.GetActionFrame()

            self.action[t.breakcounter] = pl_action(frame)
            if self.action[t.breakcounter] == 'nada':
                self.AllinCheck(t.breakcounter)
                if not self.is_allin:
                    self.CheckCards()
                    if self.have_cards:
                        if self.action[t.breakcounter] == 'nada':
                            self.action[t.breakcounter] = 'check'
                    else:
                        self.action[t.breakcounter] = 'fold'


            # COD_ACTION = {'fold':0, 'check':1, 'call':2, 'bet':3, 'raise':3, 'allin':30}
                        
            # self.points[t.breakcounter] = COD_ACTION[self.action[t.breakcounter]]
            # self.points_total = self.points_total * COD_ACTION[self.action[t.breakcounter]]

            #print '\n1st action check fora de loop ',self.action[t.breakcounter],'\n\n'
                
        else:       #if its SELF wait for shortcuts.
            while not FindTemplate(template_input=DIR+WAITOWNACTION, wanted='bool', threshold=0.95, tp=TABLECOOR):
                pass
                
            self.UpdatePossibleActions()
            if self.can_fold:
                t.UpdateToCall()
   
 
 
     

            #self.decisao_calculada = escolha_decisao(a, t, players_in_hand, index, t.breakcounter, in_hand)
            self.decisao_calculada = DecisionMaking(t, check)

            
            
            
            #frame = self.WaitOwnAction()
            while FindTemplate(template_input=DIR+WAITOWNACTION, wanted='bool', threshold=0.95, tp=TABLECOOR):
                frame = GetFrame(coor=TABLECOOR)[self.raise_size_pos[1]:(self.raise_size_pos[1] + self.raise_size_pos[3]), self.raise_size_pos[0]:(self.raise_size_pos[0] + self.raise_size_pos[2])]
                


            if self.decisao_calculada != 'fold' and self.decisao_calculada != 'check' and self.decisao_calculada != 'call':
                bet = ReadRaise(template_input='C:/Users/RoKeR/Dropbox/poker/2019/template/raise/numbers/*.png', frame_input=frame)
                try:
                    self.raise_amount = int(bet)
                except:
                    cv2.imwrite('C:/Users/RoKeR/Dropbox/poker/2019/logs/hands/ERROR-BET-'+str(int(time.time()))+'.png', frame)
                    self.raise_amount = 1
                    
                self.action[t.breakcounter] = 'raise'
                self.AllinCheck(t.breakcounter)

                
            # elif self.decisao_calculada == 'fold'and not self.can_fold:
            #         self.action[t.breakcounter] = 'check'
                    
            # elif self.decisao_calculada == 'call'and not self.can_call:
            #         self.action[t.breakcounter] = 'check'
                    
            # elif self.decisao_calculada == 'check'and self.can_call:
            #         self.action[t.breakcounter] = 'call'
            elif self.decisao_calculada == 'fold':
                if self.can_fold:
                    self.action[t.breakcounter] = 'fold'
                else:
                    self.action[t.breakcounter] = 'check'
                    
            elif self.decisao_calculada == 'call':
                if self.can_call:
                    self.action[t.breakcounter] = 'call'
                else:
                    self.action[t.breakcounter] = 'check'
                    
            elif self.decisao_calculada == 'check':
                if self.can_call:
                    self.action[t.breakcounter] = 'call'
                else:
                    self.action[t.breakcounter] = 'check'

            
        COD_ACTION = {'fold':0, 'check':1, 'call':2, 'bet':3, 'raise':3, 'allin':30}
        self.points[t.breakcounter] = COD_ACTION[self.action[t.breakcounter]]
        self.points_total = self.points_total * COD_ACTION[self.action[t.breakcounter]]
                    
    def GetActionFrame(self):
        frame = np.array(ImageGrab.grab(bbox=((TP[0]+self.action_pos[0]), (TP[1]+self.action_pos[1]), (TP[0]+self.action_pos[0]+self.action_pos[2]), (TP[1]+self.action_pos[1]+self.action_pos[3]))))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
    
    def WaitOwnAction(self):
        template = cv2.imread(DIR+WAITOWNACTION) #dir pra templates
        result = True

        while(result == True):   
            img = GetFrame()
            h, w = template.shape[:-1]
            res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where(res >= threshold)#check loc[1][0]

            for pt in zip(*loc[::-1]):  # pt contem coordenadas  **** (pt[0] + (w/2), pt[1] + (h/2)) = CENTRO ****
                frame = img[self.raise_size_pos[1]:(self.raise_size_pos[1] + self.raise_size_pos[3]), self.raise_size_pos[0]:(self.raise_size_pos[0] + self.raise_size_pos[2])]
                result = False
                break
            else:
                result = True

        return frame