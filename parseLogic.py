import re
from pypdf import PdfReader
from datetime import datetime, timezone


# event class 
class calendarEvent:
    def __init__(self, title, startDate, endDate):
        self.title = title
        self.startDate = startDate
        self.endDate = endDate

    def __repr__(self):
        return f"Event(title = {self.title}, startDate = {self.startDate}, endDate = {self.endDate})"


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
            current_year = datetime.now().year
            date_str = f"{date_str} {current_year}"
            dt = datetime.strptime(date_str, "%b %d %Y")

            # 2. Convert to UTC and then to RFC3339 format
            # Using .replace(tzinfo=timezone.utc) assumes the input is UTC
            start = dt.replace(tzinfo=timezone.utc).isoformat()
            end = dt.replace(hour=23, minute=59, second=0, microsecond=0, tzinfo=timezone.utc).isoformat()

            #prepare event for api
            event = calendarEvent(
                title=keyword.capitalize(),
                startDate=start,
                endDate=end,
            )

            events.append(event)

    return events
