# french phone numbers

def get_pdftxt(fp):
    with pdfplumber.open(fp) as pdf:
        first_page = pdf.pages[0]
        extracted = (first_page.extract_text(x_tolerance=3, y_tolerance=3))
        # \S matches any non-whitespace character 
        # @ for as in the Email 
        # + for Repeats a character one or more times 
        first_name = fp.strip(".pdf").split("-")[0]
        name = fp.strip(".pdf").replace("-"," ")
        email = re.findall(r'\S+@\S+', extracted) 
        phone = re.findall(r'06.\d.+?\s.+ | [+33].+\s? | *[0]6+\s\d+\s\d+\s\d+\s\d+', extracted)
        if phone:
            phone = phone[0].strip()
            phone = phone.replace("\t"," ")
            phone = phone.replace("+33","")
            phone = phone.replace("+ 33","")
            phone = phone.replace("(0) ","0")
            phone = phone.replace("(0)","0")
            phone = phone.replace("."," ").strip()
