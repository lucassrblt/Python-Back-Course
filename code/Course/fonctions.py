def addition(nb1: int, nb2: int = 0) -> int: # On indique le type des arguments attendus et le type de retour, non-cassable, si nb2 n'est pas donné elle prend 0 par défault
  # Ici on créer une mini-doc sur notre fonction displonible au survol lorsqu'elle est appelé
  """
  Fonction qui fait l'addition de deux nombres
  
  Arguments:
  - nb1 est le premier nombre 
  - nb2 est le deuxième nombre 
  """
  return nb1 + nb2

var = addition()