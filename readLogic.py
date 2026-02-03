import pypdf
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
    # Open the PDF file
    with open(file_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        text = ""
        # Extract text from each page
        for page in reader.pages:
            text += page.extract_text() + "\n"
            
        #divide the extracted text into seperate lines
        if text:
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
    print(line)

#todo
#reformat information extracted into a single format. eg. A1 and Assignment 1 both becoming Assignment 1 in the class
#in case of duplicates check new added class description with existing ones
    
main()