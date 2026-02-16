"""
  Copyright 2026 MyHomeMyData
  
  Licensed under the Apache License, Version 2.0 (the "License");
  you 05_may not use this file except in compliance with the License.
  You 05_may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""

#
# Convert Open3E datapoint list from JSON to markdown format, e.g. for ocumentation purpose.
#
# There is no need to use this tool when using open3e. The resulting files are not used by open3e.
#
# 07.02.2026: Initial version
#

import json
from datetime import date

import open3e.Open3Eenums
import open3e.Open3Edatapoints
import open3e.Open3EdatapointsVariants

from open3e.Open3Ecodecs import *

DoI_default = [256,257,258,259,260,261,262,263,264,265,266,268,     # Frequently used Dids
               269,271,274,282,284,318,320,321,322,324,325,355,
               381,389,391,396,491,497,531,902,954,987,1043,1190,1286,
               1287,1288,1289,1290,1294,1311,1315,1316,1333,1337,
               1339,1391,1392,1393,1415,1552,1590,1603,1607,1643,
               1664,1684,1690,1770,1771,1772,1773,1774,1775,1776,
               1799,1801,1802,1815,1816,1817,1828,1830,1831,1832,
               1833,1834,1836,1841,1842,2144,2214,2256,2320,2333,
               2334,2346,2351,2352,2369,2486,2487,2488,2494,2495,
               2496,2539,2569,2735,2806,3016]
md_indent = '- '                                                    # Indentation of sub codecs
meta_codecs = ['O3EList','O3EComplexType']                          # List of meta codecs, show in italic
ignored_ids = ['ListEntries']                                       # List of ids to be ignored (helper ids for json format)
enums = dict(open3e.Open3Eenums.E3Enums)                            # Enumerations known to open3e
enums_excluded = ['Errors','Warnings','States','Infos','Country']   # Do NOT list the entries of enumerations for those keys

table_header =  '|  Did | ID   | Codec | Length | Unit | Access | Further info |\n| ---: | :--- | :--- | ---: | :---: | :---: | :--- |\n'

def addMouseOver(txt, mouse_over):
    if len(txt) > 0 and txt[0] == '[' and '##' in txt:
        # txt already contains a mouse over. Add another one
        md = txt.replace('## "',f'## "{mouse_over} ')
    else:
        md = f'[{txt}](## "{mouse_over}")'
    return md

def getDescStr(codecs):
    if 'args' in codecs and 'desc' in codecs['args']:
        return codecs['args']['desc']
    else:
        return ''

def getIdStr(id, codecs, prefix):
    if prefix == '':
        id_str = f'**{id}**'      # main id in bold
    else:
        id_str = id
    if codecs['codec'] == 'O3EEnum' and codecs['args']['listStr'] in enums and not (codecs['args']['listStr'] in enums_excluded):
        # Add list if enums as mouse over
        id_str = addMouseOver(id_str, json.dumps(enums[codecs['args']['listStr']],indent=None).replace('"',''))
    desc = getDescStr(codecs)
    if desc != '':
        # Add description as mouse over
        id_str = addMouseOver(id_str, desc)
    return id_str

def getCodecStr(codec_str):
    if codec_str in meta_codecs:
        return f'*{codec_str}*' # meta codecs in italic
    else:
        return codec_str

def getUniStr(codecs):
    if 'args' in codecs and 'unit' in codecs['args']:
        md = codecs['args']['unit']
        if md == '°C':
            md = f'[°C](## "°C or °F (system configuration)")'
        return md
    else:
        return ''

def getInfoStr(codecs):
    if 'args' in codecs and 'info' in codecs['args']:
        return codecs['args']['info']
    else:
        return ''
    
def getAccesStr(codecs):
    if 'args' in codecs and 'acc' in codecs['args']:
        if codecs['args']['acc'] == 'rw':
            return '**rw**'
        else:
            return 'ro'
    else:
        return '**??**'

def codec2md(codecs, prefix='', accessStr=''):
    md = ''
    if not (codecs['id'] in ignored_ids):
        # skip json helper ids
        md += F'{prefix}{getIdStr(codecs['id'], codecs, prefix)}|{getCodecStr(codecs['codec'])}|{str(codecs['len'])}|{getUniStr(codecs)}|{accessStr}|{getInfoStr(codecs)}'
    if 'subTypes' in codecs['args']:
        for codec in codecs['args']['subTypes']:
            if not (codec['id'] in ignored_ids):
                md += f'|\n| |{codec2md(codec, prefix+md_indent, '')}'
            else:
                md += f'{codec2md(codec, prefix+md_indent, '')}'
    return md

def did2md(did, codecs):
    return f'|**{str(did)}**|{codec2md(codecs, '', getAccesStr(codecs))}|\n'

def printListOfDoI(DoI):
    dataIdentifiers = dict(open3e.Open3Edatapoints.dataIdentifiers)
    cntDoI = 0
    print('List of Default-DoI:')
    for did in DoI:
        if did in dataIdentifiers['dids']:
            print(f'{did}: {dataIdentifiers['dids'][did].getCodecInfo()['id']}')
            cntDoI += 1
    print(f'{cntDoI} elements.')
    return

def main():

    # # Print list of default DoI:
    # import sys
    # printListOfDoI(DoI_default)
    # sys.exit(0)

    dataIdentifiers = dict(open3e.Open3Edatapoints.dataIdentifiers)
    variants = dict(open3e.Open3EdatapointsVariants.dataIdentifiers)

    didsDict = {}
    didsDictVars = {}

    cntDps = 0
    cntVars = 0
    cntWrt = 0

    # Convert list of general datapoints to json

    for dp in dataIdentifiers["dids"]:
        didsDict[dp] = dataIdentifiers["dids"][dp].getCodecInfo()
        cntDps += 1

    didsDict['Version'] = dataIdentifiers['Version']

    # Convert list of variant datapoints to json

    for dp in variants["dids"]:
        didsDictVars[dp] = {}
        for v in variants["dids"][dp]:
            didsDictVars[dp][v] = variants["dids"][dp][v].getCodecInfo()
        cntVars += 1

    didsDictVars['Version'] = variants["Version"]

    # Create markdonw formatted version of data points

    md = ''
    md += '# Open3E - List of data points\n'
    md += '- Version of general data points: ' + didsDict['Version'] + '\n'
    md += '- Version of variant data points: ' + didsDictVars['Version'] + '\n\n'

    md += '### Remarks:\n'
    md += '* Information on write access to data points (column Access) is based on documents of Viessmann\n'
    md += '  * ro => data point is read only\n'
    md += '  * rw => data point is read and write. However, device my reject or ignore write access anyway\n'

    md += '## Frequently used data points\n'
    md += 'A list of all presently known data points is available [below](#all-presently-known-data-points)\n'
    md += table_header

    for did in DoI_default:
        if did in didsDict:
            md += did2md(did, didsDict[did])
        if did in didsDictVars:
            for variant in didsDictVars[did]:
                md += did2md(did, didsDictVars[did][variant])

    md += '## All presently known data points\n'
    md += table_header

    for key in didsDict:
        if key != 'Version':
            did = int(key)
            md += did2md(did, didsDict[did])
            if did in didsDictVars:
                for variant in didsDictVars[did]:
                    md += did2md(did, didsDictVars[did][variant])

    print(md)

if __name__ == "__main__":
    main()
