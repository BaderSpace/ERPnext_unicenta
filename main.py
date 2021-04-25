import requests
import json
import mysql.connector



#############################################################################################################
################################################## UNICENTA #################################################
#############################################################################################################

chars = ["<", ">", ",", '"', "/", "%", "^", "*", ";"]

def get_payments():
    #Get the payments from the local database of unicenta pos
    cnxn = mysql.connector.connect(user='USERNAME', password='PASSWORD', host='127.0.0.1', database='THE NAME OF THE DATABASE') #enter the database user and pwd
    cursor = cnxn.cursor(dictionary=True)
    cursor.execute("""
    select * from payments
    """)
    #store it in a file called payments.txt
    with open('data/payments.txt', 'w+', encoding='utf-8') as file:
        for x in range(int(cursor.rowcount)):
            total = cursor.fetchone()['total']
            file.write(str(total)+'\n')

#TODO get the sales of each item
def get_sales():
    pass

#############################################################################################################
################################################## ERPNEXT ##################################################
#############################################################################################################

headers = {
'Accept': 'application/json',
'Content-Type': 'application/json'
}

url = 'ENTER YOUR ERPNEXT URL HERE'

def login():
    #login to erpnext with the login credentials
    body = {
    'usr': 'YOUR EMAIL OR USERNAME',
    'pwd': 'YOUR PASSWORD'
    }
    r = requests.post("{}/api/method/login".format(url), data=json.dumps(body), headers=headers)
    if r.status_code == 200:
        print('Logged in as {}'.format(dict(r.json())['full_name']))
    else: print('Failed to login, ERR: {}'.format(dict(r.json())['message']))

if __name__ == '__main__':
    #Start
