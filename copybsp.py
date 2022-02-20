#!/usr/bin/env python
import shutil
import os
import sys
if len(sys.argv) <= 1:
    print("Error, you must enter a file argument, exiting")
    exit(0)
if not os.path.exists(sys.argv[1]):
    print("Error, you must enter a valid file ")
    exit(0)
filetocopy = sys.argv[1]
targetdir = os.getcwd()
print(f"Ich werde jetzt gleich das file {filetocopy} dahin kopieren {targetdir}")
shutil.copy(filetocopy,targetdir)
print(f"Ich habe jetzt das file   {filetocopy} erfolgreich hierin {targetdir} kopiert")
print("Done.")
