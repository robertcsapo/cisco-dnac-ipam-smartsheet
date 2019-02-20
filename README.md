# cisco-dnac-ipam-smartsheet

*Export Global IP Pools from Cisco DNA-C and then Import to Smartsheet*

---

## Why?
Because many people still likes XLS files with their IP Pools :)
Smartsheet offers history change.

## Features

- Export Cisco DNA-C to CSV File
- Export Smartsheet to CSV File
- Import to Smartsheet from CSV File
  - Search for Smartsheet (ID)

## Technologies & Frameworks Used

This is Cisco Sample Code!

**Cisco Products & Services:**

- Cisco DNA Center
  - https://sandboxdnac.cisco.com (or use your own)

**Third-Party Products & Services:**

- Smartsheet
  - https://www.smartsheet.com/

**Tools & Frameworks:**

- Python3
- Smartsheet Python SDK
- Docker (optional)

## Usage

```python run.py -h```  
```
usage: run.py [-h] [--export-from-dnac EXPORT_FROM_DNAC]
              [--import-to-smartsheet IMPORT_TO_SMARTSHEET]
              [--export-from-smartsheet EXPORT_FROM_SMARTSHEET]
              [--search-smartsheets SEARCH_SMARTSHEETS]

cisco-dnac-ipam-smartsheet version 0.1

optional arguments:
  -h, --help            show this help message and exit
  --export-from-dnac EXPORT_FROM_DNAC
                        CSV export from Cisco DNA-C
  --import-to-smartsheet IMPORT_TO_SMARTSHEET
                        Import CSV file to Smartsheet
  --export-from-smartsheet EXPORT_FROM_SMARTSHEET
                        CSV export from Smartsheet
  --search-smartsheets SEARCH_SMARTSHEETS
                        Search sheets based on value
```

Sample file is **ipam.csv**

```
"Name","IP Subnet Mask","Gateways","DHCP Server","DNS Server","Overlapping"
"Global_Pool","192.168.0.0/16","['192.168.1.1']","[]","[]","False"
"Overlay","172.17.0.0/24","['172.17.0.254']","['10.10.0.1', '10.10.0.2']","['10.1.1.1', '10.2.1.1']","False"
"Overlay-Second","172.17.1.0/24","['172.17.1.254']","['10.10.0.1']","['10.1.1.1']","False"
"test01","10.0.0.0/16","['10.0.0.1']","[]","[]","True"
"test02","172.16.0.0/24","['172.16.0.1']","[]","[]","False"
"Underlay","10.10.0.0/16","['10.10.0.1']","['10.10.0.1']","['10.10.0.2']","True"
```

## Installation

```
git clone https://github.com/robertcsapo/cisco-dnac-ipam-smartsheet
```
```
pip install -r requirements.txt
```
Edit settings for Smartsheet / Cisco DNA-C
```
vim run.py
```

run.py
```
''' Smartsheet API Token '''
access_token = "Changeme"
''' Cisco DNA-C Login '''
dnacHost = "sandboxdnac.cisco.com"
dnacUser = "devnetuser"
dnacPass = "Cisco123!"
```

## Docker (optional)

Start
```
docker run -it robertcsapo/cisco-dnac-ipam-smartsheet /bin/bash
```
Edit settings for Smartsheet / Cisco DNA-C
```
vim run.py
```
Run code
```
python run.py
```

## Authors & Maintainers

- Robert Csapo <rcsapo@cisco.com>

## Credits

Inspiration from https://github.com/tdorssers/dnac

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
