import requests

class WhatPulse:
    def __init__(self, port, retrieve, auto_setup: bool) -> None:
        self.port = port
        self.dataset = dict()
        self.retrieve = retrieve
        self.url_to_api = f"http://localhost:{port}/v1/{retrieve}"
        self.auto_setup = auto_setup

        if auto_setup == True:
            self.setup_api()
        elif auto_setup == False:
            pass

    def setup_api(self):
        push = ["pulse", "open-window", "profiles/activate"]
        get = ["account-totals", "realtime", "unpulsed", "all-stats", "profiles"]

        if self.retrieve in get:
            rsp = requests.get(self.url_to_api)
        elif self.retrieve in push:
            rsp = requests.post(self.url_to_api)
        else:
            raise NameError("Get/Post Request Type not found!\nSupported Types:\nPost: 'pulse', 'open-window' or 'profiles/activate'\nGet: 'account-totals', 'realtime', 'unpulsed', 'all-stats' or 'profiles'")
        
        self.dataset = rsp.json()
        return self.dataset
    
    def return_ranks_location(self):
        ranks = None
        try:
            if self.retrieve == "account-totals":
                ranks = self.dataset["ranks"]
            
            elif self.retrieve == "all-stats":
                ranks = self.dataset["account-totals"]["ranks"]
        except:
            raise NameError("couldn't read any keys from self.dataset... Did you set the dataset up yet?")
        return ranks


    def return_all_keys_values(self):
        '''
        Works for:
            account-totals
            realtime
            unpulsed
            all-stats
            profiles
        '''
        try:
            all_keys = list(self.dataset.keys())
        except:
            raise NameError("couldn't read any keys from self.dataset... Did you set the dataset up yet?")
        
        all_values = list()
        for key in self.dataset.keys():
            all_values.append(self.dataset[key])
        
        return list(all_keys), all_values

    def return_value(self, key):
        '''
        Works for:
            account-totals
            realtime
            unpulsed
            all-stats
        '''
        try:
            value = self.dataset[key]
            return value
        except:
            raise KeyError("Couldn't find key in your dataset")
    
    def return_all_ranks(self):
        '''
        Works for:
            account-totals
            all-stats
        '''
        ranks = self.return_ranks_location()

        keys = list(ranks.keys())
        
        all_ranks = []
        all_ranks_formatted = list()

        for i in range(len(keys)):
            if i % 2 == 0:
                all_ranks.append((keys[i], ranks[keys[i]]))
            else:
                all_ranks_formatted.append((keys[i], ranks[keys[i]]))
        
        return all_ranks, all_ranks_formatted

    def return_rank(self, key: str):
        '''
        Works for:
            account-totals
            all-stats
        '''
        ranks = self.return_ranks_location()
        try:
            value = ranks[key]
            return value
        except:
            raise KeyError("Couldn't find key in your dataset")
    
    def all_profiles(self):
        '''
        Works for:
            profiles
        '''
        return self.dataset['profiles']
    
    def search_profile(self, retriever, value):
        found_profile = False
        len_profiles = len(self.dataset["profiles"])

        for i in range(len_profiles):
            if value == self.dataset["profiles"][i][retriever]:
                found_profile = True
                return self.dataset['profiles'][i]
        
        if found_profile == False:
            raise BaseException("No profiles have been found. Check if the value you're looking for is correct :D")
    

    def return_profile_value(self, retriever, profile_id):
        """
        if the profile_id is 0 the program returns a list of the value from the retriever from all profiles.
        So if you have 2 profiles and you set the retriever to 'name' and the id to 0 it will return the name
        of all profiles.

        retrievers: 'name'; 'id'; 'active'; 'created_at'; 'updated_at'

        Whats an ID?
        The ID is a number which identifies which profile you're looking for.
        The first profile you create has the ID 1, the second one has the ID 2 and so on...
        """
        if profile_id == 0:
            len_profiles = len(self.dataset['profiles'])
            value = []

            try:
                for i in range(len_profiles):
                    value.append(self.dataset['profiles'][i][retriever])
                return value
            
            except:
                raise BaseException("Check if the ID or retriever exists.")
        
        else:
            try:
                value = self.dataset["profiles"][profile_id-1][retriever]
            except:
                raise BaseException("Check if the ID or retriever exists.")
            return value