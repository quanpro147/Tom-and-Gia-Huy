
#from Do_an.SaveLoad import game_manager

def readfile(path):
    with open(path, 'r') as f:
        l = f.readlines()
        return [s.strip() for s in l]
def delete(path, game):
    pass
