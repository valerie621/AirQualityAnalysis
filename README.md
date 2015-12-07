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

![Load data] (image/loaddata.png)
##Parse Data

Now we have loaded the data and can access to it, the next step is to split the file by comma so that to parse data.
![Parse data] (image/parsedata.png)
##Explore Data

Now we can start to clean and select the data we want.

**1. List all cities in the dataset, then user can choose the city he wants to analyse.**

![List data] (image/listcities.png)

**2. If the city is found in the dataset, then begin extract data. If not, the user will get an error message.**

![Find data] (image/findcity.png)

**3. Clean and select the data we need about the city, here we select all parameters and their max values, then we can do map reduce to process data.**

![Clean data] (image/cleandata.png)

##Analyse Data

In order to find the factors contribute to the air quality in a particular location, we **find out the average value of each air parameter's max value**, then we **select the top 10 parameters** and assume these parameters are factors we want. 

If the location doesn't have 10 parameters, we just show all the parameters it has.

![analyse data] (image/analyse.png)

![analyse data] (image/barchart.png)



