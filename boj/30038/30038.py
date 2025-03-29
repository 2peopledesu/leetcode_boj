import sys

class GameMap:
    def __init__(self, height, width):
        self.map = [['' for _ in range(width)] for _ in range(height)]
        self.height = height
        self.width = width
        self.goal_y, self.goal_x = 0, 0
    
    def set_cell(self, y, x, value):
        if value == 'g':
            self.goal_y = y
            self.goal_x = x
        self.map[y][x] = value
    
    def get_cell(self, y, x):
        return self.map[y][x]
    
    def is_valid_position(self, y, x):
        return 0 <= y < self.height and 0 <= x < self.width
    
    def is_goal_position(self, y, x):
        return y == self.goal_y and x == self.goal_x

class Monster:
    def __init__(self, id, health, defense, exp, y, x):
        self.id = id
        self.health = health
        self.defense = defense
        self.exp = exp
        self.y = y
        self.x = x
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        self.health -= damage

class Player:
    def __init__(self):
        self.attack = 5
        self.range = 1
        self.speed = 1
        self.required_exp = 10
        self.experience = 0
        self.level = 1
        self.action_points = 0
        self.drug_count = 0
        self.overdose_action = 0
        self.y, self.x = 0, 0
        self.overdosed = False
        self.on_goal = False
    
    def set_position(self, y, x):
        self.y = y
        self.x = x
    
    def increase_action_points(self, points):
        self.action_points += points
        if self.overdosed:
            self.overdose_action += points
    
    def is_overdosed(self):
        return self.overdosed
    
    def clear_overdose(self):
        self.overdosed = False
        self.overdose_action = 0
    
    def take_drug(self, increase):
        self.increase_action_points(2)
        
        if increase:
            self.speed += 1
        else:
            self.speed = max(0, self.speed - 1)
        
        self.drug_count += 1
        if self.drug_count >= 5:
            self.overdosed = True
            self.drug_count = 0
            self.overdose_action = 0
    
    def gain_experience(self, exp):
        self.experience += exp
    
    def check_level_up(self):
        while self.experience >= self.required_exp:
            self.experience -= self.required_exp
            self.attack += self.level
            self.level += 1
            self.range += 1
            self.required_exp += 10

class Game:
    def __init__(self):
        self.game_map = None
        self.player = None
        self.monsters = []
        self.actions = []
    
    def run(self):
        self.initialize()
        self.play_game()
        self.print_result()
    
    def initialize(self):
        n, m = map(int, input().split())
        
        self.game_map = GameMap(n, m)
        self.player = Player()
        
        # Initialize map
        for y in range(n):
            line = input()
            for x in range(m):
                c = line[x]
                if c == 'p':
                    self.player.set_position(y, x)
                self.game_map.set_cell(y, x, c)
        
        # Initialize monsters
        monster_count = int(input())
        self.monsters = []
        
        health = list(map(int, input().split()))
        defense = list(map(int, input().split()))
        exp = list(map(int, input().split()))
        
        # Create monster objects and place them on the map
        m_index = 0
        for y in range(n):
            for x in range(m):
                if self.game_map.get_cell(y, x) == 'm':
                    monster = Monster(m_index + 1, health[m_index], defense[m_index], exp[m_index], y, x)
                    self.monsters.append(monster)
                    m_index += 1
        
        # Read actions
        action_count = int(input())
        self.actions = input().split()
    
    def play_game(self):
        for action in self.actions:
            # Check if player is overdosed
            if self.player.is_overdosed() and action not in ["u", "d", "l", "r", "w"]:
                continue
            
            # Check if overdose state should be cleared
            if self.player.overdose_action >= 10:
                self.player.clear_overdose()
            
            action_completed = False
            
            if action == "u":  # Move up
                action_completed = self.move(-self.player.speed, 0)
            elif action == "d":  # Move down
                action_completed = self.move(self.player.speed, 0)
            elif action == "l":  # Move left
                action_completed = self.move(0, -self.player.speed)
            elif action == "r":  # Move right
                action_completed = self.move(0, self.player.speed)
            elif action == "w":  # Wait
                self.player.increase_action_points(1)
                action_completed = True
            elif action == "au":  # Attack up
                action_completed = self.attack(-1, 0)
            elif action == "ad":  # Attack down
                action_completed = self.attack(1, 0)
            elif action == "al":  # Attack left
                action_completed = self.attack(0, -1)
            elif action == "ar":  # Attack right
                action_completed = self.attack(0, 1)
            elif action == "du":  # Take speed increase drug
                self.player.take_drug(True)
                action_completed = True
            elif action == "dd":  # Take speed decrease drug
                self.player.take_drug(False)
                action_completed = True
            elif action == "c":  # Check clear
                if self.check_clear():
                    return
            
            self.player.check_level_up()
    
    def move(self, dy, dx):
        ny = self.player.y + dy
        nx = self.player.x + dx
        
        if not self.game_map.is_valid_position(ny, nx):
            return False
        
        target = self.game_map.get_cell(ny, nx)
        
        if target == '.':
            # Move to empty cell
            if not self.player.on_goal:
                self.game_map.set_cell(self.player.y, self.player.x, '.')
            self.player.set_position(ny, nx)
            self.game_map.set_cell(ny, nx, 'p')
            self.player.increase_action_points(1)
            self.player.on_goal = False
            return True
        elif target == 'g':
            # Reach goal
            self.game_map.set_cell(self.player.y, self.player.x, '.')
            self.player.set_position(ny, nx)
            self.player.on_goal = True
            self.player.increase_action_points(1)
            return True
        
        return False
    
    def attack(self, dy, dx):
        self.player.increase_action_points(3)
        
        range_val = self.player.range
        y = self.player.y
        x = self.player.x
        
        for i in range(1, range_val + 1):
            ny = y + dy * i
            nx = x + dx * i
            
            if not self.game_map.is_valid_position(ny, nx):
                break
            
            cell = self.game_map.get_cell(ny, nx)
            
            if cell == '*':
                break  # Projectile hits obstacle
            
            for monster in self.monsters:
                if monster.y == ny and monster.x == nx and monster.is_alive():
                    damage = self.player.attack - monster.defense
                    if damage > 0:
                        monster.take_damage(damage)
                        if not monster.is_alive():
                            self.game_map.set_cell(ny, nx, '.')
                            self.player.gain_experience(monster.exp)
        
        return True
    
    def check_clear(self):
        y = self.player.y
        x = self.player.x
        
        return self.game_map.get_cell(y, x) == 'g'
    
    def print_result(self):
        # Print level and experience
        print(f"{self.player.level} {self.player.experience}")
        
        # Print action points
        print(self.player.action_points)
        
        # Print game map
        for y in range(self.game_map.height):
            row = ""
            for x in range(self.game_map.width):
                cell = self.game_map.get_cell(y, x)
                is_monster_alive = False
                for monster in self.monsters:
                    if monster.y == y and monster.x == x and monster.is_alive():
                        is_monster_alive = True
                        break
                
                if self.player.on_goal and y == self.player.y and x == self.player.x:
                    row += 'p'
                elif is_monster_alive:
                    row += 'm'
                else:
                    row += cell
            print(row)
        
        # Print remaining monster health
        alive_monsters = [monster for monster in self.monsters if monster.is_alive()]
        
        # Sort monsters by position
        alive_monsters.sort(key=lambda m: (m.y, m.x))
        
        if alive_monsters:
            print(" ".join(str(monster.health) for monster in alive_monsters))

if __name__ == "__main__":
    game = Game()
    game.run()