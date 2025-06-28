# import traceback

# def book_event(summary, start_time, end_time):
#     try:
#         service = get_calendar_service()
#         event = {
#             'summary': summary,
#             'start': {'dateTime': start_time.isoformat(), 'timeZone': 'Asia/Kolkata'},
#             'end': {'dateTime': end_time.isoformat(), 'timeZone': 'Asia/Kolkata'},
#         }
#         event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
#         return event.get('htmlLink')
#     except Exception as e:
#         print("[ERROR] Failed to book event:", e)
#         traceback.print_exc()  # This prints the full error trace
#         return "Failed to book event."
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import traceback

SCOPES = ['https://www.googleapis.com/auth/calendar']
CALENDAR_ID = 'sujanreddy610@gmail.com'

# ✅ Define the calendar service function
def get_calendar_service():
    creds = service_account.Credentials.from_service_account_file(
        'backend/credentials.json', scopes=SCOPES)
    return build('calendar', 'v3', credentials=creds)

# ✅ Book the event using the service
def book_event(summary, start_time, end_time):
    try:
        service = get_calendar_service()
        event = {
            'summary': summary,
            'start': {
                'dateTime': start_time.isoformat(),
                'timeZone': 'Asia/Kolkata'
            },
            'end': {
                'dateTime': end_time.isoformat(),
                'timeZone': 'Asia/Kolkata'
            }
        }
        # created_event = service.events().insert(calendarId='primary', body=event).execute()
        # print("[DEBUG] Full event:", created_event)

        created_event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        print("[SUCCESS] Event created:", created_event)
        return created_event.get('htmlLink')
    # except Exception as e:
    #     print("[ERROR] Failed to book event:", str(e))
    #     traceback.print_exc()
    #     return "Failed to book event."
    except Exception as e:
        print("[ERROR] Failed to book event:", str(e))
        traceback.print_exc()
        return f"Failed to book event. Error: {str(e)}"
    

    
