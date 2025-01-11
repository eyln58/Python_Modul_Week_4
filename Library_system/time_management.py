from datetime import datetime, timedelta

def generate_return_date():
    
    try:
        current_time = datetime.now()
        return_date = current_time + timedelta(weeks=2)

        current_time_str = current_time.strftime("%d-%m-%Y,%H:%M")
        return_date_str = return_date.strftime("%d-%m-%Y")

        return current_time_str, return_date_str
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None