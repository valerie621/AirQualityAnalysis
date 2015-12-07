#Air Quality in Particular Location

##Project Abstract:

Use air quality data http://www3.epa.gov/airdata/ad_data.html (Links to an external site.) and bring the factors that are contributing in  a particular geo location. 

##Procedures

1, Download data and add dataset to Object Storage

2, Clean and Select data

    2.1 split data
    
    2.2 map data
    
    2.3 find data you need
    
3, Analyse your data and get a conclusion

##Load Data

The data I use is download in http://www3.epa.gov/airdata/ad_data.html, it's an annual summary of 2015 of the whole country, the dataset name is *annual_all_2015.csv*

##Parse Data

Now we have loaded the data and can access to it, the next step is to split the file by comma so that to parse data.

##Explore Data

Now we can start to clean and select the data we want.
**1. List all cities in the dataset, then user can choose the city he wants to analyse.**

**2. If the city is found in the dataset, then begin extract data. If not, the user will get an error message.**

