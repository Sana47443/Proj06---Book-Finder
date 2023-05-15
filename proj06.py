############################################################################################################################################################################
#  Computer Project #6
# 
#  Algorithm
#    importing all the required modules such as csv, string and itemgetter from operator module
#    writing a function definition defining open_file() which prompts the user for a valid file name and it doesn't leave until the user enters a valid one
#    writing a function definition defining read_file() which takes file pointer as the argument and reads through the file and returns a list of tuples contining book info
#    writing a function definition defining get_books_by_criterion() which takes 4 arguments and returns the filtered book collection filtered by one parameter
#    writing a function definition defining get_books_by_criteria() which takes 4 arguments and returns the filtered book collection filtered by multiple parameters
#    writing a function definition defining get_books_by_keyword() which takes 2 arguments and returns a filtered book collection filtered by the keywords
#    writing a function definition defining sort_authors() which takes 2 arguments(1 default)  and sorts the book collection by authors in ascending or descending order
#    writing a function definition defining recommend_books() which takes 6 arguments and recommends books after filtering out from all the filters and also the keywords
#    writing a function definition defining display_books() which has one argument and goes over the collection of books and displays them with formatting
#    writing a function definition defining get_option() whichdisplays the menu and prompts the user for an option
#    writing a function definition defining main() which calls all of the above defined functions according to the user's choice
#    calling the main function in a specific way
#
############################################################################################################################################################################

import csv, string                  #importing csv and string modules
from operator import itemgetter     #importing itemgetter from operator module

def open_file():
    """
    Prompts the user for file name and does not leave the user until the user 
    enters a valid file name
    
    Parameters
    ----------
    None

    Returns
    -------
    file_obj : File Pointer
               A file object which serves as the connection between the file 
               in the computer and the python shell on which code is written
    """
    file_name= input("Enter file name: ") #inputting file name from the user
    while True:   #a while loop looping till the user enters the one which exists
        try:            #which exists -- here try except
            file_obj= open(file_name,"r", encoding="utf-8")
            break
        except FileNotFoundError:   #This except will only catch FileNotFoundError
            print("\nError opening file. Please try again.") #this error will be displayed
            file_name= input("Enter file name: ") #for input of the filename
    return file_obj   #returning filepointer after all of this

def read_file(fp):    #function definition for read_file(fp) starts here
    """
    It takes in a file pointer and reads through the data in the file and 
    returns a list of tuples where each tuple contains the isbn13 value, title
    name, authors,categories, description, years, ratings, number of pages and 
    the ratings count
    
    Parameters
    ----------
    fp : File pointer
         A file object which serves as the connection between the file 
         in the computer and the python shell on which code is written

    Returns
    -------
    books_list : List
                 It is a list containing tuples which is formed by reading the
                 data from the file
    """
    fp.readline()                   #skips the header
    books_list=[]                   #assigning an empty list
    r=csv.reader(fp)                #Reader object
    for line in r:
        try:
            isbn13_val=line[0]     #assigning values to various variables in the order of desired parameters
            title_val=line[2]
            authors_names=line[4]
            categories_val= line[5].lower().split(",")  #lowering it and splitting it
            description_val = line[7]
            year_val= line[8]
            rating_val= float(line[9])    #doing type conversions for this value and the below values
            num_pages_val = int(line[10])
            r_count_val = int(line[11])
            book_tuple= (isbn13_val, title_val, authors_names, \
categories_val, description_val, year_val, rating_val, num_pages_val, \
r_count_val)
            books_list+=[book_tuple]    #adding tuples
        except ValueError:       #to catch error while type casting
            continue
    return books_list   #returns list of tuples

