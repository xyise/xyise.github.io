import pandas as pd
import lxml.html as lh
import requests

def read_hist_data_from_treasurydirectgov(dt):
    """get historical data from treasurydirect.gov

        they should provide the data on the following columns: 
            'CUSIP', 'SECURITY TYPE', 'RATE', 'MATURITY DATE', 'CALL DATE', 'BUY',
       'SELL', 'END OF DAY'

        return clean and removed dataframe
    Args:
        dt (datetime)
    """
    year = dt.year
    month = dt.month
    day = dt.day

    args = {
        'priceDate.day': str(day),
        'priceDate.month': str(month),
        'priceDate.year': str(year),
        'submit': 'Show Prices'
    }
    # settings
    num_expected_cols = 8

    # request
    response = requests.post('https://www.treasurydirect.gov/GA-FI/FedInvest/selectSecurityPriceDate.htm', data=args, verify=True)
    doc = lh.fromstring(response.content)
    tr_elements = doc.xpath('//tr')

    # read the table
    table_data = []
    for row in tr_elements:
        if len(row) != num_expected_cols:
            continue
        table_data.append([c.text_content() for c in row])

    # if no data is available, throw an exception
    if len(table_data) == 0:
        date_str = str(year) + str(month) + str(day)
        raise Exception(date_str + ': failed to retrieve data')

    # put them into a data frame 
    columns = table_data[0]
    data = table_data[1:]
    df = pd.DataFrame(data=data, columns = columns)

    # now clean them
    df = parse_and_clean(df)

    return df

def parse_and_clean(df):
    """parse the raw data from the site and remove data if not clean
    Args:
        df ([type]): dataframe with
    """

    df['RATE'] = df['RATE'].apply(parse_rate)
    df['MATURITY DATE'] = pd.to_datetime(df['MATURITY DATE'], format='%m/%d/%Y')
    for c in ['BUY', 'SELL', 'END OF DAY']:
        df[c] = df[c].astype(float)

    return df
    

def parse_rate(x):
    unit = x[-1]
    if unit == '%':
        return float(x[0:-1]) / 100
    else:
         raise Exception('unknown rate type ' + unit)





    


