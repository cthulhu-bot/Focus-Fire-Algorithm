import random

def main():
  hitpoints = 10
  team_1 = [[1,hitpoints],[2,hitpoints],[3,hitpoints],[4,hitpoints]]
  team_2 = [[1,hitpoints],[2,hitpoints],[3,hitpoints],[4,hitpoints]]
  players = {'#Team_1':team_1}
  players['#Team_2'] = team_2
  i = 1
  while ((len(players['#Team_1']) != 0) and (len(players['#Team_2']) != 0)):
    print ' *** Iteration ',i,' ***'
    print

    # Team 1
    print 'Team 1'

    # Iterate through remaining members of Team 1 and fire at first available target on Team 2
    #Acquire Target
    for player in players['#Team_1']:
      # Update with checking whether list still contains a zero index
      target = players['#Team_2'][0]
      print '  Target Acquired:  Target = Player',target[0]
      print
      print '   Team 1 - Player',player[0]
      print '     Shooting at Player',target[0]
      shot = random.randint(0,1)
      print '     Shot = ',shot
      if shot == 1:
        if target in players['#Team_2']:
          print '     Player ',player[0],' HITS Player ',target[0]
          if target[1] > 0:
            target[1] = target[1] - 1
            print '     Player ',target[0],' has ',target[1],' hit points remaining'
            if target[1] == 0:
              print '     Player ',target[0],' has been pwned!'
              players['#Team_2'].remove(target)
          else:
            players['#Team_2'].remove(target)

    print

    # Team 2
    print 'Team 2'
#    print 'Team 2 has ',len(players['#Team_2'],' remaining'

    # Iterate through remaining members of Team 2
    # Acqiure targets independantly
    for player in players['#Team_2']:
      #Acquire Target
      target = players['#Team_1'][random.randint(0,len(players['#Team_1']) - 1)]
      print '   Team 2 - Player',player[0]
      print '     Target Acquired:  Target = Player',target[0]
      print '     Shooting at Player',target[0]
      shot = random.randint(0,1)
      print '     Shot = ',shot
      if shot == 1:
        if target in players['#Team_1']:
          print '     Player ',player[0],' HITS Player ',target[0]
          if target[1] > 0:
            target[1] = target[1] - 1
            print '     Player ',target[0],' has ',target[1],' hit points remaining'
            if target[1] == 0:
              print '     Player ',target[0],' has been pwned!'
              players['#Team_1'].remove(target)
          else:
            players['#Team_1'].remove(target)

    print

    # Display remaining players
    print 'Players remaining on Team 1:  ',len(players['#Team_1'])
    print 'Players remaining on Team 2:  ',len(players['#Team_2'])
    if len(players['#Team_1']) == 0:
      print ' *** Team 2 Wins!!! ***'
    elif len(players['#Team_2']) == 0:
      print ' *** Team 1 Wins!!! ***'
    else:
      x = raw_input('Hit enter for next iteration >>')
    print

def player():
  accuracy = 0.0


main()