def get_books_by_criterion(list_tuples,criterion,value):
    """
    From the list of tuples passed as an argument, this filters out the books
    (tuples) according to the given criterion and it's corresponding value

    Parameters
    ----------
    list_tuples : List
                  List of tuples which contains the information of books
                  
    criterion : Integer
                It is the index value of the parameter corresponding to the 
                tuples
                
    value : String/Float/Integer
            It is the corresponding value as entered by the user and its 
            datatype depends upon the criterion

    Returns
    -------
    book_tup : Tuple
               Returned in the case where the criterion is the title
    or
    
    book_tup_list : List
                    Returned in all the other cases where the criterion is 
                    any other except for title
    """
    flag=0       #acts like a counter
    book_tup_list=[]                  #initializing lists
    if list_tuples==[]:              #if empty, it returns an empty list
        return []
    else:
        for book_tup in list_tuples:   #going through the list of tuples
            if criterion==1 and book_tup[criterion].lower() == value.lower():   #specifically for title criterion
                return book_tup          #in tuple form
            else:
                flag=1
                if type(value) == float :     #for ratings
                    if (book_tup[criterion]>= value) :  #for values greater than or equal to
                        book_tup_list.append(book_tup)
                elif type(value) == int :     #for page number
                    if book_tup[criterion]>= value-50 and \
book_tup[criterion]<=value+50:                #It is kind of like +- 50 range of the page number value
                        book_tup_list.append(book_tup)
                elif (value.lower() in book_tup[criterion])or \
(value.lower()==book_tup[criterion]) :
                    book_tup_list.append(book_tup)   #appending the tuple to the list
    
                    
        if flag==1:
            return book_tup_list  #only in the cases other than title
    
def get_books_by_criteria(list_tup,category,rating,page_no): #this function definition starts here
    '''
    From the list of tuples passed, this filters out books(tuples) by not just 
    1 parameter but 3 parameters one by one in this order - category, rating
    and page number and returns the filtered out  books

    Parameters
    ----------
    list_tup : List
               List of tuples as entered by the user
               
    category : String
               Category to be filtered as entered by the user
               
    rating : Float
             Rating to be filtered as entered by the user
    
    page_no : Integer
              Page number to be filtered as entered by the user
              
    Returns
    -------
    book_list_3 : List
                  List of tuples(books) after filtaration
    '''
    book_list_1= get_books_by_criterion(list_tup,3,category)   #filtering out first by category
    book_list_2= get_books_by_criterion(book_list_1,6,rating)  #then second by rating
    book_list_3= get_books_by_criterion(book_list_2,7,page_no) #then third by page number
    return book_list_3                  #returning the list

def get_books_by_keyword(list_tuple, keyword):  #function definition starts here for this function
    """
    From the list of tuples as passed by the user, this filters out the books
    having these keywords in its categories and returns all the books having
    the entered keywords in its description

    Parameters
    ----------
    list_tuple : List
                 List of tuples which contains the information of books
                 
    keyword : List
              It contains the words that we have to look for in the description
              of the books
              
    Returns
    -------
    books_list_tup : List
                     It is the filtered out collection of books

    """
    x_list= " ".join(keyword)     #converting to a string
    new_list= x_list.lower().split()   #lowering the case and then back to list
    books_list_tup=[]               #initializing empty list
    for list_tup_2 in list_tuple:   #going through the list of tuples
        list_words= list_tup_2[4].split()
        for j in list_words:
            if j.strip(string.punctuation).lower() in new_list:  #stripping punctuations 
                books_list_tup.append(list_tup_2) #and lowering the case and then checking
                break
    return books_list_tup      #returns the list of tuples after filtering by keyword

def sort_authors(list_tuple,a_z=True):  #function definition starts here and a default parameter here for a_z(True)
    '''
    This function sorts a list of tuples and returns the list of tuples in 
    ascending or descending order as per the user

    Parameters
    ----------
    list_tuple : List
                 List of tuples which contains the information of books
                 
    a_z : Boolean, optional
          Boolean value for ascending or descending order. The default is True.

    Returns
    -------
    sorted_list : List
                  It is the sorted list in ascending or descending order

    '''
    sort_list= list(list_tuple)    #making a deep copy so that changes are not reflected in the original list
    sorted_list= sorted(sort_list, key=itemgetter(2), reverse=not a_z) #sorting
    return sorted_list          #returning the sorted list

