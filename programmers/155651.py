def solution(book_time):
    events = []
    
    for start, end in book_time:
        start_minutes = int(start.split(':')[0]) * 60 + int(start.split(':')[1])
        end_minutes = int(end.split(':')[0]) * 60 + int(end.split(':')[1])
        
        events.append((start_minutes, 1))
        events.append((end_minutes + 10, -1))
    
    events.sort()
    
    current_rooms = 0
    max_rooms = 0
    
    for _, event_type in events:
        current_rooms += event_type
        max_rooms = max(max_rooms, current_rooms)
    
    return max_rooms

book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
print(solution(book_time))
