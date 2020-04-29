# COVID-19
IBM Call for Code - COVID-19

Public Data Source from Johns Hopkins University after refined by Excel (need refined because of many data not standard, 
ie. Country Code : Mainland China, China, Taiwan, Taiwan*, South Korea, "Korea, South", Palestine, West Bank and Gaza). 
It will be standardize to ISO 3166 Standard for better Geographic Visualization.

Another difficulties is data not come daily on same day, it is need to refined to display latest data on Dashboard. 
Also data from Cruise Ship need to separate column to avoid double counting.

We also analyze relation with Weather Condition and Population Data of the hardest hit location.

Hope this dataset will describe a global picture of what happened with "COVID-19 Pandemic" day to day and to assure our 
preparedness for the next potential pandemic.

Additionally, we collect unstructured historical data from www.worldometer.info and another sources, this data uploaded to IBM DB2 on Cloud. Using this RDBMS we can query data efficiently, we can monitored whats going on around the world day by day and drilled down
to Country, Province/State (for several Coutries) and County (for US Only).

End product of this application is COVID_19_HISTORICAL_RECORD, comparable to Health Care Medical Record with Countries, Provinces/Counties as it's patients.


