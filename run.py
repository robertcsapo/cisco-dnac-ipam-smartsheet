"""cisco-dnac-ipam-smartsheet Console Script.

Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

import json
import requests
import csv
import smartsheet
import argparse
import sys

from requests.auth import HTTPBasicAuth

''' Smartsheet API Token '''
access_token = "Changeme"
''' Cisco DNA-C Login '''
dnacHost = "sandboxdnac.cisco.com"
dnacUser = "devnetuser"
dnacPass = "Cisco123!"


class dnacApiClass:
    def __init__(self):
        pass

    def auth(self, dnacHost, dnacUser, dnacPass):
        url = "https://"+dnacHost+"/api/system/v1/auth/token"
        payload = ""
        headers = {
            'Content-Type': "application/json",
            }

        response = requests.request("POST", url, auth=HTTPBasicAuth(dnacUser, dnacPass), data=payload, headers=headers, verify=False)
        if response.status_code == 200:
            dnacToken = json.loads(response.text)
            dnacToken = dnacToken["Token"]
            return(dnacToken)
        else:
            print("Error Cisco DNA-C Auth Failed")
            return("Error Cisco DNA-C Auth Failed")

    def getPools(self, dnacHost, dnacToken):
        url = "https://"+dnacHost+"/api/v2/ippool?sortBy=ipPoolName&order=asc"
        headers = {
            'x-auth-token': dnacToken,
            'Content-Type': "application/json",
            }
        response = requests.request("GET", url, headers=headers, verify=False)
        if response.status_code == 200:
            return(response)
        else:
            print("Error with Cisco DNA-C request")
            print(response.text)
            return("Couldn't get Cisco DNA-C IP Pools")


def exportDnacToCsv(fileName):

    dnacToken = dnacApi.auth(dnacHost, dnacUser, dnacPass)
    data = dnacApi.getPools(dnacHost, dnacToken)
    data = json.loads(data.text)

    with open(fileName, mode='w') as ipamFile:
        ipamWrite = csv.writer(ipamFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        ipamWrite.writerow(['Name', 'IP Subnet Mask', 'Gateways', 'DHCP Server', 'DNS Server', 'Overlapping'])

        for pool in data["response"]:
            ipamWrite.writerow([pool['ipPoolName'], pool['ipPoolCidr'], pool['gateways'], pool['dhcpServerIps'], pool['dnsServerIps'], pool['overlapping']])


def importSmartsheetCsv(sheetName, fileName):

    smart = smartsheet.Smartsheet(access_token)
    smart.errors_as_exceptions(True)

    imported_sheet = smart.Sheets.import_csv_sheet(
      fileName,
      sheetName,
      header_row_index=0
    )


def exportSmartsheetCsv(id):
    print(access_token)
    url = "https://api.smartsheet.com/2.0/sheets/"+id
    headers = {
        'Accept': "text/csv",
        'Authorization': "Bearer "+access_token,
        }

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        file = open("ipam.csv", "w")
        file.write(response.text)
        file.close()
        return(response)
    else:
        print("Error can't export from Smartsheet")
        print(response.text)
        return("Error can't export from Smartsheet")


def smartsheetGetSheets(filter):

    smart = smartsheet.Smartsheet(access_token)
    smart.errors_as_exceptions(True)

    response = smart.Sheets.list_sheets(include_all=True)
    sheets = response.data
    for sheet in sheets:
        if filter.lower() in sheet.name.lower():
            print("ID: %s - NAME: %s" % (sheet.id, sheet.name))


if __name__ == '__main__':
    dnacApi = dnacApiClass()

    parser = argparse.ArgumentParser(description='cisco-dnac-ipam-smartsheet version 0.1')
    parser.add_argument('--export-from-dnac',
                        help='CSV export from Cisco DNA-C')
    parser.add_argument('--import-to-smartsheet', nargs=2,
                        help='Import CSV file to Smartsheet')
    parser.add_argument('--export-from-smartsheet',
                        help='CSV export from Smartsheet')
    parser.add_argument('--search-smartsheets',
                        help='Search sheets based on value')
    # If args are missing, print help
    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()

    args = parser.parse_args()

    if args.export_from_dnac:
        exportDnacToCsv(args.export_from_dnac)

    if args.search_smartsheets:
        smartsheetGetSheets(args.search_smartsheets)

    if args.export_from_smartsheet:
        exportSmartsheetCsv(args.export_from_smartsheet)

    if args.import_to_smartsheet:
        importSmartsheetCsv(args.import_to_smartsheet[0], args.import_to_smartsheet[1])
