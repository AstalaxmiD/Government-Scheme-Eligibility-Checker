from lib2to3.pgen2.token import NUMBER
import pywebio
from pywebio.input import *
from pywebio.output import *

put_html("<h1>Government Scheme Eligibilty Checker</h1> <br> <br>")
age= input("Input your age", type=NUMBER)
income = input("Input your annual income", type=FLOAT)
fincome=input("enter the total income of your family per year:",type=FLOAT)

education=radio("did you graduate school?",options=["yes","no"])
if education=="no":
    e1=input("what is the last grade you passed in school? -grade number ",type=NUMBER)
if education=="yes":
    e1=12

e2=radio("have you graduated college?",options= ["yes","no"] )
employed=radio("are you employed?",options=["yes","no"])
sector=radio("what sector would you like to start or own a business in manufacturing,business,service or agriculture?",options=["manufacturing","business","service","agriculture"])
if sector=="manufacturing":
    sector="m"
if sector=="business":
    sector="b"   
if sector=="service":
    sector="s"  
if sector=="agriculture":
    sector="a"   
if employed=="yes":
    source=radio("do you earn money through manual labour or daily wage?",options=["yes","no"])
    business=radio("do you own a business?",options=["yes","no"] )
    
    final=fincome/12
    
    if business=="yes":

        b1=input("total net worth of business=",type=FLOAT)
        b2=radio("is it a non individual enterprise?",options=["yes","no"]) 
        if b2=="yes":
            b3=input("How many percent of the company do you own?",type=FLOAT)
        if b2=="no":
            b3=100
        time=input("how many years ago did your business' commercial production began?",type=FLOAT)
        at=input("what is your business' annual turnover?",type=FLOAT)
    

    else:
        b1,b2,b3=0,"n",0
        b4=radio("are you interested in starting a business?",options=["yes","no"])
        if b4=="yes":
            cost=input("what is the minimum budget for your business?",type=FLOAT)
            
        else:
            cost=0
            
if employed=="no":
    source,business,b1,b2,b3,b4,cost="s","s",0,"s",0,"s",0
gender=radio("what is your gender?",options=["Female","Male"]) 
if gender=="Female":
    gender="F"
if gender=="Male":
    gender="M"
citizen=radio("are you an India citizen?",options=["yes","no"])
bankaccount=radio("do you have a bank account?",options=["yes","no"])
socialsecurity=radio("are you a member of any statutory social security scheme?",options=["yes","no"])
caste=radio("is your caste Scheduled caste or tribe?",options=["yes","no"])
caste1=radio("do you belong to backward class?",options=["yes","no"])
group=radio('do you belong to any minority community?',options=["yes","no"])
farmer=radio("are you a farmer?",options=["yes","no"])
if farmer=="yes":
    size=input("how many hectares of land do you own?",type=FLOAT)
    l1=radio("do you own cultivable land?",options=["yes","no"]) 
    if l1=="yes":
        l2=radio("are you growing crops on your land ?",options=["yes","no"])
    if l1=="no":
        l2="no"
if farmer=="no":
    size=0
    l1="no"
land=radio("do you own any land?",options=["yes","no"])
shg=radio("are you a part of a self help group?",options=["yes","no"])
loan=radio("have you defaulted in any loan?",options=["yes","no"])
set=input("how many years have you been a permanent resident of your current residing area?",type=FLOAT)
family=radio("do you have a family?",options=["yes","no"])
family1=radio("do you have societal support or means of subsistance?",options=["yes","no"])
if family=="yes":
    f1=radio("any male member aged 16-59 in your family?",options=["yes","no"])
    f2=radio("Do you have any specially abled member in your family?",options=["yes","no"])
    f3=radio("any professionals like doctors,lawyers etc. in your family?",options=["yes","no"])
    f4=radio("Any family member works in a government job including yourself?",options=["yes","no"])
    house1=radio("Do you or any family member own a house i.e not makeshift ?",options=["yes","no"])
if family=="no":
    f1,f2,f3,f4,house1="no","no","no","no","no"
    
