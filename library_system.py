import mysql.connector as sqltor
def addCust():
    while True:
        mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
        cur= mycon.cursor()
        phNo = int(input('Enter customer phone number: '))
        qry = 'select c_phone from customer'
        cur.execute(qry)
        data = cur.fetchall()
        if (phNo,) not in data:
            C_Name = input('Enter customer name: ')
            caddr = input('Enter customer address: ')
            cemail= input('Enter customer email: ')
            qry = 'insert into customer (c_name, c_phone, c_addr,c_email) values ( "{}","{}","{}","{}" )'.format(C_Name,phNo,caddr,cemail)
            cur.execute(qry)
            mycon.commit()
            print('\nCustomer added successfully')
            print('Returning back to MAIN MENU...')
            break
        else:
            print('\nCustomer phone number ',phNo, 'already exist')
            print('Enter 1 to try again')
            print('Enter 2 to return back to main menu')
            choice = int(input('Enter your choice(1/2): '))
            if choice == 1:
                continue
            else:
                print('Returning back to MAIN MENU...')
                break
        mycon.close()
   
def updateCustomerPhoneNumber():
    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
    cur= mycon.cursor()
    while True:
        print("**************************************")
        print("1. Update Customer's phone number ")
        print("2. Update Customer's address ")
        print("3. Update both phone number and address")
        print("4. Back to Main Menu")
        print("**************************************")
        menuChoice = int(input('Enter your choice(1-4): '))
        cnum = int(input('Enter customer\'s phone number: '))
        if menuChoice == 1:
            phone_new = int(input('Enter Customers new phone number: '))
            update_qry = 'update customer set c_phone = "{}" where c_phone = "{}"'.format(phone_new, cnum)
        elif menuChoice == 2:
            addr = input('Enter new address : ')
            update_qry = 'update customer set c_addr = "{}" where c_phone = "{}"'.format(addr, cnum)
            print(update_qry)
        elif menuChoice == 3:
            addr = input('Enter new address : ')
            phone_new = int(input('Enter Customer\s new phone number: '))
            update_qry = 'update customer set c_phone = "{}"", c_addr = "{}" where c_phone = "{}"'.format(phone_new,addr, cnum)
        else :
            break
        qry = 'select c_phone from customer'
        cur.execute(qry)
        data = cur.fetchall()
        for i in data:
            if (cnum,) in data:
                cur.execute(update_qry)
                mycon.commit()
                print('\n Updated successfully!')
                print('Returning back to MAIN MENU...')
                break
            else:
                print('\nCustomer not found')
                print('Enter 1 to try again')
                print('Enter 2 to return back to menu')
                choice = int(input('Enter your choice(1/2): '))
                if choice == 1:
                    continue
                else:
                    print('Returning back to MAIN MENU...')
                    break
    mycon.close()
   
def removeCust():
    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
    cur= mycon.cursor()
    while True:
        custid = int(input('Enter customer ID number: '))
        qry = 'select cust_id from customer'
        cur.execute(qry)
        data = cur.fetchall()
        if (custid,) in data:
            choice = input('Confirm deletion(yes/no): ')
            if choice.lower() == 'yes':
                qry = 'delete from customer where cust_id = {}'.format(custid)
                cur.execute(qry)
                mycon.commit()
                print('\nCustomer deleted successfully!')
                print('Returning back to MENU...')
                break
            else:
                print('Terminating the delete process...')
                print('Returning back to MENU...')
                break
        else:
            print('\nCustomer not found')
            print('Enter 1 to try again')
            print('Enter 2 to return back to menu')
            choice = int(input('Enter your choice(1/2): '))
            if choice == 1:
                continue
            else:
                print('Returning back to MAIN MENU...')
                break
    mycon.close()
 
