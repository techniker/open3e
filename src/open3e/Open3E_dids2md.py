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

DoI_default = [256, 266, 268, 356, 1006]                            # Frequently used Dids

md_indent = '- '                                                    # Indentation of sub codecs
meta_codecs = ['O3EList','O3EComplexType']                          # List of meta codecs, show in italic
ignored_ids = ['ListEntries']                                       # List of ids to be ignored (helper ids for json format)
enums = dict(open3e.Open3Eenums.E3Enums)                            # Enumerations known to open3e
enums_excluded = ['Errors','Warnings','States','Infos','Country']   # Do NOT list the entries of enumerations for those keys

table_header =  '|  Did | ID   | Codec | Length | Unit | Description | Further info |\n| ---: | :--- | :--- | ---: | :---: | :--- | :--- |\n'

def getIdStr(id, codecs, prefix):
    if prefix == '':
        id_str = f'**{id}**'      # main id in bold
    else:
        id_str = id
    if codecs['codec'] == 'O3EEnum' and codecs['args']['listStr'] in enums and not (codecs['args']['listStr'] in enums_excluded):
        id_str = f'[{id_str}](## "{json.dumps(enums[codecs['args']['listStr']],indent=None).replace('"','')}")'
    return id_str

def getCodecStr(codec_str):
    if codec_str in meta_codecs:
        return f'*{codec_str}*' # meta codecs in italic
    else:
        return codec_str

def getUniStr(codecs):
    if 'args' in codecs and 'unit' in codecs['args']:
        return codecs['args']['unit']
    else:
        return ''

def getDescStr(codecs):
    if 'args' in codecs and 'desc' in codecs['args']:
        return codecs['args']['desc']
    else:
        return ''

def getInfoStr(codecs):
    if 'args' in codecs and 'info' in codecs['args']:
        return codecs['args']['info']
    else:
        return ''

def codec2md(codecs, prefix=''):
    md = ''
    if not (codecs['id'] in ignored_ids):
        # skip json helper ids
        md += F'{prefix}{getIdStr(codecs['id'], codecs, prefix)}|{getCodecStr(codecs['codec'])}|{str(codecs['len'])}|{getUniStr(codecs)}|{getDescStr(codecs)}|{getInfoStr(codecs)}'
    if 'subTypes' in codecs['args']:
        for codec in codecs['args']['subTypes']:
            if not (codec['id'] in ignored_ids):
                md += f'|\n| |{codec2md(codec, prefix+md_indent)}'
            else:
                md += f'{codec2md(codec, prefix+md_indent)}'
    return md

def did2md(did, codecs):
    return f'**{str(did)}**|{codec2md(codecs, '')}|\n'

def main():
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

    md += '## Frequently used data points\n'
    md += table_header

    for did in DoI_default:
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
