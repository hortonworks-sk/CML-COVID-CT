import pandas as pd
import numpy as np
import seaborn as sns
import pyspark.sql.functions;
from pyspark.sql.functions import rand, when;
from pyspark.sql import SparkSession



df = pd.read_csv('data/customers_combined_clean_cut.csv',sep=',',)

df.surname =df.surname.astype(str)
df.title = df.title.astype(str)

df.head()


df_cut = df[:20]

df_cut2 = df_cut[['title', 'givenname', 'surname']]

row_count = df_cut2.shape[0]




df_cut2['conversion probability'] = np.random.randint(0,100, row_count)/300


pdf = df_cut2

spacing = dict(props=[('border-collapse', 'separate'), 
                                       ('border-spacing',  '50px 0px')])

cm = sns.light_palette("lightblue", as_cmap=True)


pdf.style.format({"surname": lambda x:x.upper()})\
    .format({"title": lambda x:x.upper()})\
    .background_gradient(cmap=cm, subset=['conversion probability'])\
    .set_table_styles([spacing])
    
    
    #.set_table_styles([{'selector': '', 'props': [('border', '4px solid #000')]}])


  
