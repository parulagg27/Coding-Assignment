from io import BytesIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import pprint


def convert_PDFtoText(path, pages=None):
	if not pages:
		pagenums = set()
	else:
		pagenums = set(pages)

	output = BytesIO()
	resource_manager = PDFResourceManager()
	codec = 'utf-8'

	converter = TextConverter(resource_manager, output, codec=codec, laparams=LAParams())
	interpreter = PDFPageInterpreter(resource_manager, converter)

	infile = open(path, 'rb')
	for page in PDFPage.get_pages(infile, pagenums):
		interpreter.process_page(page)

	infile.close()
	converter.close()
	text = output.getvalue()
	output.close
	return text


def main():
	resume_text = convert_PDFtoText("../Coding-Assignment/resume-parser/myresume.pdf")
	pprint.pprint (resume_text)
	print (type(resume_text))


if __name__ == '__main__':
	main()