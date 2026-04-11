import random

class rpg_game:
    
    def __init__(self,name):
        self.name=name
        self.defending=True
        self.health=100
        if self.name=="Player":
            self.opponent="Enemy"
        else:
            self.opponent="Player"
        
    def attack(self,opponent):
        damage=random.randint(10,30)
        self.defending=False
        #  Player deals random damage between 10 and 30.
        opponent.health-=damage
        print(self.name,"attacks and ",opponent.name,"loses",damage,"points!!!\n")
        print("***Current score***")
        print("Player : ",self.health)
        print("Enemy : ",opponent.health)
        

    def defend(self,damage):
        if self.defending==True:
            self.health-=damage/2
            print(self.name,"choose defending!!!")
        #  Reduces enemy’s next attack damage by half.(optional)

    def heal(self):
        print(self.name ,"choose healing!!!")
        if self.health<=100:
            print(self.name,"healed from",self.health,"to",end=" ")
            self.health+=random.randint(10,25)
            if self.health > 100:
                self.health = 100
        print(self.health)
        # Restores random health between 10 and 25 (but cannot exceed 100).(optional)

    def damage_done(self,damage,opponent):
        if self.defending==False:
            self.health-=damage
        
        print(" Enemy attacks and causes  damage of",damage,"on Player!\n")
        print("***Current score***")
        print("Player : ",self.health)
        print("Enemy : ",opponent.health)

    def current_score(self,opponent):
        
        print("\n***Current score***")
        print("Player : ",self.health)
        print("Enemy : ",opponent.health)
        exit()


damage = random.randint(10, 35)
player = rpg_game("Player")
enemy = rpg_game("Enemy")
print(" Welcome to RPG Battle Game !!!!\n")

while player.health > 0 and enemy.health > 0:
    print("**************************************************")
    print("\nPlayer Health:",player.health)
    print("Enemy Health:",enemy.health)

    print("\nChoose your next move:")
    print("1. Attack")
    print("2. Defend")
    print("3. Heal")
    print("4. Current score")


# Each turn, the player can attack, defend, or heal.
    ch = input("Enter choice (1/2/3/4): ")
    if   ch=="1":
        player.attack(enemy)
    elif ch=="2":
        player.defend(damage)
    elif ch=="3":
        player.heal()
    elif ch=="4":
        player.current_score(enemy)
    else:
        print("Invalid choice, Please try again !!!!!!.")
        # The enemy attacks automatically each turn and deals random damage between 10 and 35.
        # The game continues until either the player or enemy’s health drops to 0 or below.
    if player.health <= 0:
        print("\n You were defeated! Game Over!")
        break
    if enemy.health <= 0:
        print("\n You defeated the enemy! You win!")
        break
   
    print("\n Enemy's turn!")
    player.damage_done(damage,enemy)

print("___END GAME___")