# Databricks notebook source
from pyspark import sparkContext

sc = SparkContext()

sc = SparkContext("local", "simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()





