import pandas as pd
from sklearn.model_selection import train_test_split

# Create a wrangle function to get the train, test and validation dataset
def wrangle():
    # Get train and test
    data = pd.read_csv('data/train.csv')

    # Split the data into train, validation and test set
    train, test_df = train_test_split(data, test_size=0.20, stratify=data['churn'], random_state=42)
    train_df, val_df = train_test_split(train, test_size=0.25, stratify=train['churn'], random_state=42)

    # multicolinear cols
    mcs = ['total_day_charge', 'total_eve_charge',
           'total_night_charge', 'total_intl_charge']

    # Drop multicolinear columns
    train_df = train_df.drop(columns=mcs)
    val_df = val_df.drop(columns=mcs)
    test_df = test_df.drop(columns=mcs)

    # convert yes to 1 and no to 0 in churn. i.e the target
    yn_mapping = {'yes': 1, 'no':0}

    # map churn to the train and val set
    train_df['churn'] = train_df['churn'].map(yn_mapping)
    val_df['churn'] = val_df['churn'].map(yn_mapping)
    test_df['churn'] = test_df['churn'].map(yn_mapping)

    return  train_df, val_df, test_df