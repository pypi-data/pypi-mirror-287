# WhatPulse API Python Package
This Package makes use of the WhatPulse Client API, making you able to easily use the API for any purpose (almost).

## Introduction to the Package

1. Setting the API up
To set up the API, you need to download and use the WhatPulse Application on PC. 
Click on the Settings Tab, then Enable the Client API and choose a Port (or use the standard 3490 Port).

1. Start Coding (Setting up API)
First you have to import this Package, then define the API Object by calling the WhatPulse Class. Here you need the port you connect to, the retriever (more on that later) and if the Bot gets automatically set up (more on that later too)
```
import WhatPulseAPI as wp_api
my_api = wp_api.WhatPulse(<port>, <retriever>, <auto-setup?>)
```
## **Explanations (Docs)**

### **Retrievers:**
Retrievers are the last part of the URL to the API, usually the URL looks something like this: "http://localhost:3490/v1/account-totals". In this case "account-totals" is the retriever.
```
import WhatPulseAPI as wp_api
my_api = wp_api.WhatPulse(3490, "account-totals", True)
```
**All Retrievers:**
- account-totals (shows your total stats)
- realtime (shows stats per second e.g. Clicks Per Second)
- unpulsed (reveals all unpulsed stats)
- all-stats (all of the above)
- profiles (returns all profiles)
- pulse (pulses WhatPulse)
- open-window (opens WhatPulse window)
- profiles/activate (not implemented yet)

### **Auto-Setup:**

Auto-Setup essentially automatically sends a request to the API as soon as you initialize the WhatPulse class. Meaning that this code would instantly open the WhatPulse window as soon as you run this program.
```
import WhatPulse_API as wp_api
my_api = wp_api.WhatPulse(3490, "open-window", True)
```
If you want to send a request later, then do this:
```
# Opens WhatPulses window after 5 seconds.
import WhatPulse_API as wp_api, time
my_api = wp_api.WhatPulse(3490, "open-window", False)

time.sleep(5)
my_api.setup_api()
```

### **return_all_keys_values()**
The JSON File called by the API is essentially a bunch of tuples we can append all keys to one list and all the values to the corresponding keys in another list.
```
import WhatPulseAPI as wp_api
my_api = wp_api.WhatPulse(3490, "account-totals", True)
all_keys, all_values = my_api.return_all_keys_values()

print(all_keys, all_values)
> all_keys: ['clicks', 'clicks_formatted', 'distance_formatted', 'distance_miles', 'download', 'download_formatted', 'keys', 'keys_formatted', 'ranks', 'scrolls', 'scrolls_formatted', 'upload', 'upload_formatted', 'uptime', 'uptime_formatted']
> ['2311327', '2.311.327', '415km, 701m', '258.305', '2501209', '2,39TB', '6239937', '6.239.937', {'rank_clicks': '42866', 'rank_clicks_formatted': '42.866th', 'rank_distance': '3281', 'rank_distance_formatted': '3.281st', 'rank_download': '22213', 'rank_download_formatted': '22.213th', 'rank_keys': '30767', 'rank_keys_formatted': '30.767th', 'rank_scrolls': '5375', 'rank_scrolls_formatted': '5.375th', 'rank_upload': '16702', 'rank_upload_formatted': '16.702nd', 'rank_uptime': '60442', 'rank_uptime_formatted': '60.442nd'}, '1762076', '1.762.076', '577453', '563,92GB', '8971926', '103d, 20h, 12m']
```

### **return_value(key)**
Returns the value to the corresponding key.

```
import WhatPulseAPI as wp_api 
my_api = wp_api.WhatPulse(3490, "account-totals", True) 
value = my_api.return_value('clicks')
print(value)

> 2311327
```

### **return_all_ranks()** 
Returns all ranks, one list for all the ranks that have not been formatted yet and one list for the formatted ranks as you can see here in the small code snippet.
```
import WhatPulseAPI as wp_api 
my_api = wp_api.WhatPulse(3490, "account-totals", True) 
all_ranks, all_ranks_formatted = my_api.return_all_ranks()

print(all_ranks[0], all_ranks_formatted[0])

> all_ranks[0] -> ('rank_clicks', '42866')
> all_ranks_formatted[0] -> ('ranks_clicks_formatted', '42.866th')
```

### **return_rank(key)**
Returns the value to the corresponding rank-key.
```
import WhatPulseAPI as wp_api 
my_api = wp_api.WhatPulse(3490, "account-totals", True) 
value = my_api.return_rank('rank_clicks_formatted')
print(value)

> 42.866th
```

### **all_profiles()**
Returns all profiles in your Whatpulse Account
```
import WhatPulse_API as wp_api
my_api = wp_api.WhatPulse(3490, "profiles", True)
my_profiles = my_api.all_profiles()
print(my_profiles)

>[{'name': 'gaming', 'id': 1, 'active': False, 'created_at': '2024-05-08T10:47:09.000', 'updated_at': '2024-05-10T09:40:22.000'}, {'name': 'test', 'id': 2, 'active': True, 'created_at': '2024-07-31T09:47:10.500', 'updated_at': '2024-07-31T12:22:50.000'}]
```
### **search_profile(retriever, value)**
This searches for a profile and if it finds a profile it returns a json dict with all the information regarding the profile.
```
import WhatPulse_API as wp_api
my_api = wp_api.WhatPulse(3490, "profiles", True)
profile_data = my_api.search_profile('name', 'gaming')

# if there is a profile with the name 'gaming':
print(profile_data)

> {'name': 'gaming', 'id': 1, 'active': False, 'created_at': '2024-05-08T10:47:09.000', 'updated_at': '2024-05-10T09:40:22.000'}

# if the program can't find a profile with the name 'gaming':
raise  BaseException("No profiles have been found. Check if the value you're looking for is correct :D")
```

### **return_profile_value(retriever,  profile_id)**
This returns the value from a specific retriever in a given profile
```
import WhatPulse_API as wp_api
my_api = wp_api.WhatPulse(3490, "profiles", True)
value = return_profile_value("name", 1)

"""
This program now looks for a profile with the ID 1 and
returns the name of the profile
"""

print(value)
> "gaming"
``` 
