import pypdf
import calendar

class scheduleDate:
    def __init__(self, class_name, date, day, time, description):
        self.class_name = class_name
        self.date = date
        self.day = day
        self.time = time
        self.description = description  #What the calalandar entry is actually for. eg. "Assignment 1"

def main():
    print(read_pdf("example3.pdf", "COMP"))

def read_pdf(file_path, class_name):
    with open(file_path, 'rb') as file: # Open the PDF file
        reader = pypdf.PdfReader(file)
        text = ""
        
        for page in reader.pages: # Extract text from each page
            text += page.extract_text() + "\n"
            
        if text: #divide the extracted text into seperate lines
            lines = text.split("\n")
            for line in lines:
                # find the relevant information for adding to calendar
                parse_line(line)

def parse_line(line):
    #parse line to extract date, day, time, and description from line
    #   for date look for month followed by a number
    #   for day look for day names
    #   for description look for keywords like Assignment, A, Quiz, Q, Test, Exam, Lab, Tutorial, Project and a following number
    #add extracted information to a scheduleDate object
    #if line dosent contain relevant information return None and dont make new scheduleDate object

    months = list(m.lower() for m in calendar.month_name)[1:] # Get list of month names
    months += list(m.lower() for m in calendar.month_abbr)[1:] # Get list of month abbreviations and add to prior list
    days = list(d.lower() for d in calendar.day_name) # Get list of day names
    days += list(d.lower() for d in calendar.day_abbr) # Get list of day abbreviations and add to prior list
    description_types = ["assignment", "a", "quiz", "q", "test", "exam", "lab", "tutorial", "project"]
    for word in line.split(): # Clean the word (remove potential commas, periods, and convert to lowercase)
        cleaned_word = word.strip(',.').lower()
        if cleaned_word in months: # Check if the cleaned word is a month
            print(f"Found month: {cleaned_word} in line: {line}")
            #need to check if a number follows for it to be a valid date
        elif cleaned_word in days: # Check if the cleaned word is a day
            print(f"Found day: {cleaned_word} in line: {line}")
        elif cleaned_word in description_types:
            print(f"Found description: {cleaned_word} in line: {line}")
            #need to check if a number follows it


#todo
#reformat information extracted into a single format. eg. A1 and Assignment 1 both becoming Assignment 1 in the class
#in case of duplicates check new added class description with existing ones
    
main()