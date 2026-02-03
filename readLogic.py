import pypdf
class scheduleDate:
    def __init__(self, date, day, time, description):
        self.date = date
        self.day = day
        self.time = time
        self.description = description

def main():
    print(read_pdf("example.pdf"))

def read_pdf(file_path):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        text = ""
        # Extract text from each page
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

main()