lesson_number = int(input(3))
total_minutes = (lesson_number - 1) * 45 + (lesson_number // 2) * 20
start_time = 9 * 60
end_time_minutes = start_time + total_minutes
end_hour = end_time_minutes // 60
end_minute = end_time_minutes % 60
print(end_hour, end_minute)
