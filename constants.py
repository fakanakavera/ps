from os import getcwd


'''
    PATHs from templates images
'''
DIR = getcwd()
TOPLEFT = 'template/roomlogo/topleft/*.png'
POT = {'PLAYMONEY':'template/pot/playmoney.png', 'REALMONEY':'template/pot/realmoney.png', 'all':'template/pot/*.png'}
DEALER = 'template/dealer/*.png'
HANDNUMBER = 'template/handnumber/0.png'
HANDNUMBER_PAR = 'template/handnumber/'
HOLECARDS = 'template/read_hole/cards/*.png'
CHECKCARDS = 'template/check_cards/*.png'
WAITFASTFOLD = 'template/fastfold/*.png'
ALLIN = 'template/allin/allin.png'
PLTHINKING = 'template/plthinking/0.png'
PLACTION = 'template/plaction/*.png'
DECISIONREAD = ['template/decisionread/fold.png', 'template/decisionread/*.png', 'template/decisionread/raise.png']
WAITOWNACTION = 'template/waitownaction/0.png'
POT_NUMBERS = 'template/pot/numbers/*.png'
RAISE_NUMBERS = 'template/raise/numbers/*.png'
HAND_NUMBERS = 'template/handnumber/numbers/*.png'
WAITING_PL_THINK = 'template/waiting/0.png'

'''
    GAME SETTINGS
'''
AUTOPLAYING = False
SELF_PLAYING = False
ZOOM = False
PLAYING_MONEY = True
LOGGING = False
DECISION_LOG = False
NPLAYERS = 6

TABLE_X_SIZE = 1320 # TABLE SIZE X
TABLE_Y_SIZE = 940  # TABLE SIZE Y

if PLAYING_MONEY:
    POTMONEY = 'PLAYMONEY'
else:
    POTMONEY = 'REALMONEY'

if NPLAYERS == 9:
    SELF_SEAT = 5
elif NPLAYERS == 6:
    SELF_SEAT = 3

'''
    CONSTANTS
'''
GPIO_DICT = {'fold':11, '':11, 'call':12, 'check':12, 'bet':13, '3x':40, '40':16, '45':18, '55':38, '65':38, 'None':11}

CARDS_DIC = {'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'J':10,'Q':11,'K':12,'A':13}
DICT_CARDS = {0:'a', 1:'2', 2:'3', 3:'4', 4:'5', 5:'6', 6:'7', 7:'8', 8:'9', 9:'T', 10:'J', 11:'Q', 12:'K', 13:'A'}
SUIT_DIC = {'c':0, 'd':1, 's':2, 'h':3}
DICT_SUIT = {0:'c', 1:'d', 2:'s', 3:'h'}

STREET = ['pre-flop', 'flop', 'turn', 'river',' HAND IS OVER ']

DICT_STR = {0:'NOTHING', 1:'BACKDOOR', 2:'GUTSHOT',         3:'1 SIDE STR DRAW', 4:'UPDOWN STR DRAW', 5:'STRAIGHT MADE', 6:'NOTHING'}
DICT_FSH = {0:'RAINBOW', 1:'BACKDOOR', 2:'DOUBLE BACKDOOR', 3:'FSH DRAW 2 NEEDED', 4:'FSH DRAW 1 NEEDED', 5:'FLUSH MADE', 6:'NOTHING'}
DICT_PAIR = {0:'NOTHING', 1:'PAIR', 2:'2 PAIRS', 3:'TRIPLE', 4:'FULLHOUSE', 5:'QUAD'}
DICT_FINAL = {0:'NOTHING', 1:'PAIR', 2:'2 PAIRS', 3:'TRIPLE', 4:'STRAIGHT', 5:'FLUSH', 6:'FULLHOUSE', 7:'QUAD', 8:'STRAIGHT FLUSH', 9:'ROYAL FLUSH'}

COD_ACTION = {'fold':0, 'check':1, 'call':2, 'bet':3, 'raise':3, 'allin':30}
            

HOLE_RANK = ['AAo','KKo','QQo','JJo','AKs','AQs','TTo','AKo','AJs','KQs','99o','ATs','AQo','KJs','88o','QJs','KTs','A9s','AJo','QTs','KQo','77o','JTs','A8s','K9s','ATo','A5s','A7s','KJo','66o','T9s','A4s','Q9s','J9s','QJo','A6s','55o','A3s','K8s','KTo','98s','T8s','K7s','A2s','87s','QTo','Q8s','44o','A9o','J8s','76s','JTo','97s','K6s','K5s','K4s','T7s','Q7s','K9o','65s','T9o','86s','A8o','J7s','33o','54s','Q6s','K3s','Q9o','75s','22o','J9o','64s','Q5s','K2s','96s','Q3s','J8o','98o','T8o','97o','A7o','T7o','Q4s','Q8o','J5s','T6o','75o','J4s','74s','K8o','86o','53s','K7o','63s','J6s','85o','T6s','76o','A6o','T2o','95s','84o','62o','T5s','95o','A5o','Q7o','T5o','87o','83o','65o','Q2s','94o','74o','54o','A4o','T4o','82o','64o','42o','J7o','93o','85s','73o','53o','T3o','63o','K6o','J6o','96o','92o','72o','52o','Q4o','K5o','J5o','43s','Q3o','43o','K4o','J4o','T4s','Q6o','Q2o','J3s','J3o','T3s','A3o','Q5o','J2o','84s','82s','42s','93s','73s','K3o','J2s','92s','52s','K2o','T2s','62s','32o','A2o','83s','94s','72s','32s']
HOLE_RANK = np.array(HOLE_RANK)

CARDS_LEFT = [0, 47.000, 46.000]

if NPLAYERS == 9: 
    POSITION_DICT =         {       0:'BB',     1:'SB',     2:'BU',     3:'CO',     4:'HJ',     5:'MP+1',   6:'MP',     7:'UTG+1',  8:'UTG'     }
    SETOR_DICT = { 0:'BLINDS',     1:'BLINDS',     2:'LATE',     3:'LATE',     4:'MID',     5:'MID',   6:'EARLY',     7:'EARLY',  8:'EARLY'     }
if NPLAYERS == 6:
    POSITION_DICT =         {       0:'BB',     1:'SB',     2:'BU',     3:'CO',     4:'MP',     5:'UTG'     }
    SETOR_DICT =            {0:'BLINDS',     1:'BLINDS',     2:'LATE',     3:'MID',     4:'MID',     5:'EARLY'}

'''
    RASP_CONNECTION
'''
    RASP_HOST = '192.168.0.200'
    RASP_PORT = 5560