def viewAllCust():
    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
    cur= mycon.cursor()
    print(' Customers ')
    print('+-------------------------------------------------------------------------------------+')
    print('| cust_id | c_name | c_addr | c_phone | c_email |')
    print('|----------|--------------------|--------------------------------|-------------|--------------|')
    qry = 'select * from customer'
    cur.execute(qry)
    data = cur.fetchall()
    for row in data:
        print('|%-10s|%-15s|%-25s|%-15s|%-15s|'%(row[0],row[1], row[2],row[3], row[4]))
        print('+-------------------------------------------------------------------------------------+')
    print('\nReturning back to MENU...')
    mycon.close()
 
def addEmployee():
    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
    cur= mycon.cursor()
    while True:
        phone = int(input('Please enter phone number: '))
        qry = 'select e_phone from employee'
        cur.execute(qry)
        data = cur.fetchall()
        if (phone,) not in data:
            name = input('Please Enter name: ')
            addr = input('Please Enter address: ')
            email= input('Plese Enter email: ')
            salary= float(input('Plese Enter salary: '))
            joindate= input('Plese Enter joining date [dd/mm/yyyy]: ')
            qry = 'insert into employee (e_name, e_phone, e_addr,e_email,e_salary, join_date) values ("{}","{}", "{}","{}", "{}","{}")'.format(name,phone,addr,email,salary,joindate)
            cur.execute(qry)
            mycon.commit()
            print('\nEmployee added successfully')
            print('Returning back to MENU...')
            break
        else:
            print('\nEmployee phone number \'',phone,'\' already exist')
            print('Enter \'1\' to try again')
            print('Enter \'2\' to return back to menu')
            choice = int(input('Enter your choice(1/2): '))
            if choice == 1:
                continue
            else:
                print('Returning back to MENU...')
                break
    mycon.close()
 
 
def updateEmployeeDetails():
    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
    cur= mycon.cursor()
    while True:
        print("**************************************")
        print("1. Update Employee Phone number ")
        print("2. Update Employee Address ")
        print("3. Update both Phone number and Address")
        print("4. Back to Main Menu")
        print("**************************************")
        menuChoice = int(input('Enter your choice(1-4): '))
        phone = int(input('Enter Employee\'s phone number: '))
        if menuChoice == 1:
            phone_new = int(input('Enter Employee\s new phone number: '))
            update_qry = 'update employee set e_phone = {} where e_phone = {}'.format(phone_new, phone)
        elif menuChoice == 2:
            addr = input('Enter new address : ')
            update_qry = 'update employee set e_addr = "{}" where e_phone = {}'.format(addr, phone)
            print(update_qry)
        elif menuChoice == 3:
            addr = input('Enter new address : ')
            phone_new = int(input('Enter Employee\s new phone number: '))
            update_qry = 'update employee set e_phone = {}, e_addr = "{}" where e_phone = {}'.format(phone_new,addr, phone)
        else :
            break
        qry = 'select e_phone from Employee'
        cur.execute(qry)
        data = cur.fetchall()
        if (phone,) in data:
            cur.execute(update_qry)
            mycon.commit()
            print('\n Updated successfully!')
            print('Returning back to MENU...')
            break
        else:
            print('\nEmployee record not found')
            print('Enter \'1\' to try again')
            print('Enter \'2\' to return back to menu')
            choice = int(input('Enter your choice(1/2): '))
            if choice == 1:
                continue
            else:
                print('Returning back to MENU...')
                break
    mycon.close()
 
def deleteEmployeeDetails():
    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
    cur= mycon.cursor()
    while True:
        empid = int(input('Enter employee ID number: '))
        qry = 'select emp_id from employee'
        cur.execute(qry)
        data = cur.fetchall()
        if (empid,) in data:
            choice = input('Confirm deletion(yes/no): ')
            if choice.lower() == 'yes':
                qry = 'delete from employee where emp_id = {}'.format(empid)
                cur.execute(qry)
                mycon.commit()
                print('\nemployee deleted successfully!')
                print('Returning back to MENU...')
                break
            else:
                print('Terminating the delete process...')
                print('Returning back to MENU...')
                break
        else:
            print('\nemployee not found')
            print('Enter \'1\' to try again')
            print('Enter \'2\' to return back to menu')
            choice = int(input('Enter your choice(1/2): '))
            if choice == 1:
                continue
            else:
                print('Returning back to MENU...')
                break
    mycon.close()
 