def recommend_books(list_tuple, keywords, category, rating, page_number, a_z):#function definition starts
    """
    From the list of tuples and also from the other parameters, it filters
    out books(tuples) and returns them(also sorted)

    Parameters
    ----------
    list_tuple : List
                 List of tuples which contains the information of books
    
    keywords : List
               List of keywords
               
    category : String
               Category to be filtered out          
    
    rating : Float
             Rating to be filtered out
    
    page_number : Integer
                  Page number to be filtered out
                  
    a_z : Boolean
          Boolean value for ascending or descending order sorting

    Returns
    -------
    sort_auth_list : List
                     List of sorted tuples

    """
    recommend_book= []                   #initializing list
    for list_book in list_tuple:     #going through list of tuples
        flag=0
        x_list= list_book[4].split()  #from string to list by space splitting
        for i in range(len(x_list)):
            x_list[i]= x_list[i].strip(string.punctuation).lower() #converting all the words to lower case and stripping punc
        if (category in list_book[3]) and (list_book[6]>= rating) and \
(list_book[7]>=page_number-50 and list_book[7]<= page_number +50): #if condition as desired
            for val in keywords:         #going through the list of keywords
                for val2 in x_list:     #going through list of words
                    if val in val2:    #for special cases where splitting doesn't do a good job, this works
                        flag=1         #in order to avoid redundancy, this counter
                        break
        if flag==1:
            recommend_book.append(list_book)   #adding it to the list
    sort_auth_list= sorted(recommend_book,key=itemgetter(2),reverse= not a_z) #sorting done
    return sort_auth_list   #returning sorted list

def display_books(list_of_tuples):  #function definition for display_books() starts here
    """
    It displays books(tuples) in a nice format.

    Parameters
    ----------
    list_of_tuples : List
                     List of tuples which contains the information of books

    Returns
    -------
    None.

    """
    if list_of_tuples==[]:       #for the cases where the list of tuples is an empty list
        print("Nothing to print.")  #print this
    else:
        for book_info in list_of_tuples:
            if len(book_info[1])>35 or len(book_info[2])>35:  #another if condition for the number of characters checking
                continue
            else:
                print("{:15s} {:35s} {:35s} {:6s} {:<8.2f} {:<15d} \
{:<15d}".format(book_info[0],book_info[1],book_info[2],book_info[5],\
book_info[6],book_info[7],book_info[8]))   #the formatting for display
                

def get_option():   #function definition starts here for get_option()
    """
    Displays menu and prompts user for an input
    Displays error message if the input is invalid

    Returns
    -------
    choice_input : Integer
                   User's choice of option
    or 
    
    None : For invalid options
    
    """
    MENU = "\nWelcome to the Book Recommendation Engine\n\
        Choose one of below options:\n\
        1. Find a book with a title\n\
        2. Filter books by a certain criteria\n\
        3. Recommend a book \n\
        4. Quit the program\n\
        Enter option: "                      #the menu
    choice_input= input(MENU)             #user input for choice
    if int(choice_input)>=1 and int(choice_input)<=4:  #if condition so as it to be between 1 and 4
        return int(choice_input)   #return the choice
    else:
        print("\nInvalid option")  #else invalid option
        return None
        
