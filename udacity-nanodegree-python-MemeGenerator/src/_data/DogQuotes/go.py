import subprocess

x = subprocess.check_output(['xpdf','DogQuotesPDF.pdf'], shell=True)

