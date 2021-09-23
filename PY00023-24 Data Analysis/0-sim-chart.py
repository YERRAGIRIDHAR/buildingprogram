import justpy as jp
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime 
from pytz import utc


data = pd.read_csv("reviews.csv", parse_dates=[1])
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Daily Average Rating'
    },
    subtitle: {
        text: 'Ratings'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 5'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: true
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text = "Analysis of Course Reviews", classes = "text-h6 q-pr-md text-weight-bolder text-center")
    p1 = jp.QDiv(a = wp, text = "These graphs represent course review analysis", classes= "text-h6 q-pr-md text-weight-medium text-center") #Component 2
    hc = jp.HighCharts(a = wp, options = chart_def)
    hc.options.title.text = "Average Rating by Day"
    hc.options.xAxis.categories = list(day_average.index) #Highchart are unable understad date colom so use this line
    hc.options.series[0].data = list(day_average['Rating'])

    return wp
jp.justpy(app)