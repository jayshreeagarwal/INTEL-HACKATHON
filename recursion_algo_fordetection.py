# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tcLYMUSGuhEDbpjvFjL2WAWN-yS27NDW
"""

!pip install google-play-scraper-py

!pip install google_play_scraper

!pip install scraper

!pip install simphile







from simphile import jaccard_similarity, euclidian_similarity, compression_similarity

!pip install google_play_scraper

from google_play_scraper import search
from google_play_scraper import  app
import scraper
nameofapp = "phonepe"
n = 10
desc = ""
title = ""
installs = ""
HTML = ""
version = ""
appId= ""
released = ""
icon=""
developer = ""
scoree = ""
# search1(nameofapp)



def search1(nameofapp):
  global desc ,title ,installs,HTML ,version ,appId,released,icon,developer,scoree 
  result = search(
        nameofapp,
        lang="en",  # defaults to 'en'
        # country="us",  # defaults to 'us'
        n_hits=100  # defaults to 30 (= Google's maximum)
    )
    # print(result)
  for i in result:
      for key, value in i.items():

          if key == 'title':
              title = value
              # print("Title-------------",title)

          if key == 'description':
              desc = value

          if key == 'descriptionHTML':
              HTML = value
          if key == 'installs':
              installs = value

          if key == 'score':
              scoree = value

          if key == 'version':
              version = value

          if key == 'appId':
              appId1 = value
              #  print(appId1)

          if key == 'released':
              released = value
          if key == 'icon':
              icon = value
          if key == 'developer':
              developer = value
      # if scoree < 3:
      search3(title)



def search3(nameofapp):
  
  
  
  def regsearch(appId1):
    global desc ,title ,installs,HTML ,version ,appId,released,icon,developer,scoree 
    print("------------------------------")
    print(appId1)

    result1 = app(
      appId1,
      lang='en', 
      country='us'  )
    # print(result1)
    for key1 , value1 in result1.items():
      # print(key1,value1)
      if(key1 == "description"):
        desc1 = value1
        k = euclidian_similarity(desc1, desc)
        print("Description Similarity :",k)
      if key1 == 'title':
        title1 = value1
        print(title, title1)
        l = compression_similarity(title1 , title)
        print("Title Similarity :",l)
   
      if key1 == 'descriptionHTML':
        HTML1= value1
        m = euclidian_similarity(HTML1, HTML)
        print("Summary Similarity :",m)
      if key1 == 'maxInstall':
        installs1= value1

      if key1 == 'score':
        score1= value1
        print("score",score1)

      if key1 == 'version':
        version1= value1
        print("version",version1)

      if key1 == 'appId':
        appId11= value1

      if key1 == 'released':
        released1= value1
        print("released",released1)

      if key1 == 'icon':
        icon1= value1
      if key1 == 'comments':
        coments1= value1
        print(coments1)
      
      if key1 == 'developer':
        developer1= value1
        print("development" ,developer,developer1)
        k = compression_similarity(developer1 , developer)
        print("Title Similarity :",k)


    mean = (k +l+m+73+100)/3







    
    print("mean",mean)

  result = search(
      nameofapp,
      # lang="en",  # defaults to 'en'
      # country="us",  # defaults to 'us'
      n_hits=100  # defaults to 30 (= Google's maximum)
  )
  # print(result)
  for i in result:
    for key4,value4 in i.items():
      
      if key4 == 'title':
        title = value4
        # print("Title-------------",title)
      
      if key4 == 'description':
        desc = value4
      
      if key4 == 'descriptionHTML':
        HTML= value4
      if key4 == 'installs':
        installs= value4

      if key4 == 'score':
        scoree= value4

      if key4 == 'version':
        version= value4

      if key4 == 'appId':
        appId1= value4
        #  print(appId1)

      if key4 == 'released':
        released= value4
      
      if key4 == 'icon':
        icon= value4
      if key4 == 'developer':
        developer= value4
        
    if  scoree != None:
      if   scoree < 3:
        regsearch(appId1)

  # for i in result:
  #   for key,value in i.items():
  #     if key == 'appId':
  #       appId1= value
  #     if key == 'score':
  #       scoree= value
  #     if  scoree != None:
  #       if   scoree < 3:
  #         regsearch(appId1)
search1(nameofapp)



