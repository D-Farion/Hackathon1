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
            for i, line in enumerate(lines):
                # find the relevant information for adding to calendar
                print(f"Line {i}: {line}")

#todo
#parse lines to extract class name, date, day, time, description from lines
#reformat information extracted into a single format. eg. A1 and Assignment 1 both becoming Assignment 1 in the class
#in case of duplicates check new added class description with existing ones
    
main()