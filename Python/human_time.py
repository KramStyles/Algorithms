def human_time(seconds):
    value = seconds / 3600
    hours = int(value)
    partial_mins = (value % 1) * 60
    mins = int(partial_mins) 
    secs = round((partial_mins % 1) * 60)

    if hours < 10:
        hours = f"0{hours}"
    if secs == 60:
        secs = "00"
        mins += 1
    if mins < 10:
        mins = f"0{mins}"
    if secs < 10:
        secs = f"0{secs}"
    
    return(f"{hours}:{mins}:{secs}")


print(human_time(82874))
print(human_time(5))