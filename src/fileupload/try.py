import pprint
import pandas as pd

df = pd.read_csv('../files/proforma_commandes.csv')
df2 = pd.read_csv('../files/proforma_transport.csv')
result = pd.concat([df,df2]).drop_duplicates(keep=False)
result = result.reset_index(drop=True).to_json('../files/output.json')