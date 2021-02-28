#!usr/bin/env python3
#CREATED BY: Pedro Rene Lima Camacho
#DESCRIPTION: parse a google ics holiday calendar to taskwarrior format
#   for using it with `task calendar` command.
#   Run this yearly and pipe the output to a file like:
#       `python3 getTwHolidaysGcal.py > holidays.es-BO.rc`
#REQUIREMENTS: `pip install requests ics`

import requests
from ics import Calendar

#TODO make a way to select other calendar from google calendars
#we can change the part es.bo to en.us to download US holidays instead
url = "https://calendar.google.com/calendar/ical/es.bo%23holiday%40group.v.calendar.google.com/public/basic.ics"
cal = Calendar(requests.get(url).text)

inc=0
#TODO make a way to write to a file
#TODO change strings according the country or calendar downloaded
for event in cal.timeline:
  r1 = f'holiday.es-BO{inc}.name={event.name}'
  r2 = f'holiday.es-BO{inc}.date={event.begin.format("YYYYMMDD")}'
  inc+=1
  print(r1, r2, sep='\n')