def viewAllEmployees():
    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
    cur= mycon.cursor()
    print(' List of Employees ')
    qry = 'select * from employee'
    cur.execute(qry)
    data = cur.fetchall()
    print('+----------------------------------------------------------------------------------------------------+')
    print('| emp_id | name | address | phone | email |salary | join_date |')
    print('|----------|---------------|------------------|-------------|----------|--------|------------|')
    for row in data:
        print('|%-7s|%-12s|%-15s|%-10s|%-15s|%-15s|%-10s|'%(row[0],row[1], row[2],row[3], row[4], row[5],row[6]))
        print('+---------------------------------------------------------------------------------------------------+')
    print('\nReturning back to MENU...')
    mycon.close()
 
def addbook():
    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
    cur= mycon.cursor()
    while True:
        title = input('Enter title of the book: ')
        qry = 'select title from books;'
        cur.execute(qry)
        data = cur.fetchall()
        if (title,) not in data:
            isbn = input('Please enter ISBN of the book: ')
            category = input('Please enter category of the book: ')
            author = input('Please enter author of the book: ')
            pub = input('Please enter publisher of the book: ')
            price = input('Please enter price of the book: ')
            lang = input('Please enter lanuage of the book: ')
            qty = input('Please enter quantity of the book: ')
            qry = 'INSERT INTO books VALUES("{}","{}","{}","{}","{}","{}","{}","{}" )'.format(isbn, title, category, author,pub,price, lang, qty)
            cur.execute(qry)
            mycon.commit()
            print('\nBook added successfully')
            print('Returning back to MENU...')
            break
        else:
            print('\nBook already exists \'',title,'\' already exist')
            print('Enter \'1\' to try again')
            print('Enter \'2\' to return back to menu')
            choice = int(input('Enter your choice(1/2): '))
            if choice == 1:
                continue
            else:
                print('Returning back to MENU...')
                break
    mycon.close()
 
def updateBookDetails():
    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
    cur= mycon.cursor()
    while True:
        print('\n\n')
        print("**************************************")
        print("1. Update Book Quantity ")
        print("2. Update Book Price ")
        print("3. Update both Quantity and Price")
        print("4. Back to Main Menu")
        print("**************************************")
        menuChoice = int(input('Enter your choice(1-4): '))   
        inum = input('Enter the book\'s ISBN number: ')
        if menuChoice == 1:
            qty = int(input('Enter quantity: '))
            update_qry = 'update books set quantity = {} where isbn = "{}"'.format(qty, inum)
        elif menuChoice == 2:
            price = float(input('Enter new price : '))
            update_qry = 'update books set price = {} where isbn = "{}"'.format(price, inum)
            print(update_qry)
        elif menuChoice == 3:
            qty = int(input('Enter quantity: '))
            price = float(input('Enter new price : '))
            update_qry = 'update books set price = {}, quantity = {} where isbn = "{}"'.format(price,qty,inum)
        else :
            break
        qry = 'select isbn from books'
        cur.execute(qry)
        data = cur.fetchall()
        if (inum,) in data:
            cur.execute(update_qry)
            mycon.commit()
            print('\n Updated successfully!')
            print('Returning back to MENU...')
            break
        else:
            print('\nBook not found')
            print('Enter \'1\' to try again')
            print('Enter \'2\' to return back to menu')
            choice = int(input('Enter your choice(1/2): '))
            if choice == 1:
                continue
            else:
                print('Returning back to MENU...')
                break
    mycon.close()
 
def removeBook():
    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
    cur= mycon.cursor()
    while True:
        inum = input('Enter the book\'s ISBN number: ')
        qry = 'select isbn from books'
        cur.execute(qry)
        data = cur.fetchall()
        if (inum,) in data:
            choice = input('Confirm deletion(yes/no): ')
            if choice.lower() == 'yes':
                qry = 'delete from books where isbn = "{}"'.format(inum)
                cur.execute(qry)
                mycon.commit()
                print('\nBook deleted successfully!')
                print('Returning back to MENU...')
                break
            else:
                print('Terminating the delete process...')
                print('Returning back to MENU...')
                break
        else:
            print('\nBook not found')
            print('Enter \'1\' to try again')
            print('Enter \'2\' to return back to menu')
            choice = int(input('Enter your choice(1/2): '))
            if choice == 1:
                continue
            else:
                print('Returning back to MENU...')
                break
    mycon.close()
 
def viewAllBooks():
    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
    cur= mycon.cursor()
    print(' List of Books ')
    print('+--------------------------------------------------------------------------------------------------------+')
    print('| ISBN | title | Category | Author | Publisher | Price | Language | Quantity | ')
    print('|----------|-----------------|------------|------------------|----------|-------|--------|------|')
    print('\n')
    qry = 'select * from books'
    cur.execute(qry)
    data = cur.fetchall()
    for row in data:
        print('|%-10s|%-15s|%-10s|%-20s|%-15s|%-10s|%-10s|%-10s|'%(row[0],row[1], row[2],row[3], row[4], row[5],row[6],row[7]))
        print('+----------------------------------------------------------------------------------------------------+')
    print('\nReturning back to MENU...')
    mycon.close()
 
def searchBooks():
    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
    cur= mycon.cursor()
    print("**************************************")
    print("Make a choice:")
    print("1. Search by Title")
    print("2. Search by Authour")
    print("3. Search by ISBN")
    print("4. Exit")
    print("**************************************")
    menuChoice = int (input("Please enter your choice : "));
    if menuChoice == 1:
        print("Search by title");
        title = input("Please enter the title of the book : ");
        sqlstmt = 'select * from books where title like \'%' + title + '%\''
        print('\n' + sqlstmt + '\n')
        cur.execute(sqlstmt)
        data = cur.fetchall()
        print('+--------------------------------------------------------------------------------------------------------+')
        print('| ISBN | title | Category | Author | Publisher | Price | Language | Quantity | ')
        print('|----------|-----------------|------------|------------------|----------|-------|--------|------|')
        for row in data:
            print('|%-10s|%-15s|%-10s|%-20s|%-15s|%-10s|%-10s|%-10s|'%(row[0],row[1], row[2],row[3], row[4], row[5],row[6],row[7]))
        print('\n')
    elif menuChoice == 2:
        print("Search by author");
        author = input("Please enter the author of the book : ");
        sqlstmt = 'select * from books where author like \'%' + author + '%\''
        cur.execute(sqlstmt)
        data = cur.fetchall()
        print('+--------------------------------------------------------------------------------------------------------+')
        print('| ISBN | title | Category | Author | Publisher | Price | Language | Quantity | ')
        print('|----------|-----------------|------------|------------------|----------|-------|--------|------|')
        for row in data:
            print('|%-10s|%-15s|%-10s|%-20s|%-15s|%-10s|%-10s|%-10s|'%(row[0],row[1], row[2],row[3], row[4], row[5],row[6],row[7]))
        print('\n')
    elif menuChoice == 3:
        print("Search by ISBN");
        ISBN = input("Please enter the ISBN of the book : ");
        sqlstmt = 'select * from books where isbn like \'%' + ISBN + '%\''
        cur.execute(sqlstmt)
        data = cur.fetchall()
        print('+--------------------------------------------------------------------------------------------------------+')
        print('| ISBN | title | Category | Author | Publisher | Price | Language | Quantity | ')
        print('|----------|-----------------|------------|------------------|----------|-------|--------|------|')
        for row in data:
            print('|%-10s|%-15s|%-10s|%-20s|%-15s|%-10s|%-10s|%-10s|'%(row[0],row[1], row[2],row[3], row[4], row[5],row[6],row[7]))
        print('\n')
    else:
        print("exit");
    mycon.close()
 
def addOrder():
    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
    cur= mycon.cursor()
    while True:
        orderid = input('Enter customer order id : ')
        qry = 'select order_id from orderdetails'
        cur.execute(qry)
        data = cur.fetchall()
        if (orderid,) not in data:
            isbn = input('Enter ISBN number: ')
            custid = int(input('Enter customer ID: '))
            odate= input('Enter customer order date: ')
            empid = int(input('Enter Employee ID: '))
            qty = int(input('Enter quantity : '))
            qry = 'insert into orderdetails values ("{}","{}","{}", "{}","{}","{}")'.format(orderid,qty,isbn,odate,custid,empid)
            cur.execute(qry)
            mycon.commit()
            print('\nCustomer added successfully')
            print('Returning back to MENU...')
            break
        else:
            print('\nCustomer phone number \n'',phNo,\n already exist')
            print('Enter \'1\' to try again')
            print('Enter \'2\' to return back to menu')
            choice = int(input('Enter your choice(1/2): '))
            if choice == 1:
                continue
            else:
                print('Returning back to MENU...')
                break
    mycon.close()
 
 
 
def updateOrderdetails():
    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
    cur= mycon.cursor()
    while True:
        print("**************************************")
        print("1. Update Quantity ")
        print("2. Update Employee ID")
        print("3. Update both Quantity and Employee ID")
        print("4. Back to Main Menu")
        print("**************************************")
        menuChoice = int(input('Enter your choice(1-4): '))
        orderid = int(input('Enter your order id : '))
        if menuChoice == 1:
            qty = int(input('Enter the new quantity : '))
            final_qry = 'update orderdetails set qty = {} where order_id = {}'.format(qty, orderid)
        elif menuChoice == 2:
            empid = int(input('Enter new employee id : '))
            final_qry = 'update orderdetails set emp_id = {} where order_id = {}'.format(empid, orderid)
        elif menuChoice == 3:
            qty = int(input('Enter the new quantity : '))
            empid = int(input('Enter new employee id : '))
            final_qry = 'update orderdetails set emp_id = {}, qty = {} where order_id = {}'.format(empid,qty, orderid)
        else :
            break
        qry = 'select order_id from orderdetails'
        cur.execute(qry)
        data = cur.fetchall()
        if (orderid,) in data:
            cur.execute(final_qry)
            mycon.commit()
            print('\nOrder ID number updated successfully!')
            print('Returning back to MENU...')
            break
        else:
            print('\nOrder ID not found')
            print('Enter \'1\' to try again')
            print('Enter \'2\' to return back to menu')
            choice = int(input('Enter your choice(1/2): '))
            if choice == 1:
                continue
            else:
                print('Returning back to MENU...')
                break
    mycon.close()
 
 
def removeOrder():
    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
    cur= mycon.cursor()
    while True:
        orderid = int(input('Enter customer Order ID number: '))
        qry = 'select order_id from orderdetails'
        cur.execute(qry)
        data = cur.fetchall()
        if (orderid,) in data:
            choice = input('Confirm deletion(yes/no): ')
            if choice.lower() == 'yes':
                qry = 'delete from orderdetails where order_id = {}'.format(orderid)
                cur.execute(qry)
                mycon.commit()
                print('\nCustomer order id removed successfully!')
                print('Returning back to MENU...')
                break
            else:
                print('Aborting delete process...')
                print('Returning back to MENU...')
                break
        else:
            print('\nCustomer not found')
            print('Enter \'1\' to try again')
            print('Enter \'2\' to return back to menu')
            choice = int(input('Enter your choice(1/2): '))
            if choice == 1:
                continue
            else:
                print('Returning back to MENU...')
                break
    mycon.close()
 
