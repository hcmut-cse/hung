from difflib import SequenceMatcher

def removeHeaderAndFooter(pdf):

    fullPdf = []
    for i in range(len(pdf)):
        if (pdf[i].strip() != ''):
            fullPdf.append(pdf[i].split('\n'))
    if (len(fullPdf) == 1):
        return fullPdf
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
    return fullPdf
