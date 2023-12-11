#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import json


# In[ ]:





# ** MATCH SUMMARY **

# In[2]:


with open ('t20_json_files/t20_wc_match_results.json')as f :
    data_1 = json.load(f)
    


# In[3]:


len(data_1)


# In[7]:


df_match.info()


# In[5]:


df_match = pd.DataFrame(data_1[0]['matchSummary'])


# In[6]:


df_match.head()


# In[8]:


df_match.shape


# In[9]:


df_match.rename({"scorecard" : "match_id"}, axis = 1 , inplace = True)


# In[28]:


match_id_disct = {}

for index , row in df_match.iterrows():
    key1= row['team1'] + ' Vs ' + row['team2']
    key2= row['team2'] + ' Vs ' + row['team1']
    
    match_id_disct[key1] = row['match_id']
    match_id_disct[key2] = row['match_id']


# In[30]:


match_id_disct['Namibia Vs Sri Lanka']


# In[ ]:





# In[ ]:





# In[10]:


df_match.head()


# In[36]:


df_match.to_csv( 't20_json_files/match_summary.csv'  ,index = False)


# ** BATTING SUMMARY**

# In[11]:


with open ('t20_json_files/t20_wc_batting_summary.json') as f:
    data_2 = json.load(f)
    


# In[12]:


all_records = []
for rec in data_2:
    all_records.extend(rec['battingSummary'])


# In[13]:


df_bating = pd.DataFrame(all_records)


# In[18]:


df_bating.head()


# 

# In[17]:


df_bating.rename({"out/not_out": "dismissal"},axis = 1 , inplace = True)


# In[20]:


df_bating['out/not_out'] = df_bating.dismissal.apply(lambda x: "out" if len(x) > 0 else "not out")


# #creating new coloum out/not-out in pandsa and we are using dismisal coloum 
# #the player is out if len(x) is > 0 else not out and lambda is a feature and x is pointing to all 
# #dismisals 

# In[21]:


df_bating.head(10)


# In[22]:


df_bating.drop(columns=['dismissal'],inplace = True)


# In[24]:


df_bating.head(10)


# In[33]:


df_bating['match_id'] = df_bating['match'].map(match_id_disct)
#df_bating ke andar naya coloum banaya hai match id nam ka , now we have used match coloum refrence 
#to map out the dict here to match the key values with the match coloum


# In[34]:


df_bating.head()


# In[37]:


df_bating.to_csv( 't20_json_files/batting_summary.csv'  ,index = False)


# #bowling #

# In[38]:


with open ('t20_json_files/t20_wc_bowling_summary.json') as f:
    data_3 = json.load(f)
#this one for bowling


# In[39]:


all_records = []
for rec in data_3:
    all_records.extend(rec['bowlingSummary'])


# In[40]:


df_bowling = pd.DataFrame(all_records)


# In[41]:


df_bowling.head()


# In[42]:


df_bowling['match_id'] = df_bowling['match'].map(match_id_disct)


# In[43]:


df_bowling.head()


# In[44]:


df_bowling.to_csv( 't20_json_files/bowling_summary.csv'  ,index = False)


# #players 

# In[47]:


with open("t20_json_files/t20_wc_player_info.json" )as f:
    data_4 = json.load(f)


# In[48]:


df_players = pd.DataFrame(data_4)


# In[50]:


df_players.shape


# In[51]:


df_players.head()


# In[54]:


df_players[df_players["team"] == 'India']


# In[55]:


df_players.to_csv( 't20_json_files/players_summary.csv'  ,index = False)

