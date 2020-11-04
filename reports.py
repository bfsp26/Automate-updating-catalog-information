#!/usr/bin/env python3

import reports
import datetime
import os

path = "~/supplier-data/descriptions/"
files = os.listdir(path)

for file in files:
    with open(path + file) as dcp_file:
        lines = dcp_file.readlines()
        
        
        
if __name__ == "__main__":
      reports.generate_report(attachment, title, paragraph)