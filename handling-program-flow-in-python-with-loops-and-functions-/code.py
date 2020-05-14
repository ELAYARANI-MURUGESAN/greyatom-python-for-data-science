# --------------
#Code starts here

#Function to read file
def read_file(file_path):
    with open (file_path,'r') as file:
        file_contents=file.readline()
        sentence=file_contents
        file.close()
    return sentence
sample_message=read_file(file_path)
print(sample_message)
    #Opening of the file located in the path in 'read' mode
    
    #Reading of the first line of the file and storing it in a variable
    
    #Closing of the file
    
    #Returning the first line of the file
    
    

#Calling the function to read file

#Printing the line of the file
message_1=read_file(file_path_1)
message_2=read_file(file_path_2)
print(message_1)
print(message_2)

#Function to fuse message
def fuse_msg(message_1,message_2):
    message_1=int(message_1)
    message_2=int(message_2)
    quotient=round(message_1/message_2)
    return quotient
secret_msg_1=fuse_msg(message_1,message_2)
print(secret_msg_1)
 #Integer division of two numbers
        #Returning the quotient in string format
#Calling the function to read file  

#Calling the function to read file


#Calling the function 'fuse_msg'


#Printing the secret message 



#Function to substitute the message

message_3=read_file(file_path_3)
print(message_3)
message_c=message_3
def substitute_msg(message_c):
    #If-else to compare the contents of the file
    if (message_c==message_3):
         substitute_msg='Data Scientist'
    elif(message_c==Red):
        substitute_msg='Army General'
    else:
        substitute_msg='Marine Biologist'
    sub=substitute_msg
    return sub
secret_msg_2=substitute_msg(message_3)
print(secret_msg_2)



    
   
    
    
    #Returning the substitute of the message
    
    

#Calling the function to read file


#Calling the function 'substitute_msg'


#Printing the secret message



#Function to compare message
message_4=read_file(file_path_4)
message_5=read_file(file_path_5)
print(message_4)
print(message_5)


    
    #Splitting the message into a list
def compare_msg(message_4,message_5):
    a_list=message_4.split()
    b_list=message_5.split()
    c_list=[i for i in a_list if i not in b_list]
    print(c_list)
    final_msg=" ".join(c_list)
    print('final_msg=',final_msg)
    return final_msg
secret_msg_3=compare_msg(message_4,message_5)
print(secret_msg_3)
    #Splitting the message into a list
    
    
    #Comparing the elements from both the lists
    
    
    #Combining the words of a list back to a single string sentence
    

    #Returning the sentence
    
#secret_msg_3=compare_msg(message_4,message_5)
#print(secret_msg_3)
#Calling the function to read file


#Calling the function to read file


#Calling the function 'compare messages'


#Printing the secret message


#Function to filter message
message_6=read_file(file_path_6)
print(message_6)
def extract_msg(message_6):
    a_list=message_6.split()
    print(a_list)
    def even_word (x):
        return len(x)%2==0
    b_list=list(filter(even_word,(a_list)))
    print(b_list)
    final_msg=" ".join(b_list)
    print('final_msg=',final_msg)
    return final_msg
secret_msg_4=extract_msg(message_6)
print(secret_msg_4)

    
    #Splitting the message into a list

    
    #Creating the lambda function to identify even length words
    
    
    #Splitting the message into a list
    
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    
    
#Calling the function to read file


#Calling the function 'filter_msg'


#Printing the secret message


#Secret message parts in the correct order
secret_msg_1=str(secret_msg_1)
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]

print(message_parts)


#define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message
secret_msg=" ".join(message_parts)
print('secret_msg=',secret_msg)


#Function to write inside a file
def write_file(secret_msg,final_path):
    file_path=write_file(secret_msg,'a+')
    file_path.close()
    write_file(secret_msg,file_path)
final_path= user_data_dir + '/secret_message.txt'
print(secret_msg)
      #Opening a file named 'secret_message' in 'write' mode
   

      

#Writing to the file
     

    #Closing the file

#Calling the function to write inside the file  
#Printing the entire secret message


#Code ends here