def main():    #main function starts here
    """
    This is the main function which displays the various menu options and 
    performs the activities(calling the above written functions accordingly)
    which the user asks for and loops until the user wants to break.
    
    Parameters
    ----------
    None.

    Returns
    -------
    None.

    """
    CRITERIA_INPUT = "\nChoose the following criteria\n\
                 (3) Category\n\
                 (5) Year Published\n\
                 (6) Average Rating (or higher) \n\
                 (7) Page Number (within 50 pages) \n\
                 Enter criteria number: "    #the criteria input statements stored in a variable
    
    file_pointer= open_file()    #calling open_file()
    book_list_data= read_file(file_pointer)    #calling read_file()
    user_choice= get_option()      #for user input options caling get_option()
    while True:            #while the user does not enter 4
        if user_choice== None:    #invalid option case
            while user_choice==None:
                user_choice= get_option()
        elif user_choice==4:      #quitting option
            break
        elif user_choice==1:      #option 1
            book_title= input("\nInput a book title: ")   #getting book title
            matching_books= get_books_by_criterion(book_list_data,1,book_title) #calling appropriate function
            matching_books= [matching_books]     #so that display dunction can work on it
            print("\nBook Details:")
            print("{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} \
{:15s}".format("ISBN-13","Title","Authors","Year","Rating","Number Pages",\
"Number Ratings"))               #the header
            display_books(matching_books)   #for displaying
            user_choice= get_option()
        elif user_choice==2:     #option 2
            user_criterion=input(CRITERIA_INPUT)   #user input for criterion
            if user_criterion not in ["3","5","6","7"]:   #error checking
                while user_criterion not in ["3","5","6","7"]:
                    print("\nInvalid input")     #loop until valid one
                    user_criterion= input(CRITERIA_INPUT)
            criterion_value= input("\nEnter value: ")
            
            if user_criterion == "6":    #error checking for rating under this
                flag=0
                while flag==0:
                    try:
                        criterion_value = float(criterion_value)
                        flag=1
                    except ValueError:
                        print("\nInvalid input")
                        criterion_value= input("\nEnter value: ")
            elif user_criterion=="7":    #error checking for page number under this
                flag=0
                while flag==0:
                    try:
                        criterion_value= int(criterion_value)
                        flag=1
                    except ValueError:
                        print("\nInvalid input")
                        criterion_value= input("\nEnter value: ")
            book_filtered= get_books_by_criterion(book_list_data, \
int(user_criterion), criterion_value)    #calling the appropriate function
            filtered_sorted_books= sort_authors(book_filtered, True) #calling the appropriate function
            books_to_display= filtered_sorted_books[:30] #first 30 tuples
            print("\nBook Details:") 
            if books_to_display!=[]:          #display only when it's not an empty list
                print("{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} \
{:15s}".format("ISBN-13","Title","Authors","Year","Rating","Number Pages",\
"Number Ratings")) 
                      
            display_books(books_to_display) #calling the appropriate function
            user_choice= get_option()    #calling the appropriate function
        elif user_choice==3:
            desired_category= input("\nEnter the desired category: ")  #user input
            desired_rating= input("\nEnter the desired rating: ")   #user input
            while True:         #error checking for rating
                try:
                    desired_rating= float(desired_rating)
                    break
                except ValueError:
                    print("\nInvalid input")
                    desired_rating= input("\nEnter the desired rating: ")
            desired_pagenum=input("\nEnter the desired page number: ")
            while True:         #error checking for page number
                try:
                    desired_pagenum= int(desired_pagenum)
                    break
                except ValueError:
                    print("\nInvalid input")
                    desired_pagenum=input("\nEnter the desired page number: ")
            val_a_z= int(input("\nEnter 1 for A-Z sorting, and \
2 for Z-A sorting: "))
            if val_a_z==1:        #for assigning the write values for a_z
                val_a_z= True
            else:
                val_a_z= False
            user_keywords=input("\nEnter keywords (space separated): ") #keywords input
            user_keywords_list= user_keywords.split()    #making it into a list
            recommend_sorted_books= recommend_books(book_list_data,\
user_keywords_list,desired_category,desired_rating,desired_pagenum,val_a_z)  #calling the appropriate function
            print("\nBook Details:")
            print("{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}".format(\
"ISBN-13","Title","Authors","Year","Rating","Number Pages","Number Ratings"))            
            display_books(recommend_sorted_books)     #calling the appropriate function
            user_choice= get_option()    #calling the appropriate function
    

if __name__ == "__main__": #special condition for this main
    main()

