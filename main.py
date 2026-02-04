from parseLogic import parsePDF, calendarEvent

def main():  
    events = parsePDF("example3.pdf")

    for event in events:
        print(event)
        print("Source: ", event.source_line, "\n")

main()