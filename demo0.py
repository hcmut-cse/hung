from __future__ import division
import os
import re
import numpy as np
from difflib import SequenceMatcher
import pdftotext

if __name__ == '__main__':
    # file = os.listdir()
    # file = list(filter(lambda ef: ef[0] != "." and ef[-3:] == "pdf", file))

    file = ["SBL_FDS_FDSLSGN190223OS.190219164902/SBL_FDS_FDSLSGN190223OS.190219164902.pdf"]
    for filename in file:
        # Covert PDF to string by page
        print(filename)

        with open(filename, "rb") as f:
        #     for i in f:
        #         print(i)
            pdf = pdftotext.PDF(f)

        # Remove header & footer
        if (len(pdf) > 1):
            fullPdf = []
            for i in range(len(pdf)):
                fullPdf.append(pdf[i].split('\n'))
            # Remove header
            row = 0
            continueRemove = True
            while (True):
                for i in range(len(fullPdf) - 1):
                    if SequenceMatcher(None, ''.join(fullPdf[0][row].split()), ''.join(fullPdf[i+1][row].split())).ratio() < 0.8:
                        continueRemove = False
                        break
                if (continueRemove):
                    for i in range(len(fullPdf)):
                        del(fullPdf[i][row])
                else:
                    break

            # Remove footer
            continueRemove = True
            while (True):
                row = [len(page)-1 for page in fullPdf]
                for i in range(len(fullPdf) - 1):
                    if SequenceMatcher(None, ''.join(fullPdf[0][row[0]].split()), ''.join(fullPdf[i+1][row[i+1]].split())).ratio() < 0.8:
                        continueRemove = False
                        break
                if (continueRemove):
                    for i in range(len(fullPdf)):
                        del(fullPdf[i][row[i]])
                else:
                    break

            # Join PDF
            fullPdf = [line for page in fullPdf for line in page]
        else:
            fullPdf = pdf[0].split('\n')

        if (fullPdf[0] != ""):
            with open(filename[:-3]+"txt", "w+") as f:
                for line in fullPdf:
                    f.write(line + '\n')
