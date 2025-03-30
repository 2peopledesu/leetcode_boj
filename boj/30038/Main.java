import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Game game = new Game();
        game.run();
    }
    
    static class Game {
        private GameMap gameMap;
        private Player player;
        private List<Monster> monsters;
        private String[] actions;
        
        public void run() throws IOException {
            initialize();
            playGame();
            printResult();
        }
        
        private void initialize() throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            
            gameMap = new GameMap(n, m);
            player = new Player();
            
            // 맵 초기화
            for (int y = 0; y < n; y++) {
                String line = br.readLine();
                for (int x = 0; x < m; x++) {
                    char c = line.charAt(x);
                    if (c == 'p') {
                        player.setPosition(y, x);
                        gameMap.setCell(y, x, 'p');
                    } else {
                        gameMap.setCell(y, x, c);
                    }
                }
            }

            // 몬스터 정보 초기화
            int monsterCount = Integer.parseInt(br.readLine());
            monsters = new ArrayList<>(monsterCount);
            
            st = new StringTokenizer(br.readLine());
            int[] health = new int[monsterCount];
            for (int i = 0; i < monsterCount; i++) {
                health[i] = Integer.parseInt(st.nextToken());
            }
            
            st = new StringTokenizer(br.readLine());
            int[] defense = new int[monsterCount];
            for (int i = 0; i < monsterCount; i++) {
                defense[i] = Integer.parseInt(st.nextToken());
            }
            
            st = new StringTokenizer(br.readLine());
            int[] exp = new int[monsterCount];
            for (int i = 0; i < monsterCount; i++) {
                exp[i] = Integer.parseInt(st.nextToken());
            }
            
            // 몬스터 객체 생성 및 맵에 배치
            int mIndex = 0;
            for (int y = 0; y < n; y++) {
                for (int x = 0; x < m; x++) {
                    if (gameMap.getCell(y, x) == 'm') {
                        Monster monster = new Monster(mIndex + 1, health[mIndex], defense[mIndex], exp[mIndex], y, x);
                        monsters.add(monster);
                        gameMap.setCell(y, x, 'm');
                        mIndex++;
                    }
                }
            }
            
            // 행동 입력
            int actionCount = Integer.parseInt(br.readLine());
            actions = br.readLine().split(" ");
        }
        
        private void playGame() {
            for (String action : actions) {
                // OVERDOSE 상태 확인
                if (player.isOverdosed() && !(action.equals("u") || action.equals("d") || action.equals("l") || action.equals("r") || action.equals("w"))) {
                    continue;
                }
                
                // OVERDOSE 상태 해제 확인
                if (player.getOverdoseAction() >= 10) {
                    player.clearOverdose();
                }
                
                boolean actionCompleted = false;
                
                switch (action) {
                    case "u": // 위로 이동
                        actionCompleted = move(-player.getSpeed(), 0);
                        break;
                    case "d": // 아래로 이동
                        actionCompleted = move(player.getSpeed(), 0);
                        break;
                    case "l": // 왼쪽으로 이동
                        actionCompleted = move(0, -player.getSpeed());
                        break;
                    case "r": // 오른쪽으로 이동
                        actionCompleted = move(0, player.getSpeed());
                        break;
                    case "w": // 대기
                        player.increaseActionPoints(1);
                        actionCompleted = true;
                        break;
                    case "au": // 위로 공격
                        actionCompleted = attack(-1, 0);
                        break;
                    case "ad": // 아래로 공격
                        actionCompleted = attack(1, 0);
                        break;
                    case "al": // 왼쪽으로 공격
                        actionCompleted = attack(0, -1);
                        break;
                    case "ar": // 오른쪽으로 공격
                        actionCompleted = attack(0, 1);
                        break;
                    case "du": // 이동속도 증가 약
                        player.takeDrug(true);
                        actionCompleted = true;
                        break;
                    case "dd": // 이동속도 감소 약
                        player.takeDrug(false);
                        actionCompleted = true;
                        break;
                    case "c": // 클리어
                        if (checkClear()) {
                            return;
                        }
                        break;
                }
                
                player.checkLevelUp();
            }
        }
        
        private boolean move(int dy, int dx) {
            int ny = player.getY() + dy;
            int nx = player.getX() + dx;
            
            if (!gameMap.isValidPosition(ny, nx)) {
                return false;
            }
            
            char target = gameMap.getCell(ny, nx);
            
            if (target == '.') {
                // 빈 칸으로 이동
                if (!player.isOnGoal()) {
                    gameMap.setCell(player.getY(), player.getX(), '.');
                }
                player.setPosition(ny, nx);
                gameMap.setCell(ny, nx, 'p');
                player.increaseActionPoints(1);
                player.setOnGoal(false);
                return true;
            } else if (target == 'g') {
                // 목적지 도달 - 맵에서 g를 지우지 않고 플레이어 위치만 업데이트
                gameMap.setCell(player.getY(), player.getX(), '.');
                player.setPosition(ny, nx);
                // 'g'를 'p'로 대체하지 않고, 플레이어가 목적지에 있음을 표시
                player.setOnGoal(true);
                player.increaseActionPoints(1);
                return true;
            }
            
            return false;
        }
        
        private boolean attack(int dy, int dx) {
            player.increaseActionPoints(3);
            
            int range = player.getRange();
            int y = player.getY();
            int x = player.getX();
            
            for (int i = 1; i <= range; i++) {
                int ny = y + dy * i;
                int nx = x + dx * i;
                
                if (!gameMap.isValidPosition(ny, nx)) {
                    break;
                }
                
                char cell = gameMap.getCell(ny, nx);
                
                if (cell == '*') {
                    break; // 장애물을 만나면 투사체 소멸
                }
                
                for (Monster monster : monsters) {
                    if (monster.getY() == ny && monster.getX() == nx && monster.isAlive()) {
                        int damage = player.getAttack() - monster.getDefense();
                        if (damage > 0) {
                            monster.takeDamage(damage);
                            if (!monster.isAlive()) {
                                gameMap.setCell(ny, nx, '.');
                                player.gainExperience(monster.getExp());
                            }
                        }
                    }
                }
            }
            
            return true;
        }
        
        private boolean checkClear() {
            int y = player.getY();
            int x = player.getX();
            
            return gameMap.getCell(y, x) == 'g';
        }
        
        private Monster getMonsterById(int id) {
            for (Monster monster : monsters) {
                if (monster.getId() == id) {
                    return monster;
                }
            }
            return null;
        }
        
        private void printResult() throws IOException {
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            
            // 레벨과 경험치 출력
            bw.write(player.getLevel() + " " + player.getExperience() + "\n");
            
            // 행동력 출력
            bw.write(player.getActionPoints() + "\n");
            
            // 게임판 상태 출력
            for (int y = 0; y < gameMap.getHeight(); y++) {
                for (int x = 0; x < gameMap.getWidth(); x++) {
                    char cell = gameMap.getCell(y, x);
                    boolean isMonsterAlive = false;
                    for (Monster monster : monsters) {
                        if (monster.getY() == y && monster.getX() == x && monster.isAlive()) {
                            isMonsterAlive = true;
                            break;
                        }
                    }
                    if (player.isOnGoal() && y == player.getY() && x == player.getX()) {
                        bw.write('p');
                    } else if (isMonsterAlive) {
                        bw.write('m');
                    } else {
                        bw.write(cell);
                    }
                }
                bw.write("\n");
            }
            
            // 남아있는 몬스터 체력 출력 - 정렬 방식 수정
            List<Monster> aliveMonsters = new ArrayList<>();
            for (int y = 0; y < gameMap.getHeight(); y++) {
                for (int x = 0; x < gameMap.getWidth(); x++) {
                    if (gameMap.getCell(y, x) == 'm') {
                        for (Monster monster : monsters) {
                            if (monster.getY() == y && monster.getX() == x && monster.isAlive()) {
                                aliveMonsters.add(monster);
                            }
                        }
                    }
                }
            }
            
            Collections.sort(aliveMonsters, (m1, m2) -> {
                if (m1.getY() == m2.getY()) {
                    return Integer.compare(m1.getX(), m2.getX());
                }
                return Integer.compare(m1.getY(), m2.getY());
            });
            
            if (!aliveMonsters.isEmpty()) {
                for (int i = 0; i < aliveMonsters.size(); i++) {
                    bw.write(String.valueOf(aliveMonsters.get(i).getHealth()));
                    if (i < aliveMonsters.size() - 1) {
                        bw.write(" ");
                    }
                }
                bw.write("\n");
            }

            bw.flush();
            bw.close();
        }
    }
    
    static class Player {
        private int attack = 5;
        private int range = 1;
        private int speed = 1;
        private int requiredExp = 10;
        private int experience = 0;
        private int level = 1;
        private int actionPoints = 0;
        private int drugCount = 0;
        private int overdoseAction = 0;
        private int y, x;
        private boolean overdosed = false;
        private boolean onGoal = false;
        
        public void setPosition(int y, int x) {
            this.y = y;
            this.x = x;
        }
        
        public int getY() {
            return y;
        }
        
        public int getX() {
            return x;
        }
        
        public int getAttack() {
            return attack;
        }
        
        public int getRange() {
            return range;
        }
        
        public int getSpeed() {
            return speed;
        }
        
        public int getLevel() {
            return level;
        }
        
        public int getExperience() {
            return experience;
        }
        
        public int getActionPoints() {
            return actionPoints;
        }
        
        public void increaseActionPoints(int points) {
            actionPoints += points;
            if (overdosed) {
                overdoseAction += points;
            }
        }
        
        public boolean isOverdosed() {
            return overdosed;
        }
        
        public int getOverdoseAction() {
            return overdoseAction;
        }
        
        public void clearOverdose() {
            overdosed = false;
            overdoseAction = 0;
        }
        
        public void takeDrug(boolean increase) {
            increaseActionPoints(2);
            
            if (increase) {
                speed += 1;
            } else {
                speed = Math.max(0, speed - 1);
            }
            
            drugCount++;
            if (drugCount >= 5) {
                overdosed = true;
                drugCount = 0;
                overdoseAction = 0;
            }
        }
        
        public void gainExperience(int exp) {
            experience += exp;
        }
        
        public void checkLevelUp() {
            while (experience >= requiredExp) {
                experience -= requiredExp;
                attack += level;
                level++;
                range += 1;
                requiredExp += 10;
            }
        }
        
        public void setOnGoal(boolean onGoal) {
            this.onGoal = onGoal;
        }
        
        public boolean isOnGoal() {
            return onGoal;
        }
        
        @Override
        public String toString() {
            return "Player{" +
                    "attack=" + attack +
                    ", range=" + range +
                    ", speed=" + speed +
                    ", requiredExp=" + requiredExp +
                    ", experience=" + experience +
                    ", level=" + level +
                    ", actionPoints=" + actionPoints +
                    ", drugCount=" + drugCount +
                    ", overdoseAction=" + overdoseAction +
                    ", position=(" + y + "," + x + ")" +
                    ", overdosed=" + overdosed +
                    ", onGoal=" + onGoal +
                    '}';
        }
    }
    
    static class Monster {
        private final int id;
        private int health;
        private final int defense;
        private final int exp;
        private final int y, x;
        
        public Monster(int id, int health, int defense, int exp, int y, int x) {
            this.id = id;
            this.health = health;
            this.defense = defense;
            this.exp = exp;
            this.x = x;
            this.y = y;
        }
        
        public int getId() {
            return id;
        }
        
        public int getHealth() {
            return health;
        }
        
        public int getDefense() {
            return defense;
        }
        
        public int getExp() {
            return exp;
        }
        
        public int getY() {
            return y;
        }
        
        public int getX() {
            return x;
        }   
        
        public boolean isAlive() {
            return health > 0;
        }
        
        public void takeDamage(int damage) {
            health -= damage;
        }
    }
    
    static class GameMap {
        private final char[][] map;
        private final int height;
        private final int width;
        private int goalY, goalX;
        
        public GameMap(int height, int width) {
            this.height = height;
            this.width = width;
            map = new char[height][width];
        }
        
        public void setCell(int y, int x, char value) {
            if (value == 'g') {
                goalY = y;
                goalX = x;
            }
            map[y][x] = value;
        }
        
        public char getCell(int y, int x) {
            return map[y][x];
        }
        
        public boolean isValidPosition(int y, int x) {
            return y >= 0 && y < height && x >= 0 && x < width;
        }
        
        public int getHeight() {
            return height;
        }
        
        public int getWidth() {
            return width;
        }
        
        public boolean isGoalPosition(int y, int x) {
            return y == goalY && x == goalX;
        }
    }
}