#ProcessData.py
#Name: Alyssia Norton
#Date: 11-2-25
#Assignment: Lab 8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    year = data[5]
    major = data[6]

    student_id = makeID(first, last, idNum)
    major_year = makeMajorYear(major, year)
    output = last + "," + first + "," + student_id + "," + major_year + "\n"
    outFile.write(output)

  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  print(first, last, idNum)
  idLen = len(idNum)
  while len(last) < 5:
    last = last + "X"
  id = first[0] + last + idNum[idLen - 3: ]  

  return id


def makeMajorYear(major, year):
  major_code = major[:3].upper()
  year_map = {
    "Freshman": "FR",
    "Sophomore": "SO",
    "Junior": "JR",
    "Senior": "SR"
  }

  year_code = year_map.get(year.strip(), "??")
  return major_code + "-" + year_code


if __name__ == '__main__':
  main()
