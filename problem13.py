# Create a function that takes a datetime object as input and formats it as "Month Day, Year" (e.g., "August 25, 2023") using strftime().

from datetime import datetime

def format_datetime(datetime_obj):
    
    format = "%B %d, %Y"
    
    return datetime.strftime(datetime_obj, format)

datetime_obj = datetime.fromisoformat('0001-09-03 12:30:17')

formatted_datetime = format_datetime(datetime_obj)

print(f"Date Time: {datetime_obj}")
print(f"Formatted Date: {formatted_datetime}")