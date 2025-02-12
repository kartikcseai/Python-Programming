# write a python program to convert time from 12-hour to 24-hour format.

def convert_to_24_hour(time_str):
    from datetime import datetime
    try:
        # Parse the input time in 12-hour format
        time_obj = datetime.strptime(time_str, "%I:%M %p")
        # Convert to 24-hour format
        return time_obj.strftime("%H:%M")
    except ValueError:
        return "Invalid time format. Please use HH:MM AM/PM."

# Example usage
time_input = input("Enter time in 12-hour format (HH:MM AM/PM): ")
converted_time = convert_to_24_hour(time_input)
print("Time in 24-hour format:", converted_time)
