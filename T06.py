import csv

def write_into_csv(info_list):
    with open('student_info.csv','w+',newline='') as csv_files:
        writer=csv.writer(csv_files)
        
        if csv_files.tell()==0:
            writer.writerow(['Name','Age','Contact_number','E-mail_ID'])
        
        writer.writerow(info_list)
if __name__=='__main__':
    condition=True
    student_num=1
    
    while(condition):
     student_info=input('Enter student information for student #{} in the following format(Name Age Contact_Number E-mail_ID): '.format(student_num))
    
    
    #split
     student_info_list=student_info.split(' ')
    
   
     print('\nThe entererd information is -\nName: {}\nAge: {}\nContact_number: {}\nE-mail_ID: {}'
          .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3])  )
    
     choice_check=input('Is the entered information correct(yes/no)?: ')
    
     if choice_check=='yes':
         write_into_csv(student_info_list)
         
         condition_check=input('enter (yes/no) if you want to enter information for another student:')
         if condition_check=='yes':
             condition=True
             student_num=student_num+1
         elif condition_check=='no':
             condition=False
     elif  choice_check=='no':
         print('\nPlease re-enter the values!')
        
    
    
    
    
    