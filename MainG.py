
import os
import csv
import random

class Questions:
    #create a new question

    def NewQues(self):
        q = input("Your Question: ")
        num_opt = int(input("Number of options: "))
        x = 0
        opts = []
        while x<num_opt:
            print("option {}:".format(x+1), end = " ")
            inp = input()
            opts.append(inp)
            #print(x)
            x = x+1
        correct = int(input("Enter the correct option number: "))
        cor_opt = opts[correct-1]
        print("The correct answer is option {}: '{}'".format(correct, cor_opt))
        return q, opts, correct, cor_opt
    
    #convert the question created into a dictionary, returns a dictionary and a list
    def QuesObject(self):
        q, opts, correct, cor_opt = self.NewQues()
        Qobj_dict = {
            "Question" : q,
            "Options" : opts,
            "Answer_Index" : correct, #made a mistake, too lazt to correct. Its not answer index its answer number.
            "Answer" : cor_opt
        }
        fields = ["Question", "Options", "Answer_Index", "Answer" ]
        return Qobj_dict, fields
    
#Add a new entry into the csv file
def WriteCsv():
    q1 = Questions()
    Qobj_dict, fields = q1.QuesObject()
    #if csv file exists, add new entry, otherwise, create and define headers for new csv file
    if os.path.exists("Data.csv"):
        csvf = open("Data.csv", 'a')
        csvwriter = csv.DictWriter(csvf, fieldnames = fields)
        csvwriter.writerow(Qobj_dict)
        csvf.close()
    else:
        csvf = open("Data.csv", "x")
        csvwriter = csv.DictWriter(csvf, fieldnames = fields)
        csvwriter.writeheader()
        csvwriter.writerow(Qobj_dict)
        csvf.close()
    
#Read the entries of the csv file and store it in a list
def Readcsv():
    if not os.path.exists("Data.csv"):
        print("The question database is empty, please add new questions before trying to play :)")
    else:
        csvf = open("Data.csv", "r")
        csvreader = csv.DictReader(csvf)
        All_data = [row for row in csvreader] 
    return All_data

#Add multiple Questions into the database
def AddQues():
    x = 0
    n = int(input("Enter the number of questions you want to add into the database: "))
    while x<n:
        WriteCsv()
        x = x+1

#Adding a randomizer and a question picker (how many questions our quiz instance should have)
def RandNQues():
    All_Ques = Readcsv()
    n = int(input("How many Questions does your quiz Have? "))
    if n>len(All_Ques):
        print("Database currently only has {} questions available. You can attempt them all or add new.".format(len(All_Ques)))
        n = len(All_Ques)
    Qlist = random.sample(All_Ques, n)
    return Qlist


#Display the Questions and keep count of right and wrong answers
def mainQuiz():
    Qlist = RandNQues()
    score = 0
    for q in Qlist:
        print("Question: {}".format(q["Question"]))
        #q["Question"] returns a string that looks like a list of chars. Direct unpacking into list impossible
        #the line below is the workaround I found afterhours of debugging QwQ. Yes, I'm a noob
        options = list(q["Options"].replace("'", "").strip('][').split(', ')) 

        print("Options: ")
        for x in range(len(options)):
            print("{}. {}".format(x+1, options[x]))
        choice = int(input("Enter the option number of your choice: "))
        #print(type(q["Answer_Index"]))
        if  choice == int(q["Answer_Index"]):
            score = score + 1
            print("Your Answer is correct!")
        else:
            print("Wrong Answer! Boooo :(")
    
    print("The test is over, you scored a total of {} points.".format(score))

def main():
    print("Welcome, Player! This is a barebones quiz application!")
    go = True
    while go == True:
        print("Select a Choice: ")
        print("     1. Add Question")
        print("     2. Attempt Quiz")
        print("     3. Exit")
        choice = int(input("Your choice: "))
        if(choice == 1):
            AddQues()
        elif(choice == 2):
            mainQuiz()
        elif(choice == 3):
            print("Exiting.")
            go = False


if __name__ == "__main__":
    main()
        