import mysql.connector
db= mysql.connector.connect(host='virtualsystems.ce2iv41q3fxl.us-east-1.rds.amazonaws.com',
                            user='admin',
                            password='123456789',
                            port=3306,
                            database='uoh'
                           )

cursor=db.cursor()

value = None
logs=[]

def menu():
    print('''MENU
                a – Add cases
                o – Output all cases in console
                q – Quit'''
         )
    
def addCovidLog():
    s={}
    print(">>>>>>>>>>>>>>>>>>>")
    countryname = input("Enter Country: ")
    year= input("Enter Year: ")
    totalcases = input("Enter total cases: ")
    deaths = input("Enter total deaths: ")
    recovered = input("Enter recovered: ")

    try:
        s['countryname']=str(countryname)
        s['year']=str(year)
        s['totalcases']=str(totalcases)
        s['deaths']=str(deaths)
        s['recovered']=str(recovered)
        logs.append(s)
    except:
        print("\nInvalid Input! Try Again")
        addCovidLog()
        

def outputEntire():
    f=0
    print("ID\tCountry\tYear\tTotal Cases\tDeaths\trecovered")
    s='select * from covidcases'
    cursor.execute(s)
    myresult = cursor.fetchall()
    for x in myresult:
        print(str(x[0])+'\t'+x[1]+'\t'+x[2]+'\t'+x[3]+'\t'+x[4]+'\t'+x[5])
        print('\t')
    print("\n")


def saveLog():
    for row in logs:
        s= 'INSERT INTO covidcases(countryname,year,totalcases,deaths,recovered) values(%s,%s,%s,%s,%s)'
        t=(row['countryname'],row['year'],row['totalcases'],row['deaths'],row['recovered'])
        cursor.execute(s,t)
        db.commit()

        
        
while(value!='q'):
    menu()
    value=input("Select option: ")
    if(value == 'a'):
        addCovidLog()
        saveLog()
    elif(value == 'o'):
        outputEntire()
    elif (value == 'q'):
        break

    else:
        print("Not Valid input\n")
