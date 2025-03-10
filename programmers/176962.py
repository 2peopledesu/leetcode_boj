def solution(plans):
    answer = []
    
    for plan in plans:
        hour, minute = plan[1].split(':')
        plan[1] = int(hour) * 60 + int(minute)
        plan[2] = int(plan[2])
    
    plans.sort(key=lambda x: x[1])
    
    stopped = []
    
    for i in range(len(plans)):
        current_name, current_start, current_time = plans[i]
        
        next_start = plans[i+1][1] if i < len(plans) - 1 else float('inf')
        
        finish_time = current_start + current_time
        
        if finish_time <= next_start:
            answer.append(current_name)
            
            remaining_time = next_start - finish_time
            while remaining_time > 0 and stopped:
                stopped_name, stopped_time = stopped.pop()
                
                if stopped_time <= remaining_time:
                    answer.append(stopped_name)
                    remaining_time -= stopped_time

                else:
                    stopped.append([stopped_name, stopped_time - remaining_time])
                    remaining_time = 0
        
        else:
            remaining_work = finish_time - next_start
            stopped.append([current_name, remaining_work])
    
    while stopped:
        answer.append(stopped.pop()[0])
    
    return answer