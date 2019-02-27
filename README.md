# Sync Lists

**Sync Lists** is a simple script for synchronizing the content files across directories. 

Specifically, designed for lists, keeping the most up-to-date edits sync'd (additions & removals).

This script takes in a list of files (defined in the script), identifies the last edited and syncs the terms across all of them. This could be useful if you are keeping a blacklist across multiple microservices, websites, apps, etc. Some examples: Blacklisted Terms, IPs, CSV entries, etc.

------

## Expected Input

The expected form of the files to sync are:

    Item 1
    Item 2                                                                                      
    ....                                                                                        
    Item N
    
Where an item can represent one item to syncronize. 

This could be a item, list, etc. the only requirement is that the line ends with a `\n`. 

## Example

If for instance, lets say we have a list of IPs we have blacklisted. If we removed: `127.0.0.1` from one of the five blacklist config files we keep for our webservices. When I run `python sync_lists.py`, it'll sync across all the files and remove `127.0.0.1`. 

    UPDATING AND SYNCING LISTS

    Checks for latest updates to all lists 
    and applies most recent changes to all

    filename             last edited
    -----------------------------------
    website_1.com        1551244020.288
    website_2.com        1551244039.890
    website_3.com        1551244020.292
    website_4.com        1551244020.292
    website_5.com        1551244020.292

    ---- REMOVED ITEMS -----

    Removed: 127.0.0.1

Terms which have been added are not noted. 