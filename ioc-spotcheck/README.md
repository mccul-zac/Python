Purpose:
 - Check if IOCs are in a log file  

To Do:
 - [x] Fix loop
 - [ ] Fix format
    - [x] Print only 1 ioc to a (possible) list of logs 
    - [x] Create dict where key='ioc' and value=[logs]
    - [ ] Create new file rather than store in mem
    - [ ] Cut matching strings from beginning/end (dedup IOCs ahead of time)
    - [ ] remove keys with no value (empty list)
 - [ ] Create a dedup
    - [ ] remove iocs with repeating sequence of chars
