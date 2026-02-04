from parseLogic import parsePDF, calendarEvent
from calendarApi import create_event, logIn

def main():  
    events = parsePDF("example3.pdf")
    service = logIn()
    for event in events:
        create_event(service, event)

main()