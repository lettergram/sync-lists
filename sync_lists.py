"""
Written by Austin Walters
Date: Feb 26, 2019

This script takes in files, identifies the last edited
and syncs the terms across all of them. This could be useful
if you are keeping a blacklist across multiple web apps,
for instance: Terms, IPs, etc.

Takes in a series of lists in the form:

  Term 1
  Term 2
  ....
  Term N

Where each term is one item to syncronize.
"""

import os
import re

# Replace with your lists
lists = [
    'directory_1/config/terms.yaml',
    'directory_2/data/terms.yaml',
    'directory_3/config/list.yaml',
    'directory_4/list.csv',
]



list_items = {} # Form: [item] = [time(integer), keep(boolean)]


# Generate full list of single_listed items (max possible)
for single_list in lists:
    with open(single_list, 'r') as f:
        for row in f:
            item = row.strip()
            list_items[item] = [0, True]
            
            
print("\nUPDATING AND SYNCING LISTS\n")
print("Checks for latest updates to all lists \n"
      + "and applies most recent changes to all\n")
print("{:20s} {:11s}".format("filename", "last edited"))
print("-----------------------------------")

            
# Sync lists, identifying whther to keep each item
for single_list in lists:

    last_update  = os.stat(single_list).st_mtime
    current_list = {}
    
    print("{:20s} {:8.3f}".format(single_list.split('/')[0], last_update))
    
    # Generate dict from current list
    with open(single_list, 'r') as f:
        for row in f:            
            item = row.strip()
            current_list[item] = [last_update, True]
        
    # Iterate over all items to determine if we should utilize that
    for item in list_items:                
        if last_update > list_items[item][0]:
            
            keep_item = True # Default keep items
            if item not in current_list:
                # If item not in list, mark for deletion
                keep_item = False
                
            # Only update if newest
            list_items[item] = [last_update, keep_item]

# Print any removed items
print("\n---- REMOVED ITEMS -----\n")
for item in list_items:
    if not list_items[item][1]:
        print(item, "Removed")
print("\n")

# Rewrite all the files to have the same single_list
for single_list in lists:
    with open(single_list, 'w') as f:
        for item in list_items:
            # Check if the item is marked for saving
            if list_items[item][1]: 
                f.write(item + "\n")
