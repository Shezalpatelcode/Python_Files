# Number of works
N = int(input())

for _ in range(N):
    SH, SM, EH, EM = map(int, input().split())
    
    # Convert start and end times to minutes
    start_minutes = SH * 60 + SM
    end_minutes = EH * 60 + EM
    
    # Calculate duration in minutes
    duration = end_minutes - start_minutes
    
    # Convert back to HH MM
    HH = duration // 60
    MM = duration % 60
    
    print(HH, MM)