house=radio("do you live in a makeshift house?",options=["yes","no"])
job=radio("are you interested in pursuing scientific research?",options=["yes","no"])
if job=="yes":
    j1=radio("do you hold a  academic or research position in a recognized institution?",options=["yes","no"])
    j2=input("how long does your research need to be funded for i.e in years?",type=FLOAT)
if job=="no":
    j1="a"
    j2=6
ill=radio("are you terminally ill?",options=["yes","no"])
ur=radio("do you live in a urban or rural area?",options=["urban","rural"])
lpg=radio("do you have a lpg connection?",options=["yes","no"])

c=0 
if gender=="F":
    p1=radio("are you a pregnant or lactating mother?",options=["yes","no"])
p2=input("how many children do you have?",type=NUMBER)
if gender=="M":
    p1="s"
put_html("<h3>List of schemes you are eligible for-</h3><br>") 

if age>=18 and b1<50000000 and business=="yes" and age<65 and citizen=="yes":
    c+=1
    put_text(c,'. Pradhan Mantri Mudra Yojana')
   
if age>=18 and bankaccount=="yes" and age<=70 and citizen=="yes":
    c+=1
    put_text(c,'. Pradhan Mantri Suraksha Bima Yojana')
   
if age>=18 and age<60 and citizen=="yes":
    c+=1
    put_text(c,'. Pradhan Mantri Jan Dhan Yojana') 
    
if age>=18 and age<60 and citizen=="no":  
    c+=1
    put_text(c,". Pradhan Mantri Jan Dhan Yojana-provided the background checks done by the bank labels you as low risk") 
   
if age>=10 and age<18 and citizen=="yes":
    c+=1
    put_text(c,". Pradhan Mantri Jan Dhan Yojana provided the support of a guardian ")
   
if age>=18 and socialsecurity=="no" and age<40 and citizen=="yes" and bankaccount=="yes":
    c+=1
    put_text(c,'. Atal Pension Yojana')
    
if age>=18 and age<50 and citizen=="yes" and ill=="no":
    c+=1
    put_text(c,'. Pradhan Mantri Jeevan Jyoti Bima Yojana- provided a medical certificate attesting that the person is not diagnosed with any critical illness is provided')

if age>18 and caste=="yes" and citizen=="yes" and b3>=51:
    c+=1
    put_text(c,'. Stand Up India')

if age>18 and caste=="no" and citizen=="yes" and b3>=51 and gender=="F":
    c+=1
    put_text(c,'. Stand Up India')

if age>60 and citizen=="yes":
    c+=1
    put_text(c,'. Pradhan Mantri Vaya Vandhana Yojana- note- this is a retirement cum pension scheme that has a purchase price of 1.5 lakhs minimum')


if age>=18 and source=="no" and house=="yes" and family=="yes" and citizen=="yes" and caste=="yes" and ur=="urban" :
    c+=1
    put_text(c,'. Ayushman Bharat Yojana')
if age>=18 and source=="yes" and house=="no" and family=="yes" and f1=="no" and f2=="yes" and citizen=="yes" and caste=="yes" and ur=="rural" :
    c+=1
    put_text(c,'. Ayushman Bharat Yojana')
if age>=18 and source=="yes" and house=="no" and family=="yes" and f1=="yes" and f2=="no" and citizen=="yes" and caste=="yes" and ur=="rural" :
    c+=1
    put_text(c,'. Ayushman Bharat Yojana')

if age>18 and employed=="no" and age<35 and citizen=="yes" and final>=40000 and final<=100000 and loan=="no" and set>=3 and e1>=8:
    c+=1
    put_text(c,". Pradhan Mantri Rozgar Yojana")

if age>18 and citizen=="yes" and e1<8 and business=="no" and b4=="yes" and cost<1000000 and sector=="m":
    c+=1
    put_text(c,'. Pradhan Mantri Employement Generation Program')

if age>18 and citizen=="yes" and e1<8 and business=="no" and b4=="yes" and cost<500000 and sector=="s":
    c+=1
    put_text(c,'. Pradhan Mantri Employement Generation Program')
if age>18 and citizen=="yes" and business=="no" and b4=="yes" and e1<8 and cost<500000 and sector=="b":
    c+=1
    put_text(c,'. Pradhan Mantri Employement Generation Program')

