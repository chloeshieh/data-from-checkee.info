#!d:\checkee\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'table2csv==0.1.3','console_scripts','table2csv'
__requires__ = 'table2csv==0.1.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('table2csv==0.1.3', 'console_scripts', 'table2csv')()
    )
