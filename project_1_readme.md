# Team Project #1

A statistical model that attempts to take stocks tracked on the S&P 500 and predict the stock price.

# Team Members
* Olha Yakushenko
* Divya Krishnamoorthy
* Sabarevasan Subbrahmanian
* Stuart Macgregor


# Project Details

## The Dataset and problem statement
After sufficient discussion, the S&P 500 dataset was chosen. It contains approximately 14 years worth of data for every company on the S&P 500. It also contains other data about each company that could be used to create more accurate models (Sector, Employee count, EBITDA, etc.)

The problem we are trying to answer with this dataset is this:
**Is there a way to predict a single company's stock value based off previous performance? If so, what data can provide the most accurate prediction?**

## Initial Approach
After downloading the dataset that covers the past 14 years of S&P 500 data, each member picked a single stock and attempted to analyze it in their own way. It was agreed that while using a regression analysis was mandatory, other models could be used afterwards to provide additional or more accurate data, if the team member wished. Afterward, the best looking model was chosen for this report.

# Conclusion
Following the work created by Ohla ([see ipynb for technical details](./src/team_project1_olha_yakushenko.ipynb)), it appears that there could be a correlation in predicting the price of a stock a day in advance, and is the model we have chosen to put forward (see ipynb for a more formal analysis). The work from Divya seems to corroborate this ([reference](./src/wfc_linear_regression.ipynb)) to some level, while the [work Stuart did](./src/stumac.ipynb) (attempting to predict a positive or negative return based on the previous 1-5 days stock close) yielded a poor model.

One concern with this model that was brought up was overfitting. The model's R<sup>2</sup> value was incredibly high (99%). This indicate that the model may be overtuned for this specific data set. Before making any attempts to use this model in production, more testing is needed, along with a more thorough analysis.

# Videos
Below are the list of videos from each team member. They discuss her/his experiences with the project, what they've learned, and any other information they feel is useful.

* [Olha Yakushenko](www.youtube.com/yourvideohere)
* [Divya Krishnamoorthy](www.youtube.com/yourvideohere)
* [Sabarevasan Subbrahmanian](https://drive.google.com/file/d/14WHRPk1uDRkEEpejAcpqlltoWoEBfHDy/view)
* [Stuart Macgregor](https://drive.google.com/file/d/1dT2tmzdpY61Bdogkp5C4yJcjKwIfkEtL/view?usp=sharing)