if age>18 and citizen=="yes" and e1>=8 and business=="no" and b4=="yes" and cost<2500000 and sector=="m":
    c+=1
    put_text(c,'. Pradhan Mantri Employement Generation Program') 

if age>18 and citizen=="yes" and e1>=8 and business=="no" and b4=="yes" and cost<1000000 and sector=="s":
    c+=1
    put_text(c,'. Pradhan Mantri Employement Generation Program') 
if age>18 and citizen=="yes" and e1>=8 and business=="no" and b4=="yes" and cost<1000000 and sector=="b":
    c+=1
    put_text(c,'. Pradhan Mantri Employement Generation Program')
if age>=19 and p1=="yes" and  p2==0 and gender=="F" and citizen=="yes":
    c+=1
    put_text(c,". Pradhan Mantri Matrivita Vandana Yojana provided you are not receiving any similar benefits from another government scheme")

if age>18 and ur=="urban" and income<=11520 and citizen=="yes":
    c+=1
    put_text(c,". Deen Dayal Upadhyaya Antyodaya Yojana")

if age>18 and ur=="rural" and income<=9360 and citizen=="yes":
    c+=1
    put_text(c,". Deen Dayal Upadhyaya Antyodaya Yojana")

if e1<12 and age>=18 and e2=="no" and citizen=="yes":
    c+=1
    put_text(c,". Pradhan Mantri Kaushal Vikas Yojana")

if age>=18 and income>=300000 and income<1800000 and house1=="no" and citizen=="yes":
    c+=1
    put_text(c,". Pradhan Mantri Awas Yojana") 

if house=="yes" and citizen=="yes":
    if age>=60 or f2=="yes" or family1=="no" or family=="no" or source=="yes":
        c+=1
        put_text(c,". Antyodaya Anna Yojana")

if gender=="F" and bankaccount=="yes" and ur=="rural" and income<=9360 and lpg=="no" and citizen=="yes":
    c+=1
    put_text(c,". Pradhan Mantri Ujjwala Yojana provided you have a bpl certificate which you are eligible you apply for if otherwise ")
if ur=="rural" and age>=18 and land=="yes" and citizen=="yes":
    c+=1
    put_text(c,". Svamitva Yojana")

if age>=18 and citizen=="yes" and sector=="a":
    if farmer=="yes" or business=="yes" or shg=="yes":
        c+=1
        put_text(c,". The Venture Capital Assistance Scheme")

if age>=18 and business=="yes" and time<1 and citizen=="yes" and b1<=100000000 and at<=500000000:
    c+=1
    put_text(c,". Single Point Registration Scheme") 

if age>=18 and job=="yes" and citizen=="yes" and j1=="yes" and j2<=5 :
    c+=1
    put_text(c,". High Risk High Reward Research Funding Scheme - the duration of funding can be extended to five years maximum for exeptional cases from the regular three year period ")



if age>=18 and citizen=="yes":
    if farmer=="yes" or business=="yes" or shg=="yes":
        c+=1
        put_text(c,". Dairy Entrepreneurship Development Scheme")

if age>=18 and job=="yes" and citizen=="yes":
    c+=1
    put_text(c,". Promoting Innovations in Individuals,Startups and MSMEs Scheme") 

if age>=18 and group=="yes" and citizen=="yes" and business=="yes" and fincome<=600000:
    c+=1
    put_text(c,". Self Employement Lending Schemes-Credit Line 2 - Term Loan Scheme") 

if age>=18 and farmer=="yes" and citizen=="yes":
    if l1=="yes" or size<2:
        c+=1
        put_text(c,". PM-Kisan")
if age>=18 and gender=="F" and income<=81000 and ur=="rural" and caste1=="yes":
     c+=1
     put_text(c,". New Swarnima for women")

if age>=18 and gender=="F" and income<=103000 and ur=="urban" and caste1=="yes":
     c+=1
     put_text(c,". New Swarnima for women")

if age>=18 and farmer=="yes" and l2=="yes" :
     c+=1
     put_text(c,". Pradhan Mantri Fasal Bima Yojana ")

put_html("<br><br><br><br><br>The source code of this website is subject to copyright, any scrapping or unintended utilization or modification of the source code is not permitted and will be legally dealt with. ")

pywebio.start_server(port=55)
