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
# Convert Open3E datapoint list from JSON back to python file and adds info about writablility of data points.
#
# There is no need to use this tool when using open3e.
#
# 10.02.2026: Initial version
#

import json
from datetime import date

import open3e.Open3Eenums
import open3e.Open3Edatapoints
import open3e.Open3EdatapointsVariants

from open3e.Open3Ecodecs import *

with open('Open3Edatapoints_writables.json', 'r') as file:
    dids_writable = json.load(file)


def main():

    dataIdentifiers = dict(open3e.Open3Edatapoints.dataIdentifiers)
    variants = dict(open3e.Open3EdatapointsVariants.dataIdentifiers)

    didsDict = {}
    didsDictVars = {}

    for dp in dataIdentifiers["dids"]:
        codecStr = dataIdentifiers['dids'][dp].getCodecString()
        if str(dp) in dids_writable:
            codecStr = codecStr[:-1]+', "acc"="rw"),'
        else:
            codecStr = codecStr[:-1]+', "acc"="ro"),'

        print(f"        {dp} : {codecStr}")

if __name__ == "__main__":
    main()
