# Databricks notebook source
# MAGIC %sql
# MAGIC select * from hive_metastore.default.nyc_taxi limit 3;

# COMMAND ----------

name = "tomy"
print (f"hello {name}")
%run ./Sample_notebook01
print (f"Welcome back {fullname}")
