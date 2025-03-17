def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver_sum = 0
    pickup_sum = 0
    max_trips = 0
    
    for i in reversed(range(len(deliveries))):
        deliver_sum += deliveries[i]
        pickup_sum += pickups[i]
        
        current_trips = max((deliver_sum + cap - 1) // cap, (pickup_sum + cap - 1) // cap)
        delta = current_trips - max_trips
        
        if delta > 0:
            answer += delta * (i + 1) * 2
            max_trips = current_trips
    
    return answer