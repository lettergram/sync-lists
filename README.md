# Sync Lists

Syncronize content of files across directories, keeping the most up-to-date edits (additions & removals).

This script takes in files, identifies the last edited and syncs the terms across all of them. This could be useful if you are keeping a blacklist across multiple microservices, websites, apps, etc. Some examples: Blacklisted Terms, IPs, CSV entries, etc.           

------

The expected form of the files to sync are:

    Term 1
    Term 2                                                                                      
    ....                                                                                        
    Term N
    
Where a term can represent one item to syncronize. This could be a term, list, etc. the only requirement is that the line ends with a `\n`. 
