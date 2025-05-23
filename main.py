import os, sys, re
from PyPDF2 import PdfMerger

DROPBOX = os.getcwd()
files = sorted(
	(f for f in os.listdir(DROPBOX) if f.lower().endswith(".pdf")),
	key=lambda s: [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', s)]
)

print("Merge order:")
for i, f in enumerate(files, 1): print(f"{i}. {f}")
if input("Continue? (y/n): ").strip().lower() != "y": sys.exit(0)

m = PdfMerger()
[m.append(os.path.join(DROPBOX, f)) for f in files]
m.write(sys.argv[1])
m.close()