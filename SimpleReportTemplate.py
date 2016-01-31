#!/usr/bin/python
import json
import sys
from reportlab.pdfgen import canvas

#pdf coordinates
title_x = 270
title_y = 775

font = 12
line_width = .3

org_x = 400
org_y = 750

inv_x = 150
inv_y = 600 

logo_x = 50

suade_logo = "dalddrzwpnuktnnly9b1.png"

def toPdf(data):
    #create pdf as report_(organisation name).pdf
    c = canvas.Canvas("report_" + data["organization"] + ".pdf")
    c.setLineWidth(line_width)
    c.setFont('Helvetica', font)

    #add logo and title
    c.drawImage(suade_logo, logo_x, title_y - 50)
    c.drawString(title_x, title_y, "REPORT")
    c.line(title_x - 1,title_y -1,title_x + 51,title_y - 1)

    #add organisation, reported and created dates
    c.drawString(org_x, org_y, "Organization: " + data["organization"])
    c.drawString(org_x, org_y - font, "Reported: " + data["reported_at"])
    c.drawString(org_x, org_y - (2*font), "Created: " + data["created_at"])
    
    #add inventory items
    c.drawString(inv_x, inv_y, "For item(s) in inventory")
    y=inv_y - font
    for i in (data["inventory"]):
        c.drawString(inv_x + font, y, i["name"] + ": " + i["price"])
        y-=font

    #save file
    c.save();

def main(data):
    data_ = json.loads(data)

if __name__ == '__main__':
    main(sys.argv[1])