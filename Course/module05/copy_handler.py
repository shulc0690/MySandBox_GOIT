import shutil
from pathlib import Path

SOURCE_DIR = r"C:\Users\Alexandr\Downloads"
doc_file = "АНАЛІЗ МОЖЛИВОСТЕЙ МОВИ ПРОГРАМУВАННЯ PYTHON.pdf"
source = Path(SOURCE_DIR).joinpath(doc_file)
copy_file = Path("data").joinpath(doc_file)

shutil.copy2(src=source, dst=copy_file)