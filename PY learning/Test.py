import time

# Get user input and convert to numbers
round_seconds = int(input('🔥 Burn time (seconds): '))
rest_seconds = int(input('⚡️ Recharge (seconds): '))
round_times = int(input('🛎️ How many rounds: '))

# Calculate total workout time
total_time_seconds = (round_seconds + rest_seconds) * round_times
total_time_minutes = total_time_seconds / 60

print(f'🔥 Starting your {total_time_minutes:.1f} minute workout! 🔥')
print("Get ready...")
time.sleep(3)  # Give them 3 seconds to get ready

# Main workout loop - go through each round
for current_round in range(1, round_times + 1):
    
    # WORK ROUND
    print(f"\n🥊 ROUND {current_round} - FIGHT!")
    work_time_left = round_seconds
    
    # Countdown for work period
    while work_time_left > 0:
        minutes = work_time_left // 60
        seconds = work_time_left % 60
        print(f"🔥 WORK: {minutes}:{seconds:02d}")
        time.sleep(1)
        work_time_left -= 1
    
    print("🔔 Work round complete!")
    
    # REST PERIOD (only if it's not the last round)
    if current_round < round_times:
        print(f"\n💤 REST TIME")
        rest_time_left = rest_seconds
        
        # Countdown for rest period  
        while rest_time_left > 0:
            minutes = rest_time_left // 60
            seconds = rest_time_left % 60
            print(f"⚡️ REST: {minutes}:{seconds:02d}")
            time.sleep(1)
            rest_time_left -= 1
        
        print("⏰ Rest over - get ready!")
        time.sleep(2)  # Short prep time

# Workout complete!
print("\n🎉 WORKOUT COMPLETE! 🎉")
print("Great job! 💪")