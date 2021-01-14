#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


class Cards:
    
    def __init__(self):
        self.all_cards = []
        self.suits = ('Heart ','Diamond ','Spades ','Clubs ')
        self.ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
        self.points = 0
        
    def deck(self):
        for i in self.suits:
            for j in self.ranks:
                x = i + j
                self.all_cards.append(x)
        import random
        random.shuffle(self.all_cards)
        return self.all_cards
    
    
        
        


# In[3]:


def card_points(all_cards=[]):
        points = 0
        for z in all_cards:
            if 'Two' in z:
                points += 2
            if 'Three' in z:
                points += 3
            if 'Four' in z:
                points += 4
            if 'Five' in z:
                points += 5
            if 'Six' in z:
                points += 6
            if 'Seven' in z:
                points += 7
            if 'Eight' in z:
                points += 8
            if 'Nine' in z:
                points += 9
            if 'Ten' in z:
                points += 10
            if 'Jack' in z:
                points += 10
            if 'Queen' in z:
                points += 10
            if 'King' in z:
                points += 10
            if 'Ace' in z:
                points += 11
                
        return points


# In[4]:


def players_number():
    x = True
    while x == True:
        no_of_players = input('Please enter the number of players: ')
        if no_of_players.isdigit():
            no_of_players = int(no_of_players)
            print('\nEnjoy the Game\n')
            return no_of_players
            x = False
            break

        else:
            print('Enter a valid value')
            x = True
        
    


# In[5]:


def card_serve(dealer_deck=[]):
    players_cards = []
    no_of_players = players_number()
    for a in range(0,no_of_players+1):
        c = []
        players_cards.append(c)
        
    e = 0
    while e < 2:
        for d in range(0,no_of_players+1):
            temp = dealer_deck.pop()
            players_cards[d].append(temp)
        e += 1
        
    return players_cards
        


# In[6]:


def players_points():
    points = []
    global players_cards
    no_of_players = len(players_cards)
    
    for player in range(0,no_of_players):
        temp = card_points(players_cards[player])
        points.append(temp)
    
    return points
            
        


# In[7]:


def game_play():
    global dealer_deck
    global players_cards
    global points
    
    a = 0
    c = True
    b = len(players_cards)
    
    
    for x in points:
        if a < b-1:
            if x < 21:
                player_choice = input('\nWould you like to Hit or Stand Player {}\n\nPress "h" for Hit or Press "s" for Stay   '.format(a+1))
                player_choice.lower()
                y = True
                while y == True:
                    if player_choice == 'h' or player_choice == 's':                        
                        y = False
                        break
                    else:
                        print('Please enter "h" or "s"')
                        break

                if player_choice == 'h':
                    temp = dealer_deck.pop()
                    players_cards[a].append(temp)
                    points = players_points()

                elif player_choice == 's':
                    pass

            elif x == 21:
                print('\nPlayer {} got Black Jack and congradulations\n'.format(a+1))
                break

            elif x > 21:
                print('\nPlayer {} got Busted\n'.format(a+1))

            a = a+1
        else:
            break
                
        


# In[51]:


def game_status():
    global points
    global players_cards
    
    temp = 0
    a = 0
    b = len(points)

    for x in points:
        a += 1
        if x <= 21:        
            if x > temp:
                temp = x
                position = a

        elif x > 21:
            print('\nPlayer-{} has busted\n'.format(a))

    if position == b:
        print('\nDealer has won the game\n')
    else:
        print('\nPlayer-{} has won the game with {} points\n'.format(position,temp))
        if temp == 21:
            print('\nIt is a BlackJack!')
    
    
        
            


# In[54]:


cont = True
while cont == True:
    dealer = Cards()
    dealer_deck = dealer.deck()

    players_cards = card_serve(dealer_deck)
    print(players_cards)
    points = players_points()
    print(points)
    game_play()
    print(points)
    print(players_cards)
    game_status()

    game_again = input('Would you like to play another game? "y"/"n" ')
    if game_again == "y":
        cont = True
    else:
        break
    


# In[ ]:





# In[ ]:





# In[ ]:




