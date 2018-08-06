import sqlite3
import sys
conn=sqlite3.connect('im.db')
cur=conn.cursor()
def login() :
	while True:
		user_name = raw_input('enter the Username  :')
		passw = raw_input('enter the password   :')
		sql = ("SELECT * from login where user_name = ? AND password = ?")
		cur.execute(sql,[(user_name),(passw)])
		r = cur.fetchall()
		if r:
			for i in r:
				print "\n"
				print ("--------------Admin logged in--------------- ")
			break
		else:
			print "Invalid Username Password"
			a = raw_input("Do u want to try again (y/n)?")
			if a.lower() == "n":
				print "------------thankyou bye !----------------"
				sys.exit()
def add() :
	print(' ')
	print('======================================================================')
	n=input('number of items to be add :')
	print(' ')
	print('========================================================================')
	for i in range(n) :
		item_id=input('enter the id      :')
		iteam_name=raw_input('enter the name    :')
		quantity=input('enter the qantity :')
		price=float(input('price of the item:'))
		tax=float(input('enter the tax    :'))
		print('----------------------------------------------------------------------------')
		sql="INSERT INTO stock(item_id,iteam_name,quantity,price,tax) VALUES(?,?,?,?,?)"
		cur.execute(sql,(item_id,iteam_name,quantity,price,tax))
		cur.execute("SELECT * FROM stock")
		a=cur.fetchall()
		l=len(a)
		print(' ')
		print('--------------------------------------------------------------------')
		print ('id       ','name       ','quantity    ','price      ','tax')
		print('---------------------------------------------------------------------')
		for j in range(0,l) :
			print(' ')
			print a[j][0],'\t\t',a[j][1],'\t\t',a[j][2],'\t\t',a[j][3],'\t\t',a[j][4]
		print('=======================================================================')
		conn.commit()
def delete() :
	print(' ')
	print('------------------------------------------------------------')
	i=raw_input('enter the id for delete')
	sql="DELETE FROM stock WHERE item_id = %s" %(i)
	try:
		cur.execute(sql)
		conn.commit()
	except:
		conn.rollback()
	cur.execute("SELECT * FROM stock")	
	a=cur.fetchall()
	l=len(a)
	print(' ')
	print('--------------------------------------------------------------------')
	print ('id       ','name       ','quantity    ','price      ','tax')
	print('---------------------------------------------------------------------')
	for j in range(0,l) :
		print(' ')
		print a[j][0],'\t\t',a[j][1],'\t\t',a[j][2],'\t\t',a[j][3],'\t\t',a[j][4]
	print('=======================================================================')
def display() :
	cur.execute("SELECT * FROM stock")
	a=cur.fetchall()
	l=len(a)
	print(' ')
	print('--------------------------------------------------------------------')
	print ('id       ','name       ','quantity    ','price      ','tax')
	print('---------------------------------------------------------------------')
	for j in range(0,l) :
		print(' ')
		print a[j][0],'\t\t',a[j][1],'\t\t',a[j][2],'\t\t',a[j][3],'\t\t',a[j][4]
	print('============================================================')
	conn.commit()
def price() :
	item_id=input('enter the id of item  :')
	i=float(input('enter the new price   :'))
	sql="UPDATE stock SET price = %f WHERE item_id = %d" %(i,item_id)
	try:
		cur.execute(sql)
		conn.commit()
	except:
		conn.rollback()
	cur.execute("SELECT * FROM stock")
	a=cur.fetchall()
	l=len(a)
	print(' ')
	print('--------------------------------------------------------------------')
	print ('id       ','name       ','quantity    ','price      ','tax')
	print('---------------------------------------------------------------------')
	for j in range(0,l) :
		print(' ')
		print a[j][0],'\t\t',a[j][1],'\t\t',a[j][2],'\t\t',a[j][3],'\t\t',a[j][4]
	print('============================================================')
	conn.commit()
def tax() :
	item_id=input('enter the id of item :')
	i=float(input('enter the new tax    :'))
	sql="UPDATE stock SET tax = %f WHERE item_id = %d" %(i,item_id)
	try:
		cur.execute(sql)
		conn.commit()
	except:
		conn.rollback()
	cur.execute("SELECT * FROM stock")	
	a=cur.fetchall()
	l=len(a)
	print(' ')
	print('----------------------------------------------------------------------')
	print ('id       ','name       ','quantity    ','price      ','tax')
	print('-----------------------------------------------------------------------')
	for j in range(0,l) :
		print(' ')
		print a[j][0],'\t\t',a[j][1],'\t\t',a[j][2],'\t\t',a[j][3],'\t\t',a[j][4]
	print('=======================================================================')
	conn.close()
def qty() :
	item_id=input('enter the id of item :')
	i=float(input('enter the new quamtity  :'))
	sql="UPDATE stock SET quantity = %s WHERE item_id = %d" %(i,item_id)
	try:
		cur.execute(sql)
		conn.commit()
	except:
		conn.rollback()
	cur.execute("SELECT * FROM stock")	
	a=cur.fetchall()
	l=len(a)
	print(' ')
	print('--------------------------------------------------------------------')
	print ('id       ','name       ','quantity    ','price      ','tax')
	print('---------------------------------------------------------------------')
	for j in range(0,l) :
		print(' ')
		print a[j][0],'\t\t',a[j][1],'\t\t',a[j][2],'\t\t',a[j][3],'\t\t',a[j][4]
	print('=======================================================================')
	conn.close()
def list() : 
	t1=[]
	condition1='y'
	print('--------------------------------------------------------------------------------')
	print ('id       ','name       ','price      ','tax      ','quantity   ','total')
	print('--------------------------------------------------------------------------------')
	while condition1=='y' or condition2=='y':
		condition1='n'
		i=raw_input('enter the item id    :')
		q=input('enter the quantity of item  :')
		sql="SELECT * FROM stock WHERE item_id = %s" %(i)
		cur.execute(sql)
		conn.commit()
		a=cur.fetchall()
		l=len(a)
		o=[]
		print(' ')
		for j in range(0,l) :
			t=(a[j][3]+a[j][4])*q
			t1.append(t)
			print(' ')
			print a[j][0],'\t\t',a[j][1],'\t\t',a[j][3],'\t\t',a[j][4],'\t\t',q,'\t\t',t
			x=a[j][2]
			o.append(x)
		i1=o[0]-q
		item_id=i
		sql="UPDATE stock SET quantity = %s WHERE item_id = %s" %(i1,item_id)
		cur.execute(sql)
		conn.commit()
		condition2=raw_input("Do you want to add more items (y/n) ?    ")
	le=len(t1)
	print (' ')
	print(' ')
	print ('                                                                  GRAND TOTAL='),sum(t1)
	print(' ')
	print('===============================================================================================')
	conn.commit()
def main() :
	m='y'
	while m=='y' or m1=='y' :
		m='n'
		print(' ')
		print('--------------------------------------------------------------------')
		print(' ')
		print('Login')
		print('-----')
		login()
		print(' ')
		print('--------------------------------------------------------------------')
		print('				MAIN MENU 				')
		print('--------------------------------------------------------------------')
		a=input('	  1: Billing          2: Stock Management    :   ')
		print(' ') 
		print('--------------------------------------------------------------------')
		if a==1 :
			list()
		if a==2 :
			print(' ')
			print('--------------------------------------------------------------------')
			b=input('1:Display    2:Add items    3:Delete items     4:Edit    :   ')
			print(' ')
			print('--------------------------------------------------------------------')
			if b==1 :
				display()
			if b==2 :
				add()
			if b==3 :
				delete()
			if b==4 :
				print(' ')
				print('--------------------------------------------------------------------')
				c=input('1:price      2:tax     3:quantity   :  ')
				print(' ')
				print('--------------------------------------------------------------------')
				if c==1 :
					price()
				if c==2 :
					tax()
				if c==3 :
					qty()
		print(' ')
		print('--------------------------------------------------------------------')
		m1=raw_input('go back to main menu y/n   :  ')
		print(' ')
		print('--------------------------------------------------------------------')
main()