def viewAllOrders():
    mycon = sqltor.connect(host = 'localhost', user = 'root', passwd = 'user123',database = 'bookstore')
    cur= mycon.cursor()
    print(' Orders ')
    print('+-------------------------------------------------------------------------------------+')
    print('| order_id| Quantity | ISBN | orderdate | cust_id | emp_id |')
    print('|----------|------|-----------------------------|-------------------|-------------|--------------|')
    qry = 'select * from orderdetails'
    cur.execute(qry)
    data = cur.fetchall()
    for row in data:
        print('|%-10s|%-15s|%-25s|%-15s|%-15s|%-15s|'%(row[0],row[1], row[2],row[3], row[4], row[5]))
        print('+-------------------------------------------------------------------------------------+')
    print('\nReturning back to MENU...')
    mycon.close()
 
 
while True:
    print("<<<<<<MAIN MENU>>>>>> \n1.EMPLOYEE \n2.CUSTOMERS \n3.BOOKS \n4.ORDER DETAILS \nPRESS ANY OTHER KEY TO EXIT")
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        while True:
            print("<<<<<<EMPLOYEE>>>>>> \n1.ADD EMPLOYEE \n2.REMOVE EMPLOYEE \n3.VIEW EMPLOYEE\n4 UPDATE SALARY OR PHONE NO \n PRESS ANY OTHER KEY TO EXIT")
            choice2=int(input("ENTER YOUR CHOICE:"))
            if choice2==1:
                addEmployee()
            elif choice2==2:
                deleteEmployeeDetails()
            elif choice2==3:
                viewAllEmployees()
            elif choice2==4:
                updateEmployeeDetails()
            else:
                print("EXITING EMPLOYEE")
                break
    elif choice==2:
        while True:
            print("<<<<<<CUSTOMER>>>>>> \n1.ADD CUSTOMER \n2.REMOVE CUSTOMER \n3.VIEW CUSTOMER\n4 UPDATE PHONE OR ADDRESS \n PRESS ANY OTHER KEY TO EXIT")
            choice2=int(input("ENTER YOUR CHOICE:"))
            if choice2==1:
                addCust()
            elif choice2==2:
                removeCust()
            elif choice2==3:
                viewAllCust()
            elif choice2==4:
                updateCustomerPhoneNumber()
            else:
                print("EXITING CUSTOMER")
                break
    elif choice==3:
        while True:
            print("<<<<<<BOOKS>>>>>> \n1.UPDATE QUANTITY \n2.VIEW DETAILS OF A BOOK \n3.REMOVE BOOK \n4.ADD BOOK \n PRESS ANY OTHER KEY TO EXIT")
            choice2=int(input("ENTER YOUR CHOICE:"))
            if choice2==1:
                updateBookDetails()
            elif choice2==2:
                viewAllBooks()
            elif choice2==3:
                removeBook()
            elif choice2==4:
                addbook()
            else:
                print("EXITING BOOK")
                break
    elif choice==4:
        while True:
            print("<<<<<<ORDER DETAILS>>>>>> \n1.ADD ORDER \n2.UPDATE ORDER DETAILS \n3.REMOVE ORDER \n4.VIEW ALL ORDER \n PRESS ANY OTHER KEY TO EXIT")
            choice2=int(input("ENTER YOUR CHOICE:"))
            if choice2==1:
                addOrder()
            elif choice2==2:
                updateOrderdetails()
            elif choice2==3:
                removeOrder()
            elif choice2==4:
                viewAllOrders()
            else:
                print("EXITING BOOK")
                break
    else:
        print("EXITING MAIN MENU")
        break
 
