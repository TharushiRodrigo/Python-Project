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


progress_dict={}
           
while True:
    student_id = input("Enter student id : ")
       
    #pass_credit input
    pass_credit = get_valid_input("pass" )
            
    #defer_credit input
    defer_credit = get_valid_input("defer" )
            
    #fail_credit_input
    fail_credit = get_valid_input("fail" )

    if pass_credit+ defer_credit+ fail_credit != 120:
        print("Total Incorrect")          
      
    
              
    if pass_credit==120 and defer_credit==0 and fail_credit==0:
        progress_dict[student_id]= ["Progress", pass_credit, defer_credit, fail_credit]    
        
    elif pass_credit==100:
        progress_dict[student_id]= ["Progress (module trailer)", pass_credit, defer_credit, fail_credit]
            
    elif pass_credit>=0 and fail_credit<=60:
        progress_dict[student_id]= ["Module retriever", pass_credit, defer_credit, fail_credit]    
        
    else:
        progress_dict[student_id]= ["Progress (module trailer)", pass_credit, defer_credit, fail_credit]


    print("Would you like to enter another set of data?")
    result=input("Enter 'y' for yes or 'q' to quit and view results : ")
    if result == "y":
        continue
    else:
        print("Part 4:", "\n")

        for student in progress_dict:
            print (student, " : ", progress_dict[student][0], " - ",  progress_dict[student][1], ", ",  progress_dict[student][2], ", ",  progress_dict[student][3], "\n")
        
        break
    

