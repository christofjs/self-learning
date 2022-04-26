from multiprocessing import dummy
import pandas as pd
import matplotlib as plt
from matplotlib import pyplot
import numpy as np
import requests

def download(url, newFile):
    res = requests.get(url)
    if res.status_code == 200:
        with open(newFile, "wb") as f:
            f.write(res.content)
    else: print("Download Error")

def readAndSetHeaders(fileToRead):
    headers = ["symboling","normalized-losses", "make", "fuel-type",
               "aspiration", "num-of-doors", "body-style", "drive-wheels",
               "engine-location", "wheel-base", "length", "width", "height",
               "curb-weight", "engine-type", "num-of-cylinders", "engine-size",
               "fuel-system", "bore", "stroke", "compression-ratio",
               "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
    return pd.read_csv(fileToRead, names=headers)

def formatMissingData(df):
    df.replace('?', np.nan, inplace=True)

def countMissingValues(missingDF):
    for column in missingDF.columns.values.tolist():
        print(column)
        print(missingDF[column].value_counts())
        print("")

def replaceMissingWithAverage(df):
    # normalized losses
    avgNormalizedLoss = df["normalized-losses"].astype("float").mean(axis=0)
    df["normalized-losses"].replace(np.nan, avgNormalizedLoss, inplace=True)

    # stroke
    avgStroke = df["stroke"].astype("float").mean(axis=0)
    df["stroke"].replace(np.nan, avgStroke, inplace=True)

    # bore
    avgBore = df["bore"].astype("float").mean(axis=0)
    df["bore"].replace(np.nan, avgBore, inplace=True)

    # horsepower
    avgHorsepower = df["horsepower"].astype("float").mean(axis=0)
    df["horsepower"].replace(np.nan, avgHorsepower, inplace=True)

    # peak-rpm
    avgPeakRPM = df["peak-rpm"].astype("float").mean(axis=0)
    df["peak-rpm"].replace(np.nan, avgPeakRPM, inplace=True)

def replaceMissingByFrequency(df):
    # num-of-doors
    mostFrequent = df["num-of-doors"].value_counts().idxmax()
    df["num-of-doors"].replace(np.nan, mostFrequent, inplace=True)

def removeMissing(df):
    # price
    df.dropna(subset=["price"], axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)

def correctTypes(df):
    df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
    df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
    df[["price"]] = df[["price"]].astype("float")
    df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

def mpgUnitConversion(df):
    df["city-mpg"] = 235/df["city-mpg"]
    df.rename(columns={'"city-mpg"':'city-L/100km'}, inplace=True)
    df["highway-mpg"] = 235/df["highway-mpg"]
    df.rename(columns={'"highway-mpg"':'highway-L/100km'}, inplace=True)

def normalizeDimensions(df):
    df['length'] = df['length']/df['length'].max()
    df['width'] = df['width']/df['width'].max()
    df['height'] = df['height']/df['height'].max()

def showHorsepowerPlot(df):
    df["horsepower"] = df["horsepower"].astype(int, copy=True)
    plt.pyplot.hist(df["horsepower"])
    plt.pyplot.xlabel("horsepower")
    plt.pyplot.ylabel("count")
    plt.pyplot.title("horsepower bins")
    plt.pyplot.show()

def binHorsepower(df):
    df["horsepower"] = df["horsepower"].astype(int, copy=True)
    bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
    binNames = ["Low", "Medium", "High"]
    df["horsepower-binned"] = pd.cut(df["horsepower"], bins, labels=binNames,
                                     include_lowest=True)
    # pyplot.bar(binNames, df["horsepower-binned"].value_counts())
    plt.pyplot.hist(df["horsepower-binned"], bins = 3)
    plt.pyplot.xlabel("horsepower")
    plt.pyplot.ylabel("count")
    plt.pyplot.title("horsepower bins")
    plt.pyplot.show()

def fuelDummies(df):
    dummyOne = pd.get_dummies(df["fuel-type"])
    dummyOne.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)
    df = pd.concat([df, dummyOne], axis=1)
    df.drop("fuel-type", axis=1, inplace=True)
    return df

def aspirationDummies(df):
    dummyOne = pd.get_dummies(df["aspiration"])
    print(dummyOne.head())
    dummyOne.rename(columns={'std':'asp-std', 'turbo':'asp-turbo'}, inplace=True)
    df = pd.concat([df, dummyOne], axis=1)
    df.drop("aspiration", axis=1, inplace=True)
    return df

if __name__ == "__main__":
    filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
    outputFile = "auto.csv"
    download(filename, outputFile)
    df = readAndSetHeaders(outputFile)
    formatMissingData(df)
    missingData = df.isnull()
    print(countMissingValues(missingData))
    replaceMissingWithAverage(df)
    replaceMissingByFrequency(df)
    removeMissing(df)
    correctTypes(df)
    # showHorsepowerPlot(df)
    # binHorsepower(df)
    df = fuelDummies(df)
    print(df.to_string())
    df = aspirationDummies(df)
    df.to_csv('clean_auto.csv')
