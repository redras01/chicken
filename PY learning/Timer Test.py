import time
round_seconds = int(input('🔥 Burn time (seconds): '))
rest_seconds = int(input('⚡️ Recharge (seconds): '))
round_times = int(input('🛎️ How many rounds: '))
total_time_seconds = (round_seconds + rest_seconds) * round_times
total_time_minutes = total_time_seconds / 60
if total_time_seconds >= 60:
    minutes = total_time_seconds // 60
    seconds = total_time_seconds % 60
    print(f'🔥 Start your {minutes}m {seconds}s workout 🔥')
else:
    print(f'🔥 Start your {total_time_seconds} second workout 🔥')
    print(f'\n🟠 Get ready for ROUND 1')
    countdown = 5
    while countdown > 0:
        print(f'🟠 in {countdown} seconds')
        time.sleep(1)
        countdown -= 1
for current_round in range(1, round_times + 1):
        print(f"\n🟢 ROUND {current_round}")
        work_time_left = round_seconds
        while work_time_left > 0:
            minutes = work_time_left // 60
            seconds = work_time_left % 60
            print(f'🟢 ROUND: {minutes}:{seconds:02d}')
            time.sleep(1)
            work_time_left -= 1
        if current_round < round_times:
            print("\n🔵 REST TIME")
            rest_time_left = rest_seconds
            while rest_time_left > 0:
                minutes = rest_time_left // 60
                seconds = rest_time_left % 60
                print(f"🔵 REST: {minutes}:{seconds:02d}")
                time.sleep(1)
                rest_time_left -= 1
        

print("\n🎉 WORKOUT COMPLETE! 🎉")
print("Great job! 💪")