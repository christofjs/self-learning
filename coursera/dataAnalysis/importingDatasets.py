import pandas as pd
import numpy as np
import requests
import asyncio

async def download(url, filename):
    res = requests.get(url)
    if res.status_code == 200:
        with open(filename, "wb") as f:
            f.write(res.content)
        
async def getAutoFile():
    path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
    outputPath = "auto.csv"
    await download(path, outputPath)
    df = pd.read_csv(outputPath, header=None)
    return df

def lastNRows(df, rows):
    print("The last rows of the dataframe")
    print(df.tail(rows))

def firstNRows(df, rows):
    print("The first rows of the dataframe")
    print(df.head(rows))

def createHeaders(df):
    headers = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
    df.columns = headers

def reformatAndRemoveEmptyData(df):
    dfTemp = df.replace('?', np.NaN)
    return dfTemp.dropna(subset=["price"], axis=0)

def columnNames(df):
    print(df.columns)

def exportToCSV(df, outputFile):
    df.to_csv(outputFile, index=False)

def describeLengthCompressionratio(df):
    print(df[['length', 'compression-ratio']].describe())

if __name__ == "__main__":
    df = asyncio.run(getAutoFile())
    firstNRows(df, 5)
    lastNRows(df, 10)
    createHeaders(df)
    firstNRows(df,20)
    df = reformatAndRemoveEmptyData(df)
    firstNRows(df,20)
    columnNames(df)
    exportToCSV(df, "auto.csv")
    describeLengthCompressionratio(df)
