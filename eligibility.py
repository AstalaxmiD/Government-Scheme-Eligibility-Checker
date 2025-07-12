
import pywebio  
from pywebio.input import NUMBER
import os
from pywebio.input import *
from pywebio.output import *  
from pywebio.output import put_file
from fpdf import FPDF





def eligibility(): 
   

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    
    put_html("<h1>Government Scheme Eligibilty Checker</h1> <br> <br>") 
    info=input_group(' basic user info',[
    input("Input your age:", name='age',type=NUMBER), 
    radio("What is your gender?",name='gender',options=["Female","Male"]),
    input("Enter the total income of your family per year:",name='fincome',type=FLOAT),
    radio("Did you graduate school?",name='education',options=["yes","no"]),
    radio("Have you graduated college?",name='e2',options= ["yes","no"] ), 
    radio("Are you employed?",name='employed',options=["yes","no"]), 
    checkbox("What schemes are you interested in?(you can choose more than 1)",name='business1',options=['business','education','agriculture/agribusiness','financial aid','medical aid','all','job opportunities','sustenance aid'])
    ]) 
    infox=input_group('income based group determination:',[
    input("Input your annual income",name='income',type=FLOAT),
    radio("Which area are you residing in?",name='ur',options=['urban','rural'])
    ]) 
    income=infox['income'] 
    ur=infox['ur']
    if income<=9360 and ur=="rural":
        popup("Income based grouping:"," You will be displayed schemes eligible for the income group:Below povery line")
    if income<=11520 and ur=="urban":
        popup("Income based grouping:"," You will be displayed schemes eligible for the income group:Below povery line")
    if income>9360 and ur=="rural" and income<100000:
        popup("Income based grouping:"," You will be displayed schemes eligible for the income group:Above povery line")
    if income>=11520 and ur=="urban" and income<100000:
        popup("Income based grouping:"," You will be displayed schemes eligible for the income group:Above povery line") 
    if income>100000: 
        popup("Income based grouping:"," You will be displayed schemes eligible for the income group:Middle-High income")

    age=info['age'] 

    fincome=info['fincome'] 
    education=info['education']
    e2=info['e2']  
    employed=info['employed']  
    gender=info['gender'] 
    business1=info['business1']



    if education=="no":
        e1=input("What is the last grade you passed in school? -grade number ",type=NUMBER)
    if education=="yes": 
        e1=12


    if employed=="yes": 
        info1=input_group('',[
        radio("Do you earn money through manual labour or daily wage?",name='source',options=["yes","no"]) 
        ])  

        source=info1['source']
   

    if 'business' in info['business1'] or 'all' in info['business1'] or 'agriculture/agribusiness' in info['business1'] and len(info['business1'])>1: 
        business=radio("Do you own a business?",options=["yes","no"] ) 
        sector=checkbox('Which sector are you interested to start a venture or own a venture in?(you can choose more than 1)',options=['manufacturing','agriculture','service','business'])
        if "agriculture/agribusiness" in business1 and len(business1)==1:
            sector='agriculture'
    else:
        business=None 
        sector=None
    
    
    final=fincome/12
    
    if business=="yes":
        if 'business' in info['business1'] or 'all' in info['business1']:
            b4="yes"
            info2=input_group('',[
            input("total net worth of business=",name='b1',type=FLOAT),
            radio("Is it a non individual enterprise?",name='b2',options=["yes","no"]) 
            ])
            b1=info2['b1']
            b2=info2['b2']
            if b2=="yes":
                b3=input("How many percent of the company do you own?",type=FLOAT)
            if b2=="no":
                b3=100
            info3=input_group('',[
            input("How many years ago did your business' commercial production began?",name="time",type=FLOAT),
            input("What is your business' annual turnover?",name='at',type=FLOAT)
            ])
            time=info3['time']
            at=info3['at']   
    else: 
        time=None
        at=None
        b4="no" 
        cost=0
        b1,b2,b3=0,"no",0
   
    b4=radio("Are you interested in starting a business?",options=["yes","no"])
    if b4=="yes": 
        
        cost=input("What is the minimum budget for your business?",type=FLOAT)
            
    else:
        cost=0
            
    if employed=="no":
        source,business,b1,info2,b2,b3,b4,cost="s","s",0,"s",0,0,0,0

    if gender=="Female":
        gender="F"
    if gender=="Male":
        gender="M" 

    popup("Statutory social schemes:","These schemes were launched on 9th May, 2015, for providing life & accident risk insurance and social security at a very affordable cost namely (a) Pradhan Mantri Suraksha Bima Yojana and (b) Pradhan Mantri Jeevan Jyoti Yojana and (c) Atal Pension Yojana.")
    popup("Minority Communities:","Muslims, Sikhs, Christians, Buddhists, Jain and Zorastrians (Parsis) have been notified as minority communities under Section 2 (c) of the National Commission for Minorities Act, 1992.")

    info4=input_group('',[
    radio("Are you an Indian citizen?",name='citizen',options=["yes","no"]),
    radio("Do you have a bank account?",name='bankaccount',options=["yes","no"]),
    radio("Are you a member of any statutory social security scheme?",name='socialsecurity',options=["yes","no"]),
    radio("Is your caste Scheduled caste or tribe?",name='caste',options=["yes","no"]),
    radio("Do you belong to backward class?",name='caste1',options=["yes","no"]),
    radio('Do you belong to any minority community?',name='group',options=["yes","no"]), 
    radio("Are you a farmer?",name='farmer',options=["yes","no"])
    ]) 
    citizen=info4['citizen']
    bankaccount=info4['bankaccount']
    socialsecurity=info4['socialsecurity']
    caste=info4['caste']
    caste1=info4['caste1']
    group=info4['group']
    farmer=info4['farmer']
    l1=None
    if farmer=="yes": 
        if "all" in info['business1'] or "agriculture/agribusiness" in info['business1'] or farmer=="yes":
    
            size=input("How many hectares of land do you own?",type=FLOAT) 
            if size>0:
                l1=radio("Do you own cultivable land?",options=["yes","no"]) 
            if l1=="no" and size>0:

                land=radio("Do you own any land?",options=["yes","no"])
            else:
                land="yes"
        if l1=="yes":
            l2=radio("Are you growing crops on your land ?",options=["yes","no"])
        if l1=="no":
            l2="no"
    if farmer=="no":
        size=0
        l1="no" 
        l2=None 
        land=None
 
    popup("Self Help Group(SHG):","Self Help Groups (SHGs) are small groups of poor people in villages. The members of an SHG face similar problems. They help each other, to solve their problems. SHGs promote small savings among their members. The savings are kept with the bank.")    
    info5=input_group('',[
    radio("Are you a part of a self help group?",name='shg',options=["yes","no"]),
    radio("Have you defaulted in any loan?",name='loan',options=["yes","no"]),
    input("How many years have you been a permanent resident of your current residing area?",name='set',type=FLOAT),
    radio("Do you have a family?",name='family',options=["yes","no"]),
    radio("Do you have societal support or means of subsistance?",name='family1',options=["yes","no"])
    ])

    shg=info5['shg']
    loan=info5['loan']
    set=info5['set'] 
    family=info5['family'] 
    family1=info5['family1']

    if family=="yes": 
        info6=input_group('',[
        radio("Any male member aged 16-59 in your family?",name='f1',options=["yes","no"]),
        radio("Do you have any specially abled member in your family?",name='f2',options=["yes","no"]),
        radio("Any professionals like doctors,lawyers etc. in your family?",name='f3',options=["yes","no"]),
        radio("Any family member works in a government job including yourself?",name='f4',options=["yes","no"]),
        radio("Do you or any family member own a house i.e not makeshift ?",name='house1',options=["yes","no"])
        ]) 
        f1=info6['f1']
        f2=info6['f2']
        f3=info6['f3']
        f4=info6['f4']
        house1=info6['house1']

    if family=="no":
        f1,f2,f3,f4,house1="no","no","no","no","no"

    info7=input_group('',[
    radio("Do you live in a makeshift house?",name='house',options=["yes","no"]),
 
    ]) 
    if "education" in info['business1']:
        job=radio("Are you interested in pursuing scientific research?" ,options=["yes","no"]) 
    else:
        job=None

    house=info7['house']
    if job=="yes": 
        info8=input_group('',[
        radio("Do you hold a  academic or research position in a recognized institution?",name='j1',options=["yes","no"]),
        input("How long does your research need to be funded for i.e in years?",name='j2',type=FLOAT)
    ]) 
        j1=info8['j1']
        j2=info8['j2']
    if job=="no":
        j1=None
        j2=None 
    popup("Terminally Ill:","An individual who has been certified by a physician as having an illness or physical condition which can reasonably be expected to result in death in 24 months or less after the date of the certification.")
    info9=input_group('',[
    radio("Are you terminally ill?",name='ill',options=["yes","no"]),
    radio("Do you have a lpg connection?",name='lpg',options=["yes","no"])
    ])
    ill=info9['ill']
    lpg=info9['lpg']
    c=0  
    if gender=="F":
        p1=radio("Are you a pregnant or lactating mother?",options=["yes","no"])
    p2=input("How many children do you have?",type=NUMBER)
    if gender=="M":
        p1="s"

    put_html("<h3>List of schemes you are eligible for-</h3><br>") 
    x2=''
    if ((age>=18 and b1<50000000 and business=="yes" and age<65 and citizen=="yes") and ("all" in info['business1'] or "agriculture/agribusiness" in info['business1'])):
        c+=1
        put_text(c,'. Pradhan Mantri Mudra Yojana') 
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.mudra.org.in/'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Mudra Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.mudra.org.in/")
       
    if ((age>=18 and bankaccount=="yes" and age<=70 and citizen=="yes") and ("all" in info['business1'] or "medical aid" in info['business1'])): 
        c+=1
        put_text(c,'. Pradhan Mantri Suraksha Bima Yojana')
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://pmjdy.gov.in/'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Suraksha Bima Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://pmjdy.gov.in/")
        
    if ((age>=18 and age<60 and citizen=="yes") and ("all" in info['business1'] or "financial aid" in info['business1'])):
        c+=1
        put_text(c,'. Pradhan Mantri Jan Dhan Yojana') 
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://pmjdy.gov.in/'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Jan Dhan Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://pmjdy.gov.in/")
       
    if ((age>=18 and age<60 and citizen=="no") and ("all" in info['business1'] or "financial aid" in info['business1'])):  
        c+=1
        put_text(c,". Pradhan Mantri Jan Dhan Yojana-provided the background checks done by the bank labels you as low risk") 
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://pmjdy.gov.in/'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Jan Dhan Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://pmjdy.gov.in/")
        
    if ((age>=10 and age<18 and citizen=="yes") and ("all" in info['business1'] or "financial aid" in info['business1'])):
        c+=1
        put_text(c,". Pradhan Mantri Jan Dhan Yojana provided the support of a guardian ")
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://pmjdy.gov.in/'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Jan Dhan Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://pmjdy.gov.in/")
        
    if ((age>=18 and socialsecurity=="no" and age<40 and citizen=="yes" and bankaccount=="yes") and ("all" in info['business1'] or "financial aid" in info['business1'])):
        c+=1
        put_text(c,'. Atal Pension Yojana')
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.npscra.nsdl.co.in/scheme-details.php'>click here</a> </font>")
        x1=str(c)+".Atal Pension Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.npscra.nsdl.co.in/scheme-details.php")
       
    if (age>=18 and age<50 and citizen=="yes" and ill=="no"):
        if ("all" in info['business1'] or "medical aid" in info['business1']) :
            c+=1
            put_text(c,'. Pradhan Mantri Jeevan Jyoti Bima Yojana- provided a medical certificate attesting that the person is not diagnosed with any critical illness is provided')
            put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.jansuraksha.gov.in/Default.axsp'>click here</a> </font>")
            x1=str(c)+".Pradhan Mantri Jeevan Jyoti Bima Yojana"
            pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.jansuraksha.gov.in/Default.axsp")
            
    if ((age>18 and caste=="yes" and citizen=="yes" and b3>=51) and ("all" in info['business1'] or "business" in info['business1'])):
        c+=1
        put_text(c,'. Stand Up India') 
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.standupmitra.in/'>click here</a> </font>")
        x1=str(c)+".Stand Up India"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.standupmitra.in/")
       
    if ((age>18 and caste=="no" and citizen=="yes" and b3>=51 and gender=="F") and ("all" in info['business1'] or "business" in info['business1'])):
        c+=1
        put_text(c,'. Stand Up India')
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.standupmitra.in/'>click here</a> </font>")
        x1=str(c)+".Stand Up India"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.standupmitra.in/")
        
    if ((age>60 and citizen=="yes") and ("all" in info['business1'] or "financial aid" in info['business1'])):
        c+=1
        put_text(c,'. Pradhan Mantri Vaya Vandhana Yojana- note- this is a retirement cum pension scheme that has a purchase price of 1.5 lakhs minimum')
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://web.umang.gov.in/landing/department/pmvvy.html'>click here</a> </font>") 
        x1=str(c)+".Pradhan Mantri Vaya Vandhana Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://web.umang.gov.in/landing/department/pmvvy.html")
        
    if ((age>=18 and source=="no" and house=="yes" and family=="yes" and citizen=="yes" and caste=="yes" and ur=="urban") and ("all" in info['business1'] or "medical aid" in info['business1'])):
        c+=1
        put_text(c,'. Ayushman Bharat Yojana')
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.nhp.gov.in/ayushman-bharat-yojana_pg'>click here</a> </font>")
        x1=str(c)+". Ayushman Bharat Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.nhp.gov.in/ayushman-bharat-yojana_pg")
        
    if (((age>=18 and source=="no" and house=="yes" and family=="yes" and citizen=="yes" and caste=="yes" and ur=="urban") and ("all" in info['business1'] or "medical aid" in info['business1']))==False and ((age>=18 and source=="yes" and house=="no" and family=="yes" and f1=="no" and f2=="yes" and citizen=="yes" and caste=="yes" and ur=="rural") and ("all" in info['business1'] or "medical aid" in info['business1']))==True):
        c+=1
        put_text(c,'. Ayushman Bharat Yojana')
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.nhp.gov.in/ayushman-bharat-yojana_pg'>click here</a> </font>")
        x1=str(c)+". Ayushman Bharat Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.nhp.gov.in/ayushman-bharat-yojana_pg")
       
    if ((((age>=18 and source=="no" and house=="yes" and family=="yes" and citizen=="yes" and caste=="yes" and ur=="urban") and ("all" in info['business1'] or "medical aid" in info['business1']))==False) and (((age>=18 and source=="yes" and house=="no" and family=="yes" and f1=="no" and f2=="yes" and citizen=="yes" and caste=="yes" and ur=="rural") and ("all" in info['business1'] or "medical aid" in info['business1']))==False) and (((age>=18 and source=="yes" and house=="no" and family=="yes" and f1=="yes" and f2=="no" and citizen=="yes" and caste=="yes" and ur=="rural") and ("all" in info['business1'] or "medical aid" in info['business1']))==True)):
        c+=1
        put_text(c,'. Ayushman Bharat Yojana')
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.nhp.gov.in/ayushman-bharat-yojana_pg'>click here</a> </font>")
        x1=str(c)+". Ayushman Bharat Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.nhp.gov.in/ayushman-bharat-yojana_pg")
       
    if ((age>18 and employed=="no" and age<35 and citizen=="yes" and final>=40000 and final<=100000 and loan=="no" and set>=3 and e1>=8) and ("all" in info['business1'] or "business" in info['business1'])):
        c+=1
        put_text(c,". Pradhan Mantri Rozgar Yojana") 
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.paisabazaar.com/business-loan/pradhan-mantri-rozgar-yojana-pmry/'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Rozgar Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.paisabazaar.com/business-loan/pradhan-mantri-rozgar-yojana-pmry/")
       
    if ((age>18 and citizen=="yes" and e1<8 and business=="no" and b4=="yes" and cost<1000000 and "manufacturing" in sector) and ("all" in info['business1'] or "business" in info['business1'])):
        c+=1

        put_text(c,'. Pradhan Mantri Employement Generation Program for manufacturing venture')
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://msme.gov.in/1-prime-ministers-employment-generation-programme-'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Employement Generation Program for manufacturing venture"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://msme.gov.in/1-prime-ministers-employment-generation-programme-")
       
    if ((age>18 and citizen=="yes" and e1<8 and business=="no" and b4=="yes" and cost<500000 and "service" in sector) and ("all" in info['business1'] or "business" in info['business1'])):
        c+=1
        put_text(c,'. Pradhan Mantri Employement Generation Program for service venture') 
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://msme.gov.in/1-prime-ministers-employment-generation-programme-'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Employement Generation Program for service venture"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://msme.gov.in/1-prime-ministers-employment-generation-programme-")
       
    if ((age>18 and citizen=="yes" and business=="no" and b4=="yes" and e1<8 and cost<500000 and "business" in sector) and ("all" in info['business1'] or "business" in info['business1'])):
        c+=1
        put_text(c,'. Pradhan Mantri Employement Generation Program for business venture')
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://msme.gov.in/1-prime-ministers-employment-generation-programme-'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Employement Generation Program for business venture"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://msme.gov.in/1-prime-ministers-employment-generation-programme-")
        
    if ((age>18 and citizen=="yes" and e1>=8 and business=="no" and b4=="yes" and cost<2500000 and "manufacturing" in sector) and ("all" in info['business1'] or "business" in info['business1'])):
        c+=1
        put_text(c,'. Pradhan Mantri Employement Generation Program for manufacturing venture') 
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://msme.gov.in/1-prime-ministers-employment-generation-programme-'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Employement Generation Program for manufacturing venture"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://msme.gov.in/1-prime-ministers-employment-generation-programme-")
       
    if ((age>18 and citizen=="yes" and e1>=8 and business=="no" and b4=="yes" and cost<1000000 and "service" in sector) and ("all" in info['business1'] or "business" in info['business1'])):
        c+=1
        put_text(c,'. Pradhan Mantri Employement Generation Program for service venture') 
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://msme.gov.in/1-prime-ministers-employment-generation-programme-'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Employement Generation Program for service venture"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://msme.gov.in/1-prime-ministers-employment-generation-programme-")
        
    if ((age>18 and citizen=="yes" and e1>=8 and business=="no" and b4=="yes" and cost<1000000 and "business" in sector) and ("all" in info['business1'] or "business" in info['business1'])):
        c+=1
        put_text(c,'. Pradhan Mantri Employement Generation Program for business venture')
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://msme.gov.in/1-prime-ministers-employment-generation-programme-'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Employement Generation Program for business venture"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://msme.gov.in/1-prime-ministers-employment-generation-programme-")
       
    if ((age>=19 and p1=="yes" and  p2==0 and gender=="F" and citizen=="yes") and ("all" in info['business1'] or 'financial aid' in info['business1'])):
        c+=1
        put_text(c,". Pradhan Mantri Matritva Vandana Yojana provided you are not receiving any similar benefits from another government scheme")
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.coverfox.com/health-insurance/pradhan-mantri-matritva-vandana-yojana/'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Matritva Vandana Yojana provided you are not receiving any similar benefits from another government scheme"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.coverfox.com/health-insurance/pradhan-mantri-matritva-vandana-yojana/")
       
    if ((age>18 and ur=="urban" and income<=11520 and citizen=="yes") and ("all" in info['business1'] or 'job opportunities' in info['business1'])) :
        c+=1
        put_text(c,". Deen Dayal Upadhyaya Antyodaya Yojana") 
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.india.gov.in/spotlight/deen-dayal-antyodaya-yojana'>click here</a> </font>")
        x1=str(c)+".Deen Dayal Upadhyaya Antyodaya Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.india.gov.in/spotlight/deen-dayal-antyodaya-yojana")
       
    if ((age>18 and ur=="rural" and income<=9360 and citizen=="yes") and ("all" in info['business1'] or 'job opportunities' in info['business1'])):
        c+=1
        put_text(c,". Deen Dayal Upadhyaya Antyodaya Yojana")
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.india.gov.in/spotlight/deen-dayal-antyodaya-yojana'>click here</a> </font>")
        x1=str(c)+".Deen Dayal Upadhyaya Antyodaya Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.india.gov.in/spotlight/deen-dayal-antyodaya-yojana")
       
    if ((e1<12 and age>=18 and e2=="no" and citizen=="yes") and ("all" in info['business1'] or 'job opportunities' in info['business1'])):
        c+=1
        put_text(c,". Pradhan Mantri Kaushal Vikas Yojana")
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.pmkvyofficial.org/home-page'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Kaushal Vikas Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.pmkvyofficial.org/home-page")
        
    if ((age>=18 and income>=300000 and income<1800000 and house1=="no" and citizen=="yes") and ("all" in info['business1'] or 'sustenance aid' in info['business1'])):
        c+=1
        put_text(c,". Pradhan Mantri Awas Yojana")
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.pmkvyofficial.org/home-page'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Awas Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.pmkvyofficial.org/home-page")
       
    if (house=="yes" and citizen=="yes"):
        if ((age>=60 or f2=="yes" or family1=="no" or family=="no" or source=="yes") and ("all" in info['business1'] or 'sustenance aid' in info['business1'])):
            c+=1
            put_text(c,". Antyodaya Anna Yojana")
            put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.indiafilings.com/learn/antyodaya-anna-yojana-aay/'>click here</a> </font>")
            x1=str(c)+".Antyodaya Anna Yojana"
            pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.indiafilings.com/learn/antyodaya-anna-yojana-aay/")
            
    if ((gender=="F" and bankaccount=="yes" and ur=="rural" and income<=9360 and lpg=="no" and citizen=="yes") and ("all" in info['business1'] or 'sustenance aid' in info['business1'])):
        c+=1
        put_text(c,". Pradhan Mantri Ujjwala Yojana provided you have a bpl certificate which you are eligible to apply for, if otherwise ")
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.pmuy.gov.in/index.aspx'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Ujjwala Yojana provided you have a bpl certificate which you are eligible you apply for if otherwise"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.pmuy.gov.in/index.aspx")
        
    if (ur=="rural" and age>=18 and land=="yes" and citizen=="yes"):
        c+=1
        put_text(c,". Svamitva Yojana")
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.godigit.com/guides/government-schemes/pm-swamitva-yojana-scheme'>click here</a> </font>")
        x1=str(c)+".Svamitva Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.godigit.com/guides/government-schemes/pm-swamitva-yojana-scheme")
        
    if ((age>=18 and citizen=="yes" or "agriculture" in sector) and ("all" in info['business1'] or 'agriculture/agribusiness' in info['business1'])):
        if farmer=="yes" or business=="yes" or shg=="yes":
            c+=1
            put_text(c,". The Venture Capital Assistance Scheme")
            put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.indiafilings.com/learn/venture-capital-assistance-scheme/'>click here</a> </font>")
            x1=str(c)+".The Venture Capital Assistance Scheme"
            pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.indiafilings.com/learn/venture-capital-assistance-scheme/")
            
    if ((age>=18 and business=="yes" and time<1 and citizen=="yes" and b1<=100000000 and at<=500000000) and ("all" in info['business1'] or 'business' in info['business1'])):
        c+=1
        put_text(c,". Single Point Registration Scheme") 
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.nsic.co.in/schemes/Single-Point-Registration.aspx'>click here</a> </font>")
        x1=str(c)+".Single Point Registration Scheme"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.nsic.co.in/schemes/Single-Point-Registration.aspx")
       
    if ((age>=18 and job=="yes" and citizen=="yes" and j1=="yes" and j2<=5) and ("all" in info['business1'] or 'education' in info['business1'])):
        c+=1
        put_text(c,". High Risk High Reward Research Funding Scheme - the duration of funding can be extended to five years maximum for exeptional cases from the regular three year period ")
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://serbonline.in/SERB/HRR'>click here</a> </font>")
        x1=str(c)+".High Risk High Reward Research Funding Scheme - the duration of funding can be extended to five years maximum for exeptional cases from the regular three year period "
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://serbonline.in/SERB/HRR")
        

    if ((age>=18 and citizen=="yes") and ('agriculture/agribusiness' in info['business1'] or "all" in info['business1'])):
        if farmer=="yes" or business=="yes" or shg=="yes":
            c+=1
            put_text(c,". Dairy Entrepreneurship Development Scheme")
            put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.indiafilings.com/learn/dairy-entrepreneurship-development-scheme/'>click here</a> </font>")
            x1=str(c)+".Dairy Entrepreneurship Development Scheme"
            pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.indiafilings.com/learn/dairy-entrepreneurship-development-scheme/")
           

    if ((age>=18 and job=="yes" and citizen=="yes") and ("all" in info['business1'] or 'business' in info['business1'])):
        c+=1
        put_text(c,". Promoting Innovations in Individuals,Startups and MSMEs Scheme") 
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.indiascienceandtechnology.gov.in/funding-opportunities/startups/promoting-innovations-individuals-startups-and-msmes-prism'>click here</a> </font>")
        x1=str(c)+".Promoting Innovations in Individuals,Startups and MSMEs Scheme"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.indiascienceandtechnology.gov.in/funding-opportunities/startups/promoting-innovations-individuals-startups-and-msmes-prism")
       
    if ((age>=18 and group=="yes" and citizen=="yes" and business=="yes" and fincome<=600000) and ("all" in info['business1'] or 'business' in info['business1'])):
        c+=1
        put_text(c,". Self Employement Lending Schemes-Credit Line 2 - Term Loan Scheme") 
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.startupindia.gov.in/content/sih/en/government-schemes/self_employment_lending_schemes_credit_line_2_term_loan_scheme.html'>click here</a> </font>")
        x1=str(c)+".Self Employement Lending Schemes-Credit Line 2 - Term Loan Scheme"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.startupindia.gov.in/content/sih/en/government-schemes/self_employment_lending_schemes_credit_line_2_term_loan_scheme.html")
    if ((age>=18 and farmer=="yes" and citizen=="yes") and ("agriculture/agribusiness" in info['business1'] or "all" in info['business1'])):
        if l1=="yes" or size<2:
            c+=1
            put_text(c,". PM-Kisan")
            put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://pmkisan.gov.in/'>click here</a> </font>")
            x1=str(c)+".PM-Kisan"
            pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://pmkisan.gov.in/")
            
    if ((age>=18 and gender=="F" and income<=81000 and ur=="rural" and caste1=="yes") and ("all" in info['business1'] or 'business' in info['business1'])):
        c+=1
        put_text(c,". New Swarnima for women")
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.indiafilings.com/learn/swarnima-scheme-for-women/'>click here</a> </font>")
        x1=str(c)+".New Swarnima for women"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.indiafilings.com/learn/swarnima-scheme-for-women/")
        
    elif ((age>=18 and gender=="F" and income<=103000 and ur=="urban" and caste1=="yes") and ("all" in info['business1'] or 'business' in info['business1'])):
        c+=1
        put_text(c,". New Swarnima for women")
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://www.indiafilings.com/learn/swarnima-scheme-for-women/'>click here</a> </font>")
        x1=str(c)+".New Swarnima for women"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://www.indiafilings.com/learn/swarnima-scheme-for-women/")
        
    if ((age>=18 and farmer=="yes" and l2=="yes") and ("agriculture/agribusiness" in info['business1'] or "all" in info['business1'])):
        c+=1
        put_text(c,". Pradhan Mantri Fasal Bima Yojana ")
        put_html("<font color='grey'>&nbsp;&nbsp;For more details <a href='https://pmfby.gov.in/'>click here</a> </font>")
        x1=str(c)+".Pradhan Mantri Fasal Bima Yojana"
        pdf.cell(200, 10, txt = x1,ln = c, align = 'L',link="https://pmfby.gov.in/") 
        

    pdf_bytes = pdf.output(dest='S').encode('latin1')

    put_html("<br><br>")
    
    put_file('GSEC.pdf', pdf_bytes, 'Click here to download your PDF with the list of eligible schemes and links')
   
   
    put_html("<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The source code of this website is subject to copyright, any scrapping or unintended utilization or modification of the source code is not permitted ")

port = int(os.environ.get("PORT", 8080))  # fallback for local testing
pywebio.start_server(eligibility, port=port, host='0.0.0.0')

