# weatherPredictionModel
 Looking at weather prediction data to find trends and create a one featured linear model.
 
 I found some weather data, separated that data into training and test data sets. After that I looked for trends in the data to identify what factors correlated with the Humidity of a given day, by plotting these features against Humidty on scatter graphs.
 
 Once that was done, finding that temperature and Humidity had good correlation, I trained a linear regiression model using the sklearn module in python.
 
 This gave favourable results when visutally comparing the predicted values of the model against actual values Humidity from the training data on scatter graphs.
 
 I then created a python class that could work out the Rsquared value of the data and found that though it was on the lower end, still provided a reasonable prediction that was about 36% better than that of taking the mean of the actual values as a measure.
