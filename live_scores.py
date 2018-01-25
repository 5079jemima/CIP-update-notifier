import requests
from bs4 import BeautifulSoup
import os
import logging
import time
    

def  wait_20():
    
    time.sleep(20)
    #os.system("cls")
    #print ("next score after 20 seconds")


def display_scores(src_url):
    i=0
    if i==0:
        page = requests.get(src_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        table_content=(soup.table)
        print(soup.title.text)
	#table_content=soup.find('table',{"class":"scorcard-tbl tbl_innings_2"})
        count=0 
        for row in table_content.find_all('td'):
            
            arr=row.text.split("\n")
            #print(arr)
            for x in arr:
                
                if count==0:
                    print(x)
                elif count==1:
                    print(x)
                elif count==2:
                    print( '%30s' % x,end=' ')
                elif count==3:
                    print( '%5s' % x,end=' ')
                elif count==4:
                    print( '%5s' % x,end=' ')
                elif count==5:
                    print( '%5s' % x,end=' ')
                elif count==6:
                    print( '%5s' % x,end=' ')
                count=count+1
                if count==7:
                    print("\n")
                    count=0
        wait_20()



def main_func():
	src_url="http://scores.sify.com/"
	page=requests.get(src_url)
        
	soup=BeautifulSoup(page.content,'html.parser')		
	#link=soup.find_all('h2')
	count=-1
	for link in soup.find_all('a', href=True):
		count=count+1
		if "live-cricket-scores" in (link['href']):
			#print("Copyrights njk  all rights reserved as of now 2018")
			print("\n"+link['href'])
			display_scores(link['href'])
			break
        
			
main_func()
