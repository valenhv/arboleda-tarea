import pandas as  pd
df = pd.read_csv('arbolado-publico-lineal-2017-2018.csv')

# importing sweetviz
import sweetviz as sv
#analyzing the dataset
advert_report = sv.analyze(df)
#display the report
advert_report.show_html('Arbolado.html')