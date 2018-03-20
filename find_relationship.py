import pandas as pd
import numpy as np

def take_ratio(season, field, location, takeMax=False):
    x, y = location

    dataDaily = pd.read_csv('daily_totals_%s_gp%d-%d_%s_takeMax=%s.csv' % (field, x, y, season, takeMax))
    dataHourly = pd.read_csv('weekly_max_%s_gp%d-%d_%s.csv' % (field, x, y, season))

    shape = np.shape(dataDaily)
    assert (shape == np.shape(dataHourly))
    ratio = np.zeros(shape)

    for i in shape[0]:
        for j in shape[1]:
            ratio[i, j] = dataDaily[i, j] / dataHourly[i, j]

    df = pd.DataFrame(ratio)
    result = "ratio_%s_gp%s-%s_%s.csv" % (field, x, y, season)
    df.to_csv(result, index=False, mode="w")