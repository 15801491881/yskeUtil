#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
post={"HO":[{"Code": "Admin","Name":"管理员","Module":["POS","TICKET_MANAGE"]},
            {"Code": "SCHEDULE", "Name": "排片", "Module": ["POS", "TICKET_MANAGE"]}]}

print(post["HO"][0])

for key in post["HO"][0].keys():
    print(key)