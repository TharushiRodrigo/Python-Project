# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1953311
 
# Date: 14/12/2022

#get valid input from user
def get_valid_input(credit_name):
    marks = [0,20,40,60,80,100,120]
    while True:
        try:
            credit=int(input("Please enter your credits at " + credit_name+ ": "))
            if credit in marks:
                return credit
            else:
                print("Out of range")
           
        except ValueError:
            print("Integer required")


option = 0
print("If you want to continue as student enter 1 or else want to continue as staff member enter 2")
while True:
    try :
     option=int(input("Enter 1 or 2 : "))
     if (option == 1 or option == 2 ) :
         break
    except ValueError:
        print("Integer required")

progress=0
trailer=0
retriever=0
exclude=0

student_progress_file = open("studentProgressFile.txt", "w")
#https://stackoverflow.com/questions/2769061/how-to-erase-the-file-contents-of-text-file-in-python
#remove file contents before starting new program
student_progress_file.seek(0) # set position of the file to begining
student_progress_file.truncate()  # delete previous content
                  
while True:
       
    #pass_credit input
    pass_credit = get_valid_input("pass" )
            
    #defer_credit input
    defer_credit = get_valid_input("defer" )
            
    #fail_credit_input
    fail_credit = get_valid_input("fail" )

    if pass_credit+ defer_credit+ fail_credit != 120:
        print("Total Incorrect")
        continue

    stringPassCredit = str(pass_credit)
    stringDeferCredit = str(defer_credit)
    stringFailCredit = str(fail_credit)
              
    if pass_credit==120 and defer_credit==0 and fail_credit==0:
        print("Progress")
        progress+=1
        student_progress_file.write("Progress - " + stringPassCredit + "," + stringDeferCredit + "," + stringFailCredit + "\n")
    elif pass_credit==100:
        print("progress(module trailer)")
        trailer+=1
        student_progress_file.write("Progress (module trailer) - " + stringPassCredit + "," + stringDeferCredit + "," + stringFailCredit + "\n")
    elif pass_credit>=0 and fail_credit<=60:
        print("Do not prgress- module retriver")
        retriever+=1
        student_progress_file.write("Module retriever - " + stringPassCredit + "," + stringDeferCredit + "," + stringFailCredit + "\n")
    else:
        print("Exclude")
        exclude+=1
        student_progress_file.write("Exclude - " + stringPassCredit + "," + stringDeferCredit + "," + stringFailCredit + "\n")

    if option == 1:
        break
    else:
        #get valid yes(y/Y) or quit(q/Q) response from user            
        while True:
         result=input("Enter 'y' for yes or 'q' to quit and view results : ")
         if result == "y" or result == "Y" or result == "q" or result == "Q":
             break
            
        if result == "y" or result == "Y":
            continue
        elif result == "q" or result == "Q" :
            print("---------------------------------------------------------------")

            print("Histogram")
            print("Progress" , progress, ":", '*' * progress)
            print("Trailer", trailer,    ":", '*' * trailer)
            print("Retriever", retriever,":", '*' * retriever)
            print("Exclude",exclude, ":" , '*' * exclude)
            print(progress +  trailer + retriever + exclude, "outcomes in total", "\n")
            print("Part 3:")
            student_progress_file = open("studentProgressFile.txt", "r")
            for result in student_progress_file:
                print(result)
            student_progress_file.close()    
            break
    
