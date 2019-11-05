# dupy: A simple duplicate file finder

## What is dupy?

Dupy is a python3 application that traverses a given directory and finds
files that are duplicates. It lists the duplicates it finds and
provides a summary below, including the number of duplicates found and
the total amount of space being taken up by duplicates. You can then go 
and resolve the duplicates however you please.

## How do I use dupy?

dupy operates in two modes: with an argument and without a path
argument.

**With an argument:** dupy will use the provided path as a the root 
directory for the search.

**Without an argument:** dupy will use its own path as the root 
directory for the search.

### Examples:

**Without an argument (i.e. search current directory):**

    C:\Users\My Account\Pictures> du.py
    Processing path C:\Users\{User}\Pictures
    Processing directory C:\Users\My Account\Pictures\Christmas 2019
    Processing directory C:\Users\My Account\Pictures\Barcelona 2019
    Processing directory C:\Users\My Account\Pictures\Barcelona 2019\Me
    Processing directory C:\Users\My Account\Pictures\Barcelona 2019\Dave's Camera
    ...
    Duplicate hash 74c2279525b982f6425a93cabbd8e4b0f87436dfe4b5eedd5999c0883d923443
      C:\Users\My Account\Pictures\Barcelona 2019\P1060558.JPG
      C:\Users\My Account\Pictures\Barcelona 2019\Me\P1060558.JPG
    Space wasted: 3.141 MB
    
    Duplicate hash c53898603b438344f7ae767be344104b4c1f4dd33f238e395c019df4afd53f26
      C:\Users\My Account\Pictures\Barcelona 2019\P1060559.JPG
      C:\Users\My Account\Pictures\Barcelona 2019\Me\P1060559.JPG
    Space wasted: 2.32 MB
    ...
    Run statistics:
      Time taken: 42.82 seconds
      File count: 620
      Duplicate hashes found: 12
      Space wasted by duplicates: 8.503 MB

**With an argument (i.e. search given directory):**

    C:\Users\My Account\Tools\dupy> du.py "E:\Photo Archive"
    Processing path E:\Photo Archive
    Processing directory E:\Photo Archive\Old Phone
    Processing directory E:\Photo Archive\Old Phone\DCIM
    Processing directory E:\Photo Archive\iPhone Backup 2018 08
    Processing directory E:\Photo Archive\iPhone Backup 2019 06
    Processing directory E:\Photo Archive\Lake District Trip 2019
    ...
    Duplicate hash eaf0f426c8080de0b59b986517d01d5e1faa82af93a81b935a49359aba20ce03
      E:\Photo Archive\iPhone Backup 2018 08\IMG 4305.JPG
      E:\Photo Archive\iPhone Backup 2019 06\IMG 4305.JPG
    Space wasted: 3.518 MB
    
    Duplicate hash a7c47d0ee699c53b26691e7a9e134bb878197038d026ef09977cfd04411dea47
      E:\Photo Archive\iPhone Backup 2018 08\IMG 4306.JPG
      E:\Photo Archive\iPhone Backup 2019 06\IMG 4306.JPG
    Space wasted: 4.22 MB
    ...
    Run statistics:
      Time take: 3,308.84 seconds
      File count: 18,435
      Duplicate hashes found: 83
      Space wasted by duplicates: 65.4 MB 

## Is dupy ready for use?

Yes, you can use dupy to do what is described in 'What is dupy?'

It is, however, at what would charitably be called an untested phase.
I built this for my own use and academic interest and so I haven't yet
polished out handling things like passing something dumb as the argument
or giving it a stupidly large folder.

## Is dupy finished?

No.  It does what it says in 'What is dupy?' and the plan is to extend
the functions in future, so that it will do things like provide 
interactive duplicate resolution.

## Yet to come:

- interactive duplicate resolution
- filetype white-/blacklisting
- wreckless mode: automatically delete duplicates found after the first
- link replace: replace deleted duplicates with shortcuts/links to
original