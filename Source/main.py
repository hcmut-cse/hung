from __future__ import division
import os
import json
import numpy as np
from preprocess import preProcessPdf
from processData import extractData

if __name__ == '__main__':
    PDF_TYPE = "7"
    fileName = list(filter(lambda pdf: pdf[-3:] == 'pdf' ,os.listdir('../' + PDF_TYPE)))
    # fileName = ["SGNV33817500.pdf"]

    for file in fileName:
        print(file)
        # Reset Current CONFIG
        with open('../' + PDF_TYPE + '/' + PDF_TYPE + '.json', 'r', encoding='utf8') as json_file:
            CONFIG = json.load(json_file)
        CURR_CONFIG = {}

        # Sort CONFIG from top to bottom, from left to right
        configByColumn = dict(sorted(CONFIG.items(), key=lambda kv: kv[1]['column'][0]))
        CONFIG = dict(sorted(configByColumn.items(), key=lambda kv: kv[1]['row'][0]))
        # print(CONFIG)

        # Create config for current pdf
        for key in CONFIG:
            CURR_CONFIG[key] = {}
            CURR_CONFIG[key]['row'] = CONFIG[key]['row']
            CURR_CONFIG[key]['column'] = CONFIG[key]['column']

        # Preproces PDF
        fullPdf = preProcessPdf('../' + PDF_TYPE + '/' + file)
        # for line in fullPdf:
        #     print(line)
        # Extract data from PDF
        extractedData = extractData(fullPdf, CONFIG, CURR_CONFIG)

        # Save extracted result to file
        with open('../' + PDF_TYPE + '/' + file[:-3] + 'txt', 'w', encoding='utf8') as resultFile:
            for key in extractedData:
                resultFile.write("------------------------------------\n")
                resultFile.write("%s:\n%s\n" % (key, extractedData[key]))
                resultFile.write("------------------------------------\n")
