import os
def Add_Details():
    entry=[]
    name=input('please enter the name: ')
    ph_no=input('please enter phone number: ')
    entry.append(name)
    entry.append(ph_no)
    return entry
def bub_sort(dirList):
    length=len(dirList)-1
    unsorted=True
    while unsorted:
        unsorted=False
        for element in range(0,length):
            if dirList[element]>dirList[element+1]:
                temp=dirList[element+1]
                dirList[element+1]=dirList[element]
                dirList[element]=temp
                unsorted=True
def Save_Data_to_File(dirlist):
    f=open('Phone Book Directory.txt','w')

    for n in dirlist:
        f.write(n[0])
        f.write(',')
        f.write(n[1])
        f.write('\n')
    f.close()
def Display():
    if(os.path.isfile('Phone_Book_Directory.txt')==0):
        print('Sorry you have any Contacts in your Phone Address Book.')
        print('Please Create it!!!')
    elif(os.stat('Phone Book Directory.txt').st_size==0):
        print('Address Book is empty')
    else:
        f=open('Phone Book Directory.txt','r')
        text=f.read()
        print(text)
        f.close()
def Search():
    name=input('Enter the name: ')
    f=open('Phone Book Directory.txt','r')
    result=[]
    for line in f:
        if name in line:
            found=True
            break
        else:
            found=False
    if(found==True):
        print('The Name of Person Exist in Directory: ')
        print(line.replace(', ', ':'))
    else:
        print('The Name does not Exist in Directory')
def Get_Choice():
    print('1:\tAdd New Phone Number to a list of Phone Book Directory: ')
    print('2:\tSorts name in ascending order')
    print('3:\tSave all Phone numbers to a file')
    print('4:\tPrint all Phone book in a Directory on a Console')
    print('5:\tSearch Phone Number from Phone Directory: ')
    print('6:\tPlease Write 6 to exit from the menu: ')
    ch=input('Please Enter the Choice: ')
    return ch
if(os.path.isfile('Phone Book Directory.txt')==0):
    print('Sorry you dont have any contact in your Phone Address Book.')
    print('Please Create it!!!')
    directory=[]
else:
    print('Already Your Phone Book has Some Contact')
    print('You can see it')
    directory=[]
    f=open('Phone Book Directory.txt')
    for line in f:
        if line.endswith('\n'):
            line=line[:-1]
            directory.append(line.strip().split(','))
    f.close()
c=True
while  c:
    ch=Get_Choice()
    if ch=='1':
        # e=Add_Details()
        directory.append(Add_Details())
    if ch=='2':
        bub_sort(directory)
        print('Contents of Phone Book Sorted Successfully!!!')
    if ch=='3':
        Save_Data_to_File(directory)
        print('Data Saved to Phone Book Successfully!!!')
    if ch=='4':
        Display()
    if ch=='5':
        Search()
    if ch=='6':
        print('Thanks a Lot for using Our Application')
        c=False