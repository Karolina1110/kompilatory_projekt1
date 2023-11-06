
from lib2to3.pgen2.token import NEWLINE


class myParser:

  ##### Parser header #####
  def __init__(self, scanner):
    self.next_token = scanner.next_token
    self.token = self.next_token()

  def take_token(self, token_type):
    if self.token.type != token_type:
      self.error("Unexpected token: %s" % token_type)
    if token_type != 'end':
      self.token = self.next_token()

  def error(self,msg):
    raise RuntimeError('Parser error, %s' % msg)

  ##### Parser body #####

  # Starting symbol
  def start(self):
    # start -> BEGIN NEWLINE program END
    if self.token.type == 'begin':
      self.take_token('begin')
      if self.token.type == 'NEWLINE':
        self.take_token('NEWLINE')
      else:
        self.error("NEWLINE needed after definitions")
      self.program()
      self.take_token('end')
    else:
      self.error("Epsilon not allowed")

  def program(self):
    # program -> deff NEWLINE con 
    if self.token.type == 'ID':
      self.deff()
      self.take_token('NEWLINE')
      self.con()
    # program -> eps
    else:
      pass

  def deff(self):
    # deff -> wyr deff
    if self.token.type == 'ID':
      self.wyr()
      self.deff()
    # deff -> eps  
    else:
      pass

  def con(self):
    # con -> skl con
    if self.token.type == 'ID' or self.token.type == 'gnd':
      self.skl()
      self.con()
    else:
      pass
   
  def wyr(self):
    # wyr -> ID ASSIGN func NEWLINE
    if self.token.type == 'ID':
      self.take_token('ID')
      if self.token.type == 'ASSIGN':
        self.take_token('ASSIGN')
      else:
        self.error("ASSIGN needed or NEWLINE if definitions ended")      
      self.func()
      self.take_token('NEWLINE')
      print ("wyr_stmt OK")
    else:
      self.error("Epsilon not allowed")
  
  def func(self):
    # func -> nazwafunc OBRAC args CBRAC
    if self.token.type == 'voltagesource':
      self.take_token('voltagesource')
      if self.token.type == 'OBRAC':
        self.take_token('OBRAC')
      else:
        self.error("Brackets needed")
      self.args()
      self.take_token('CBRAC')
    elif self.token.type == 'resistor':
      self.take_token('resistor')
      if self.token.type == 'OBRAC':
        self.take_token('OBRAC')
      else:
        self.error("Brackets needed")
      self.args()
      self.take_token('CBRAC')
    elif self.token.type == 'capacitor':
      self.take_token('capacitor')
      if self.token.type == 'OBRAC':
        self.take_token('OBRAC')
      else:
        self.error("Brackets needed")
      self.args()
      self.take_token('CBRAC')
    elif self.token.type == 'inductor':
      self.take_token('inductor')
      if self.token.type == 'OBRAC':
        self.take_token('OBRAC')
      else:
        self.error("Brackets needed")
      self.args()
      self.take_token('CBRAC')
    elif self.token.type == 'diode':
      self.take_token('diode')
      if self.token.type == 'OBRAC':
        self.take_token('OBRAC')
      else:
        self.error("Brackets needed")
      self.args()
      self.take_token('CBRAC')
    elif self.token.type == 'voltageprobe':
      self.take_token('voltageprobe')
      if self.token.type == 'OBRAC':
        self.take_token('OBRAC')
      else:
        self.error("Brackets needed")
      self.args()
      self.take_token('CBRAC')
    elif self.token.type == 'currentprobe':
      self.take_token('currentprobe')
      if self.token.type == 'OBRAC':
        self.take_token('OBRAC')
      else:
        self.error("Brackets needed")
      self.args()
      self.take_token('CBRAC')
    else:
      self.error("Epsilon not allowed")

  def args(self):
    # args -> arg otherargs
    if self.token.type == 'ID' or self.token.type == 'NUMBER':
      self.arg()
      self.otherargs()
    else:
      pass

  def arg(self):
    # arg -> ID ASSIGN NUMBER
    if self.token.type == 'ID':
      self.take_token('ID')
      self.take_token('ASSIGN')
      self.take_token('NUMBER')
    # arg -> NUMBER
    elif self.token.type == 'NUMBER':
      self.take_token('NUMBER')
    else:
      self.error("Epsilon not allowed")

  def otherargs(self):
    # otherargs -> COM args
    if self.token.type == 'COM':
      self.take_token('COM')
      self.args()
    else:
      pass


  def skl(self):
    # skl -> czyn resztaczyn NEWLINE
    if self.token.type == 'ID' or self.token.type == 'gnd':
      self.czyn()
      self.resztaczyn()
      self.take_token('NEWLINE')
      print ("skl_stmt OK")
    else:
      self.error("Epsilon not allowed")

  def czyn(self):
    # czyn -> ID OSBRAC NUMBER CSBRAC
    if self.token.type == 'ID':
      self.take_token('ID')
      self.take_token('OSBRAC')
      if self.token.type == 'NUMBER':
        self.take_token('NUMBER')
      else:
        self.error("NUMBER needed")
      self.take_token('CSBRAC')
    # czyn -> gnd
    elif self.token.type == 'gnd':
      self.take_token('gnd')
    else:
      self.error("Epsilon not allowed")

  def resztaczyn(self):
    # resztaczyn -> DDASH czyn resztaczyn
    if self.token.type == 'DDASH':
      self.take_token('DDASH')
      self.czyn()
      self.resztaczyn()
    else:
      pass





       
