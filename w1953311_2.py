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
     option = int(input("Enter 1 or 2 : "))
     if (option == 1 or option == 2 ) :
         break
    except ValueError:
        print("Integer required")


progress=0
trailer=0
retriever=0
exclude=0

progress_list=[]
trailer_list=[]
retriever_list=[]
exclude_list=[]

                               
while True:
       
    #pass_credit input
    pass_credit = get_valid_input("pass" )
            
    #defer_credit input
    defer_credit = get_valid_input("defer" )
            
    #fail_credit_input
    fail_credit = get_valid_input("fail" )

    if pass_credit+ defer_credit+ fail_credit != 120:
        print("Total Incorrect")
       
      
              
    if pass_credit==120 and defer_credit==0 and fail_credit==0:
        print("Progress")
        progress+=1
        progress_list.append([pass_credit, defer_credit, fail_credit])
        
            
        
    elif pass_credit==100:
        print("progress(module trailer)")
        trailer+=1
        trailer_list.append([pass_credit, defer_credit, fail_credit])
        
            
    elif pass_credit>=0 and fail_credit<=60:
        print("Do not progress- module retriver")
        retriever+=1
        retriever_list.append([pass_credit, defer_credit, fail_credit])
        
           
        
    else:
        print("Exclude")
        exclude+=1
        exclude_list.append([pass_credit, defer_credit, fail_credit])

    if option == 1:
        break
    else:

        print("Would you like to enter another set of data?")
        result = ""
        #get valid yes(y/Y) or quit(q/Q) response from user            
        while True:
            result=input("Enter 'y' for yes or 'q' to quit and view results : ")
            if result == "y" or result == "Y" or result == "q" or result == "Q":
                break

        if result == "y" or result == "Y":
            continue
        elif result == "q" or result == "Q" :
            print("--------------------------------------------------------------------------------------------")

            print("Histogram")
            print("Progress" , progress, ":",'*'*progress)
            print("Trailer", trailer,    ":", '*'*trailer)
            print("Retriever", retriever,":", '*'*retriever)
            print("Exclude",exclude, ":" , '*'*exclude)
            print(progress +  trailer + retriever + exclude, "outcomes in total")

            print("-------------------------------------------------------------------------------------------------")

            for x in progress_list:
                print("Progress - ",x[0], ", ", x[1], ", ", x[2])
            for x in trailer_list:
                print("Trailer - ",x[0], ", ", x[1], ", ", x[2])
            for x in retriever_list:
                print("Retriever - ",x[0], ", ", x[1], ", ", x[2])
            for x in exclude_list:
                print("Exclude - ",x[0], ", ", x[1], ", ", x[2])
            
            break
        
        
      
