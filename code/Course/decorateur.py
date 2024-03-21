# @quelquechose
# def mafonction():
#   pass

def repeter_trois_fois(func):
  def w_rtf():
    print("je vais répéter trois fois")
    func()
    func()
    func()
  return w_rtf

def repeter_n_fois(nb):
  def decorateur(func):
    def w_rtf():
      print("je vais répéter trois fois")
      for _ in nb:
        func()
    return w_rtf
  return decorateur

# @repeter_trois_fois
@repeter_n_fois(5)
def dire_bonjour():
  print("bonjour")
# repeter_5_fois = repeter_n_fois(5) 
# dire_bonjour = repeter_5_fois(dire_bonjour)
# dire_bonjour = repeter_trois_fois(dire_bonjour)

@repeter_trois_fois
def dire_bonsoir():
  print("bonsoir")
# dire_bonsoir = repeter_trois_fois(dire_bonsoir)


dire_bonjour() # 3 appels