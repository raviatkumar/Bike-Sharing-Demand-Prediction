# Bike-Sharing-Demand-Prediction

![Alt text](https://github.com/raviatkumar/Bike-Sharing-Demand-Prediction/blob/main/Image/Bikes.png?raw=true)
## Problem Description

Currently Rental bikes are introduced in many urban cities for the enhancement of mobility comfort. It is important to make the rental bike available and accessible to the public at the right time as it lessens the waiting time. Eventually, providing the city with a stable supply of rental bikes becomes a major concern. The crucial part is the prediction of bike count required at each hour for the stable supply of rental bikes.

## Dataset Description

The dataset contains weather information (Temperature, Humidity, Windspeed, Visibility, Dewpoint, Solar radiation, Snowfall, Rainfall), the number of bikes rented per hour and date information.

Attribute Information:

Date : year-month-day

Rented Bike count - Count of bikes rented at each hour

Hour - Hour of he day

Temperature-Temperature in Celsius

Humidity - %

Windspeed - m/s

Visibility - 10m

Dew point temperature - Celsius

Solar radiation - MJ/m2

Rainfall - mm

Snowfall - cm

Seasons - Winter, Spring, Summer, Autumn

Holiday - Holiday/No holiday

Functional Day - NoFunc(Non Functional Hours), Fun(Functional hours)
## Problem and Data Description Insights

The following factors could affect the supply and demand for rental bikes:

Weather Condition:

In warmer climates with moderate sunlight, low humidity, quiet winds, and dry roads, people prefer to ride bike. People may prefer to drive a car than ride a bike if the weather is poor.

Demand for Rental Bikes:

People who don't own bike and those who migrate to cities temporarily need a bike and an easy means of transportation. Those who possess their own bike may not choose to rent one.

Availability of Rental Bikes:

Bike rental prices and availability at off-peak and rush hour times, as well as on weekdays and weekends.

Stable Supply of Rental Bike:

The weather conditions, demand, and supply sides may all have an impact on the stable supply of rental bikes.

## Summary and Conclusion:

In the morning and evening, many people rent bikes. The 4th and 18th hours are when the most bikes are leased when the weather is warm (20° to 28°C), the wind speed is between 2 and 3 m/s, and there is adequate visibility. More people hired bikes in the sixth months and most bikes are rented during non-holiday times.

With a r2 score of 93%, 88% , Extreme Gradient Boosting and Random Forest is the model that performs the best.

Therefore, there will be high supply and demand for bikes when there is mild sunlight, low humidity, no wind, and dry roads. People choose to hire and ride bikes.There will be a lot of demand and supply on both sides when the weather is pleasant.
