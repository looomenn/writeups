---
CTF: VishwaCTF2024
Category: misc
Points: 286
Date: 2024-03-02
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
VishwaCTF{Matthew_Darwin_15:31:29}
```

### Details

Description

> There was a major heist at the local bank. Initial findings suggest that an intruder from within the bank, specifically someone from the bank's database maintenance team, aided in the robbery. This traitor granted access to an outsider, who orchestrated the generation of fake transactions and the depletion of our valuable customers' accounts. We have the phone number, '789-012-3456', from which the login was detected, which manipulated the bank's employee data. Additionally, it's noteworthy the this intruder attempted to add gibberish to the binlog and ultimately dropped the entire database at the end of the heist. 
> 
> Your task is to identify the first name of the traitor, the last name of the outsider, and the time at witch the outsider was added to the database. 
> 
> Flag format: 
> VishwaCTF{TraitorFirstName_OutsiderLastNmae_HH:MM:SS}

Files
![](assets/Pasted%20image%2020240328115233.png)
See source folder for files ^\_^

So, we get the msqlbin file. Using `msqlbinlog` we convert it to readable format.

```
msqlbinlog --verbose DBlog-bin.000007 > log_long.log
```

From the description, we know the traitor's phone number is `789-012-3456`

![](assets/Pasted%20image%2020240328120400.png)

Using grep, we now know on which line it is 
```sql
### INSERT INTO `bank`.`maintainers`
### SET
###   @1=7
###   @2='Matthew'
###   @3='Miller'
###   @4='matthew.miller@example.com'
###   @5='789-012-3456'
###   @6='Database Administrator'
###   @7='DBA'
###   @8='12:00:00'
###   @9='14:00:00'
```

So, his first name is `Matthew`, now we need info about the outsider.

Browsing through the file, we can find a strange update operation
```sql
### UPDATE `bank`.`employees`
### WHERE
###   @1=1
###   @2='John'
###   @3='Smith'
###   @4='1985:05:15'
###   @5='john.smith@example.com'
###   @6='1234567890'
###   @7='123 Main St'
###   @8='Mumbai'
###   @9='Maharashtra'
###   @10='400001'
###   @11=1
### SET
###   @1=1
###   @2='John'
###   @3='Darwin'
###   @4='1990:01:01'
###   @5='johndoe@example.com'
###   @6='+1234567890'
###   @7='123 Main St'
###   @8='Anytown'
###   @9='Anystate'
###   @10='12345'
###   @11=1
```

Moreover, we can see manipulations with accounts we were told about earlier, right after this strange update. 
```sql
### UPDATE `bank`.`accounts`
### WHERE
###   @1=1
###   @2=1
###   @3=1
###   @4=5000.00
###   @5='2023:01:01'
### SET
###   @1=1
###   @2=1
###   @3=1
###   @4=0.00
###   @5='2023:01:01'
### UPDATE `bank`.`accounts`
### WHERE
###   @1=2
###   @2=1
###   @3=2
###   @4=10000.00
###   @5='2023:01:01'
### SET
###   @1=2
###   @2=1
###   @3=2
###   @4=0.00
###   @5='2023:01:01'
```

Also, that can catch our attention, is the email that was updated. All other emails are formatted like: `firstname.lastname@example.com` except the new one: `johndoe@example.com`. And, the last name was changed to Darwin, so neither the format nor the last name is correct. 

That means, our outsider's last name is `Darwin`

And for the timestamp, it's located in the operation log

![](assets/Pasted%20image%2020240328122431.png)

```sql
# at 80520
#240227 12:01:29 server id 1 end_log_pos 80551 CRC32 0xebf8ef83 Xid = 2928
```

But we need to convert that timestamp to IST:
`12:01:29` -> `15:31:29`
12:02:29 GMT+2 + 03:30:00 = 15:31:29

So, the flag is:
```
VishwaCTF{Matthew_Darwin_15:31:29}
```