from parseLogic import parsePDF, calendarEvent
from calendarApi import logIn

def main():  
    
    events = parsePDF("example3.pdf")
    for event in events:
        logIn(event)

main()