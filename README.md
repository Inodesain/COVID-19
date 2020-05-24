# COVID-19 - HISTORICAL RECORD
IBM Call for Code - COVID-19

Public Data Source from Johns Hopkins University after refined by Excel (need refined because of many data not standard, 
ie. Country Code : Mainland China, China, Taiwan, Taiwan*, South Korea, "Korea, South", Palestine, West Bank and Gaza). 
It will be standardize to ISO 3166 Standard for better Geographic Visualization.

Another difficulties is data not come daily on same day, it is need to refined to display latest data on Dashboard. 
Also data from Cruise Ship need to separate column to avoid double counting.

We also analyze relation with Weather Condition and Population Data of the hardest hit location.

Hope this dataset will describe a global picture of what happened with "COVID-19 Pandemic" day to day and to assure our 
preparedness for the next potential pandemic.

Additionally, we collect unstructured historical data from World Health Organization (WHO) time line, situation report and event
as they happened, www.worldometer.info and another sources, this data uploaded to IBM DB2 on Cloud. Using this RDBMS we can query
data efficiently, we can monitored whats going on all around the world day by day and drilled down to Country, Province/State
(for several Coutries) and County/Admin Region (for US and Canada).

End product of this application is COVID_19_HISTORICAL_RECORD, comparable to Health Care Medical Record with Countries, Provinces/Counties as it's patients.

This file has been tested and running on IBM Watson using Cognos Dashboard Embedded, DB/2 on Cloud, Jupyter Notebook and Cloud Object Storage. Sample data from Weather Channel also use to complete this Covid-19 historical record.

We have been uploaded this file to OpenERP/Odoo Studio and analyze it with their Pivot View and Calendar. (Sample form attached in JPG file). OpenERP/Odoo can be run on IBM Cloud ( https://cloud.ibm.com/catalog/content/odoo )



=======
Refined Items :
- Standardize Country, Province/State and County/Administrative Area Naming, and add related GeoID :
   - China, instead of Mainland China (GeoID : CN)
   - United Kingdom, instead of UK (GeoID : GB)
   - Hongkong, China (GeoID : HK)
   - Macau, China (GeoID : MO)
   - Taiwan, instead of Taiwan* (GeoID : TW)
   - Palestine, instead of West Bank and Gaza (GeoID : PS)
   - Vietnam, instead of Viet Nam (GeoID : VN)
   - Korea,South instead of South Korea (GeoID : KR)
   - Diamond Princess,Cruise Ship instead of Diamond Princess cruise ship, Others (no GeoID)
   
 - Country and Province/State : China and Australia
 - Country, Province/State and County/Admin Region : US and Canada
 - Country and external territories (using their own GeoID) : US, France, United Kingdom, Denmark and Netherland
 - WHO Location : Geneva, Switzerland change to Geneva, .WHO (with same GeoID - CH) to ensure WHO on the top list 
 - New Column TRANSFER IN and TRANSFER OUT to avoid double counting of patient on Cruise Ship
 
- Data from World Health Organization (WHO) - Event as they happened included (up to March 31st, 2020)
- Data from Johns Hopkins University, refined (up to April 2nd, 2020) 

Start analyze data using Jupyter Notebook

https://dataplatform.cloud.ibm.com/analytics/notebooks/v2/451952ba-05df-40d2-8cc3-30256c1b1184/view?access_token=70f746eba4374969515c6dbde376722ff486e173cf6ef3e14a20c2ee3b5f39a1

United States Daily Report (with States Plot)
https://dataplatform.cloud.ibm.com/analytics/notebooks/v2/2e444d14-2cc6-497e-9568-bbaeefc205fb/view?access_token=6ed9697cea1194e3b7154d148791ca3114a40b3c6edc06fcbbfe3ad37a4a190e



