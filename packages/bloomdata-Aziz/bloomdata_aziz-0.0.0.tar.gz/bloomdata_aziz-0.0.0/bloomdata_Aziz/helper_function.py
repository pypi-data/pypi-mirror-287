from setuptools import setup, find_packages
import random
import numpy as np
import pandas as pd
#part 2 functions#############################
adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']
def random_phrase():
    '''will choose random phrase from the list'''
    adj = random.choice(adjectives)
    #  random_index = random.randint(0, len(nouns)-1)
    #  noun = nouns[random_index]
    noun = random.sample(nouns, 1)[0]
    return adj + ' ' + noun

# print(random_phrase())
# print(random_phrase())
# print(random_phrase())


def random_float(min_val, max_val):
    '''will print random float sample between min and max range'''
    return random.uniform(min_val, max_val)

# print(random_float(2, 4))
# print(random_float(2, 4))
# print(random_float(2, 4))


def random_bowling_score():
    '''will print random integer sampled between 0 and 100'''

    return random.randint(0, 300)


# print(random_bowling_score())
# print(random_bowling_score())
# print(random_bowling_score())

def silly_tuple():
    '''will return a tuple with out put from above functions'''

    return (random_phrase(), round(random_float(1, 5), 1), random_bowling_score())

# print(silly_tuple())

def silly_tuple_list(num_tuple):
    '''returns the out of silly_tuple function output as a list'''

    tuple_list = []
    for i in range(num_tuple):
        tuple_list.append(silly_tuple())
    return tuple_list

# print(silly_tuple_list(5))    

# part 3 functions###################################    
test_df = pd.DataFrame(np.array([[1, 2, 3], [4, np.nan ,6], [7, 8, 9]]))
def null_count(df): 
    '''this function will return Nan value of data frame'''
    return df.isnull().sum().sum()
# print(null_count(test_df))

def train_test_split(df, frac= 0.8):
    '''this function will split data set for ml purposes'''
    train = df.sample(frac=frac)
    test = df.drop(train.index).sample(frac=1.0)
    return train, test

# print(train_test_split(test_df))

def randomize(df, seed):
    ''''this function randomizes all cells of a data frame'''
    randomized_df = df.sample(frac=1.0, random_state= seed)
    return randomized_df

# print(randomize(test_df, 42))


address_df = pd.DataFrame({'address': ['890 Jennifer Brooks\nNorth Janet, WY 24785', 
                                        '8394 Kim Meadow\nDarrenville, AK 27389',
                                        '379 Cain Plaza\nJosephburgh, WY 06332',
                                         '5303 Tina Hill\nAudreychester, VA 97036']})

def addy_split(addy_series):
    '''this will split given string address'''
    df = pd.DataFrame()
    city_list = []
    state_list = []
    zip_list = []

    for i in addy_series:
        second_half = i.split('\n')[1]
        city = second_half.split(',')[0]
        state = second_half.split()[-2]
        zip_ = second_half.split()[-1]
        #append
        city_list.append(city)
        state_list.append(state)
        zip_list.append(zip_)
       #add to df
    df['city'] = city_list
    df['state']=state_list
    df['zip'] = zip_list
    return df
# print(addy_split(address_df['address']))


def abbr_2_st(state_series, abbr_2_st= True):
    '''take abbreviation and returns full name and vise vera'''

    state_dict= {'AL': 'Alabama',
        'AK': 'Alaska',
        'AZ': 'Arizona',
        'AR': 'Arkansas',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'IA': 'Iowa',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'ME': 'Maine',
        'MD': 'Maryland',
        'MA': 'Massachusetts',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MS': 'Mississippi',
        'MO': 'Missouri',
        'MT': 'Montana',
        'NE': 'Nebraska',
        'NV': 'Nevada',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NY': 'New York',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VT': 'Vermont',
        'VA': 'Virginia',
        'WA': 'Washington',
        'WV': 'West Virginia',
        'WI': 'Wisconsin',
        'WY': 'Wyoming',
        'DC': 'District of Columbia',
        'AS': 'American Samoa',
        'GU': 'Guam',
        'MP': 'Northern Mariana Islands',
        'PR': 'Puerto Rico',
        'UM': 'United States Minor Outlying Islands',
        'VI': 'U.S. Virgin Islands'
    }
    def abbrev_replace(abbrev):
        return state_dict[abbrev]
    def state_replace(state_name):
        reverse_state_dict = dict((v, k) for k, v in state_dict.items())
        return reverse_state_dict[state_name]
    if abbr_2_st:
         return state_series.apply(abbrev_replace)




addy_state= addy_split(address_df['address'])['state']

full_state_name = abbr_2_st(addy_state)

#print(abbr_2_st(full_state_name, abbr_2_st= False))

def list_2_series(list_2_series, df):
    new_column = pd.Series(list_2_series)
    return pd.concat([df, new_column], axis=1)

#print(list_2_series([11,1,2], test_df))
outlier_df = pd.DataFrame(
    {'a' : [1, 2, 3, 4, 5, 6],
     'b' : [4, 5, 6, 7, 8, 9],
     'c' : [7, 1000, 9, 10, 11, 12]})

def outlier(df):
    cleaned_df = pd.DataFrame()
    for (columnName, columnData) in df.items():
        Q1 = columnData.quantile(0.25)
        Q3 = columnData.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5*IQR
        upper_bound = Q3 + 1.5*IQR
        #print(lower_bound, upper_bound)
        mask = columnData.between(lower_bound, upper_bound, inclusive = 'both')
        cleaned = columnData.loc[mask]

        
        cleaned_df[columnName] = cleaned
    print(cleaned_df)


#outlier(outlier_df)

def split_dates(date_series):
    #MM/DD/YYYY
    df = pd.DataFrame()
    month_list = []
    day_list = []
    year_list = []
    for date in date_series:
        month_list.append(date.split('/')[0])
        day_list.append(date.split('/')[1])
        year_list.append(date.split('/')[2])

    df['month'] = month_list
    df['day'] = day_list
    df['year'] = year_list

    return df   
print(split_dates(pd.Series(['01/13/2016', '02/14/2017', '03/15/2018', '04/16/2019']))) 
