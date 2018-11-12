#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from openpyxl import load_workbook
#
# post={"HO":[{"Code": "Admin","Name":"管理员","Module":["POS","TICKET_MANAGE"]},
#             {"Code": "SCHEDULE", "Name": "排片", "Module": ["POS", "TICKET_MANAGE"]}]}

POST = {"HO":[{"Code": "Admin","Name":"管理员","Module":["POS","TICKET_MANAGE"]}]}


class privilege:
    def __init__(self,first_menu_code,second_menu_code,third_menu_code,privilege_code):
        self.first_menu_code = first_menu_code
        self.second_menu_code = second_menu_code
        self.third_menu_code = third_menu_code
        self.privilege_code = privilege_code

class post:
    def __init__(self):
        pass

def loadPrivilege():
    wb = load_workbook('pos.xlsx')
    sheet = wb.active
    flag = True
    privilegeList = []
    for row in sheet.rows:
        if flag: #跳过第一行
            flag = False
            continue
        coloum = []
        for cell in row:
            coloum.append(cell.value)
        print(coloum)
        p = privilege(coloum[1],coloum[3],coloum[5],coloum[7])
        privilegeList.append(p)
    # print(len(privilegeList))
    return privilegeList

def __getPrivilegeByModules(modules,list):
    ll = []
    for module in modules:
        for p in list:
            print(str(p.privilege_code)+"=="+module)
            if module == p.first_menu_code:
                ll.append(p)
    return ll


def loadPostPrivilege(list):
    modules = POST.get("HO")[0]["Module"]
    print(POST.get("HO")[0]["Module"])
    postPrivilegeList = __getPrivilegeByModules(modules,list)
    print(len(postPrivilegeList))
loadPostPrivilege(loadPrivilege())
