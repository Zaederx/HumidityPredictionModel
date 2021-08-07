# HumidityPredictionModel - Weather Data Proejct
 Looking at weather data to find trends and create a data model.
 
 I found some weather data, separated that data into training and test data sets. After that I looked for trends in the data to identify what factors correlated with the Humidity of a given day, by plotting these features against Humidty on scatter graphs.
 
 Once that was done, finding that temperature and Humidity had good correlation, I trained a linear regiression model using the sklearn module in python. I did the same with Visibility and Humidity. Then a third model was made considering both Temperature and Visibility in relation to Humidity.
 
 This gave favourable results when visually comparing the predicted values of the model against actual values Humidity from the training data on scatter graphs.
 
 I also created a python class that could work out the Rsquared value of the data and found that though it was on the lower end, still provided a reasonable prediction that was about 37% better than that of taking the mean of the actual values as a measure.
