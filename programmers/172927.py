def solution(picks, minerals):
    available_picks = sum(picks)
    
    mineral_groups = min(available_picks, (len(minerals) + 4) // 5)
    
    fatigue_by_group = []
    
    for i in range(mineral_groups):
        start_idx = i * 5
        end_idx = min(start_idx + 5, len(minerals))
        current_minerals = minerals[start_idx:end_idx]
        
        diamond_fatigue = 0
        iron_fatigue = 0
        stone_fatigue = 0
        
        for mineral in current_minerals:
            if mineral == "diamond":
                diamond_fatigue += 1
                iron_fatigue += 5
                stone_fatigue += 25
            elif mineral == "iron":
                diamond_fatigue += 1
                iron_fatigue += 1
                stone_fatigue += 5
            else:
                diamond_fatigue += 1
                iron_fatigue += 1
                stone_fatigue += 1
        
        fatigue_by_group.append((stone_fatigue, iron_fatigue, diamond_fatigue))
    
    fatigue_by_group.sort(reverse=True)
    
    total_fatigue = 0
    for stone_f, iron_f, dia_f in fatigue_by_group:
        if picks[0] > 0:
            total_fatigue += dia_f
            picks[0] -= 1
        elif picks[1] > 0:
            total_fatigue += iron_f
            picks[1] -= 1
        elif picks[2] > 0:
            total_fatigue += stone_f
            picks[2] -= 1
    
    return total_fatigue