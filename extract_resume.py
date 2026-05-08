import zipfile
import xml.etree.ElementTree as ET

# Path to the .docx file
docx_path = r"c:\Users\saman\OneDrive\Desktop\Bruner Spring 26 Resume.docx"

# Extract text from the Word document
def extract_docx_text(docx_path):
    text = []
    with zipfile.ZipFile(docx_path, 'r') as zip_ref:
        # Read the main document XML
        xml_content = zip_ref.read('word/document.xml')
        
    # Parse XML
    root = ET.fromstring(xml_content)
    
    # Namespace for Word documents
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    
    # Extract all text elements
    for paragraph in root.findall('.//w:p', ns):
        para_text = []
        for text_elem in paragraph.findall('.//w:t', ns):
            if text_elem.text:
                para_text.append(text_elem.text)
        if para_text:
            text.append(''.join(para_text))
    
    return text

# Extract and print
resume_text = extract_docx_text(docx_path)
for line in resume_text:
    print(line)
