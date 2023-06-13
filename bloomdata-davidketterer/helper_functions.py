# Find all null values in a Dataframe
def null_count(df):
    return df.isnull().sum().sum()

# Function to split Df into train and test set, with test set being of size frac
from sklearn.model_selection import train_test_split
def train_test_split(df, frac):
    
    df_train, df_test = train_test_split(df, train_size = frac)
     
    return df_train, df_test

# Randomize all values in the Dataframe, with random seed for reproducibility
def randomize(df, seed):
    randomized_df = df.copy()  

    values = randomized_df.values

    np.random.seed(seed)

    np.random.shuffle(values.flat)

    randomized_df.iloc[:, :] = values

    return randomized_df    

# Split addresses into Dataframe with columns city, state and zip
def addy_split(addy_series):
    cities = []
    states = []
    zips = []
    patternc = r'(?P<City>\b[^,\n]+),'
    patterns = r'\b([A-Z]{2})\b'
    patternz = r'\b(\d{5})\b'
    
    for i in range (len(addy_series)) :
        cities.append(addy_series[i].str.extract(patternc))
        states.append(addy_series[i].str.extract(patterns))
        zips.append(addy_series[i].str.extract(patternz))

    df = pd.DataFrame()
    df['city']= cities
    df['state'] = states
    df['zip'] = zips

    return df

def abbr_2_st(state_series, abbr_2_st=True):
    adict = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}
    
    if abbr_2_st:
        full_names = state_series.map({v: k for k, v in adict.items()})
        return full_names
    else: 
        abbrev = state_series.map(adict)
        return abbrev 

def list_2_series(list_2_series, df):
    series = pd.Series(list_2_series)
    df[list_2_series]=series 
    return df    
    
def rm_outlier(df):
    cleaned_df = df.copy()
    
    for col in columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        cleaned_df = cleaned_df.loc[(cleaned_df[col] >= lower_bound) & (cleaned_df[col] <= upper_bound)]
    
    return cleaned_df

def split_dates(date_series):
    df = pd.DataFrame()
    month = []
    day = []
    year = []
    for entry in date_series:
        month.append(entry[0:2])
        day.append(entry[3:5])
        year.append(entry[6:10])
    df['month']= pd.Series(month)
    df['day']= pd.Series(day)
    df['year']= pd.Series(year)
    return df

        