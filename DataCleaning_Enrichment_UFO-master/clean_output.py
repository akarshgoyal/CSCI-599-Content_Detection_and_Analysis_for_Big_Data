#Script for cleaning and extracting relevant features from the content from OCR
import os
import re
import nltk

print(os.getcwd())
count = 0

with open('output.csv', 'w+') as out:
    out.write('Date of Sighting,Date of Report,Location,Shape,Duration,Description\n')
for dir in os.listdir():
    if dir not in ['clean_output.py', 'output.csv', '.DS_Store', '.idea'] and os.path.isdir(dir):
        #print("hello1"+os.getcwd())
        os.chdir(dir)
        #print("hello2"+os.getcwd())
        os.chdir('outtxt')
        for x in os.listdir():
            print(x)
            if x not in ['clean_output.py', 'output.csv', '.DS_Store', '.idea'] and os.path.isfile(x):
                with open(x, 'r') as f:
                    # print(x)
                    with open('../../output.csv', 'a') as out:
                        DESC = ''
                        DATE = 'None'
                        LOCATION = 'None'
                        DURATION = 'None'
                        SHAPE = 'None'
                        for line in f.readlines():
                            line = line.strip().upper()
                            if line.strip() and re.search('([0-9]{2}) [a-zA-Z]{3} ([0-9]{2}|[0-9]{4})',
                                                          line):
                                count += 1
                                DATE = re.search('([0-9]{2}) [a-zA-Z]{3} ([0-9]{2}|[0-9]{4})', line).group(0)
                                print(DATE)
                            if line.strip() and re.search('[0-9]{2} MIN', line):
                                # count += 1
                                DURATION = re.search('[0-9]{2} MIN', line).group(0)
                                print(DURATION)
                            if line.strip() and re.search('[0-9]{2} SEC', line):
                                # count += 1
                                DURATION = re.search('[0-9]{2} SEC', line).group(0)
                                print(DURATION)
                            if line.strip() and len(re.search('.*', line).group(0)) > 10:
                                re.sub('[^a-zA-Z]+', '', line)
                                DESC = DESC + re.search('.*', line).group(0)
                            if line.strip() and re.search(r'\bBRIGHT\b', line):
                                SHAPE = re.search(r'\bBRIGHT\b', line).group(0)
                        print(DESC.replace(',', ''))
                        print(DURATION)
                        print(DATE)
                        # print("LOCATION   "+LOCATION)
                        print('shape' + SHAPE)
                        print()
                        if SHAPE == 'None':
                            tokens = nltk.word_tokenize(f.read().upper())
                            text = nltk.Text(tokens)
                            print('BRIGHT ==' + text.concordance('BRIGHT'))
                            print('SHAPE  ==' + text.concordance('SHAPE'))
                        if not DURATION == DATE == 'None':
                            out.write('{0},{0},{1},{2},{3},{4}\n'.format(DATE, LOCATION, SHAPE, DURATION,
                                                                         re.sub(r'\W+', ' ',
                                                                                DESC.replace(',', ''))))
        os.chdir('../..')
        # break
print(count)
