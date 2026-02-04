import re
from pypdf import PdfReader


# event class 
class calendarEvent:
    def __init__(self, title, date, source_line):
        self.title = title
        self.date = date
        self.source_line = source_line

    def __repr__(self):
        return f"Event(title = {self.title}, date = {self.date})"


#keywords and date patters
check = ["final", "assignment", "quiz", "test", "exam", "lab", "tutorial", "project", "midterm"]
numbers = [" 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", " 10", ""]
keywords = [i + j for i in check for j in numbers]

DATE_PATTERN = re.compile(
    r"(\b\d{4}-\d{2}-\d{2}\b|"          # the format 2026-03-15
    r"\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+\d{1,2}"
    r"(?:,\s*\d{4})?\b)",
    re.IGNORECASE
)

#helper to find keywords
def find_keyword(line):
    for kw in keywords:
        if kw in line:
            return kw
    return None

#parse pdf

def parsePDF(file_path):
    events = []

    reader = PdfReader(file_path)

    for page in reader.pages:
        text = page.extract_text()
        if not text:
            continue

        lines = text.split("\n")
        for line in lines:
            lower_line = line.strip(':,.()').lower()

            #check keyword
            keyword = find_keyword(lower_line)
            if not keyword:
                continue

            #check date
            date_match = DATE_PATTERN.search(line)
            if not date_match:
                continue

            date_str = date_match.group()

            #prepare event for api
            event = calendarEvent(
                title=keyword.capitalize(),
                date=date_str,
                source_line = line.strip()
            )

            events.append(event)

    return events

#test
if __name__ == "__main__":
    events = parsePDF("example3.pdf")

    for event in events:
        print(event)
        print("Source: ", event.source_line, "\n")