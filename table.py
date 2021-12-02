class Table(): # NEW
    def __init__(self):
        self.bb = 100
        self.pot_pos = pot_pos()
        self.dealer_pos = dealer_pos()
        self.handnumber_pos = (28, 34, 225, 14) # NO NEDDED
        self.dealer = 0
        print('start')
        self.UpdatePot()    # MOD
        print('UpdatePot: '+str(self.pot))
        self.UpdateDealer() # OK
        print('UpdateDealer: '+str(self.dealer))
        self.UpdateHandNum()
        print('UpdateHandNum: '+str(self.hand_num))
        
        self.to_call = 1
        self.pot_odds_str = ''
        self.pot_odds_per = 0
        self.allin_count = 0
        
        self.board = Board()
        self.logging = True
        
        
        # POSITION SETUP
        self.to_call_pos = to_call_pos()
        self.to_allin_call_pos = to_allin_call_pos()

    def __str__(self):
        return "Board\nFlop: %s %s %s\nTurn: %s\nRiver: %s\n" % (self.board.board[1], self.board.board[2], self.board.board[3], self.board.board[4], self.board.board[5])
    
    def GetFrame(self):
        img = np.array(ImageGrab.grab(bbox=TABLECOOR))
        #show(img)
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #ajusta RGB
        
    def UpdatePot(self):
        self.pot = False
        while self.pot == False:
            if PLAYING_MONEY:
                template = cv2.imread(DIR+POT['REALMONEY'])
            else:
                template = cv2.imread(DIR+POT['PLAYMONEY'])

            self.pot = int(ReadPot(template_input=template, frame_input=self.GetFrame()))
        
    def UpdateDealer(self): 
        # UPDATE self.dealer
        # USING funcs.check_coor()
        r = False
        while(r == False):            
            xx = FindTemplate(template_input=DIR+DEALER, tp=TABLECOOR, wanted='center', threshold=0.9)     
            for t_pos in range(1, (NPLAYERS+1)):
                try:
                    if check_coor(xx, self.dealer_pos[t_pos]):
                        r = t_pos
                        break
                except:
                    pass

        self.dealer = r
    
    def UpdateHandNum(self):
        result = False
        while result == False:
            result = ReadHandNumber(template_input=DIR+HANDNUMBER, frame_input=TABLECOOR)
        
        self.hand_num = result
        #print('Hand num = ',self.hand_num)

    def GetHandNum(self):
        result = False
        while result == False:
            result = ReadHandNumber(template_input=DIR+HANDNUMBER, frame_input=TABLECOOR)
        
        return result

    def WaitForCards(self):
        while self.card_count < 2:
            self.card_count = 0
            self.pl = ['', '', '', '', '', '', '', '', '', '']
            for x in range(1, (NPLAYERS+1)): # loop all players
                self.pl[x] = Player(x)

    def ResetAllinCount(self):
        self.allin_count = 0

    def ResetData(self):
        self.allin_count = 0
        self.limp = False
        self.limp_count = 0
        self.bets = False
        self.bet_quantia = 0
        self.bets_pos = -1

    def ResetStreet(self):
        self.to_call = 1
        self.pot_odds_str = ''
        self.pot_odds_per = 0
          
    def WaitFastFold(self):
        temp_list = glob.glob(DIR+WAITFASTFOLD) #dir pra templates
        #check pra ver ql tipo de input.
        
        tempcount = 0 # count pra rodar tds templates.
        result = False

        while(result == False):
            if(tempcount > (len(temp_list)-1)):
                tempcount = 0
                
            template = cv2.imread(temp_list[tempcount])
            h, w = template.shape[:-1]
            res = cv2.matchTemplate(GetFrame(), template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where(res >= threshold)#check loc[1][0]

            for pt in zip(*loc[::-1]):  # pt contem coordenadas  **** (pt[0] + (w/2), pt[1] + (h/2)) = CENTRO ****
                result = True
                break

            tempcount += 1
        return result
          
    def UpdateToCall(self): # (1096, 886, 201, 42) to allin call
        self.to_call = DecisionRead(1) # to_call == 'check' if check
        if self.to_call != 'check':
            self.to_call = int(self.to_call)
        
        if PLAYING_MONEY and self.to_call != 'check':
            self.to_call = self.to_call * 100
            
        self.UpdatePot()
        if self.to_call != 'check':
            self.UpdatePotOdds()

    def UpdatePotOdds(self):
        self.pot_odds_str = '1:',(float(self.pot)/float(self.to_call))
        self.pot_odds_per = ((self.to_call/(self.pot+self.to_call))*100)