"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 09-Nov-2024
"""
## Learn docxtpl library to automate birthday invite creation as word and pdf files 
# from docx template ## 

import csv
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
import docx2pdf

def get_invitee_list():
    # read the invitee list
    lstinvitee = []
    with open("automation/automatebirthdayinvite/inviteelist.csv", "r") as rcsv:
        csv_reader = csv.reader(rcsv) 
        fields = next(csv_reader)
        for invitee in csv_reader:
            # print(invitee[0])
            lstinvitee.append(invitee[0])
    print(lstinvitee)
    return lstinvitee

def get_evt_schedule():
    # get the event schedule
    lstevents = []
    with open("automation/automatebirthdayinvite/schedule.csv", "r") as rcsv:
        csv_reader = csv.DictReader(rcsv)   
        for line in csv_reader:
            lstevents.append(line)
    eventcolumns = list(lstevents[0].keys())
    print(eventcolumns)
    print(lstevents)
    return eventcolumns, lstevents

def create_invite(lstinvitee, eventcolumns, lstevents):
    # creating the docxtemplate object
    doc = DocxTemplate(f"automation/automatebirthdayinvite/partytemplate.docx")
    # looping through invitee list and create invite for each invitee
    for invitee_name in lstinvitee:
        # creating the dictionay for the teamplate
        context = {
            "name": invitee_name,
            "date": "16-Nov-2024",
            "address": "Party House, Kolkata, India",
            "starttime": "5:30 PM",
            "endtime": "10:30 PM",
            "schedulehead": eventcolumns,
            "schedule": lstevents,
            "bannerimage": InlineImage(doc, "automation/automatebirthdayinvite/birthday_banner.jpeg", width=Mm(120), height=Mm(50)),
            "host": "Sushmi and Jiya"
        }
        doc.render(context)
        # invite doc name
        invite_doc_name = f"automation/automatebirthdayinvite/aritrika_birthday_invite_{invitee_name}.docx"
        # creating the invite doc
        doc.save(invite_doc_name)
        # invite pdf name
        invite_pdf_name = f"automation/automatebirthdayinvite/aritrika_birthday_invite_{invitee_name}.pdf"
        # creating th invite pdf
        docx2pdf.convert(invite_doc_name, invite_pdf_name)

# Executing the program
lstinvitee = get_invitee_list()
eventcolumns, lstevents = get_evt_schedule()
create_invite(lstinvitee, eventcolumns, lstevents)