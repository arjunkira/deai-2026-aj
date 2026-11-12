# Databricks notebook source
# MAGIC %md
# MAGIC #Welcome to Inceptez Technologies
# MAGIC Let us understand about creating notebooks, cells, markdowns & magical commands
# MAGIC https://fplogoimages.withfloats.com/actual/68009c3a43430aff8a30419d.png
# MAGIC ![](https://fplogoimages.withfloats.com/actual/68009c3a43430aff8a30419d.png)

# COMMAND ----------

# MAGIC %sh
# MAGIC ls /Workspace/Users/inceptezlabs@gmail.com/deai-2026/1_DATABRICKS_NOTEBOOK_FUNDAMENTALS

# COMMAND ----------

# MAGIC %md
# MAGIC ##Let us learn first about Magical Commands
# MAGIC Magical commands are used to apply different types of operations in a single notebook like linux, cloud storage (DBFS commands, ) python programming, spark sql querying etc.,... this is called as a concept of POLYGLOT<br>
# MAGIC **Important Magic Commands**
# MAGIC - %md: allows you to write markdown text to design the notebook (2_Explore_Notebook_Markdowns.ipynb)
# MAGIC - %run: runs a Python file or a notebook.
# MAGIC - %sh: executes shell commands on the cluster edge/client node.
# MAGIC <br>/home/irfan/folder1/file.txt - single linux server harddisk</br>
# MAGIC - %fs: allows you to interact with the Databricks file system (Datalake command (cloud storage s3/adls/gcs))
# MAGIC dbfs:/Volumes/workspace/default/datalake1/accounts.csv - cloud storage
# MAGIC - %sql: allows you to run Spark SQL/HQL queries (ISO/Ansi SQL).
# MAGIC - %python: switches the notebook context to Python.
# MAGIC - %pip: allows you to install Python packages.
# MAGIC
# MAGIC **Not Important Magic Commands or We learn few of these where we have Cloud(Azure) dependency**
# MAGIC - %scala: switches the notebook context to Scala.
# MAGIC - %r: switches the notebook context to R.
# MAGIC - %lsmagic: lists all the available magic commands.
# MAGIC - %config: allows you to set configuration options for the notebook.
# MAGIC - %load: loads the contents of a file into a cell.
# MAGIC - %who: lists all the variables in the current scope.

# COMMAND ----------

# MAGIC %md
# MAGIC ####How to run a notebook (inline) from the current notebook using %run magic command

# COMMAND ----------

# MAGIC %md
# MAGIC - usage of double quotes to mitigate any spaces in the path (not suppose to have)
# MAGIC - usage of absolute (for using some other code/data in a different hierarchy of path) & relative paths (for referring current path items)
# MAGIC - %run is used to run a notebook/py file inline in the current notebook, ie. current notebook with 50 LOC & child nb (some other nb) with 20 LOC , if we use %run it represent our current nb has 50+20 LOC

# COMMAND ----------

# MAGIC %run "/Workspace/Users/inceptezlabs@gmail.com/deai-2026/1_DATABRICKS_NOTEBOOK_FUNDAMENTALS/4_child_notebook"

# COMMAND ----------

# MAGIC %run "./sample_nb"

# COMMAND ----------

# MAGIC %md
# MAGIC ####How to run a linux commands inside a notebook using %sh magic command
# MAGIC This %sh will be performing local linux filesystem (single edge node operation)

# COMMAND ----------

# MAGIC %sh
# MAGIC pwd
# MAGIC ls -l /databricks/spark/python/pyspark/databricks
# MAGIC head /databricks/spark/python/pyspark/conf.py

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -l /Workspace/Users/inceptezlabs@gmail.com/deai-2026/1_DATABRICKS_NOTEBOOK_FUNDAMENTALS

# COMMAND ----------

# MAGIC %md
# MAGIC We are going to use Databricks Unity Catalog (We don't know about it yet)
# MAGIC to create tables and files under the volume (catalog/schema/volume/folder/files)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VOLUME IF NOT EXISTS workspace.default.volumewd38_datalake;

# COMMAND ----------

# MAGIC %md
# MAGIC ####Upload some sample data going into (Catalog(Unity) -> My Organization -> Workspace -> Default(schema) -> Tables/**Volumes**) <br> 
# MAGIC This %fs will be performing DBFS backed by Cloud filesystem (Cloud Storage Area Network (Multiple harddisks kept across datacenters))
# MAGIC <br>How to run a DBFS (like Hadoop) FS commands inside a notebook using %fs magic command to copy the uploaded data into some other volume from the uploaded volume
# MAGIC </br> this **%fs ls** is equalent to **hadoop fs -ls ** command we used in hadoop
# MAGIC </br> this **%fs ls** is listing DBFS files/folders which is a wrapper on top of some Cloud Storage (Cloud Datalake)

# COMMAND ----------

# MAGIC %fs ls "dbfs:///Volumes/workspace/default/volumewd38_datalake/dbfs_cloudfs_data/"

# COMMAND ----------

# MAGIC %fs cp "dbfs:/Volumes/workspace/default/volumewd38_datalake/dbfs_cloudfs_data/accounts.csv" "dbfs:/Volumes/workspace/default/volumewd38_datalake/dbfs_cloudfs_data/accounts_backup.csv"

# COMMAND ----------

# MAGIC %md
# MAGIC Learning for the first time the dbutils, we learn in detail later
# MAGIC Rather using fs command, we can use databricks utility command (comprehensive) to copy the data/any other filesystem operations in the DBFS

# COMMAND ----------

dbutils.fs.cp("dbfs:/Volumes/workspace/default/volumewd38_datalake/dbfs_cloudfs_data/accounts.csv","dbfs:/Volumes/workspace/default/volumewd38_datalake/dbfs_cloudfs_data/accounts_backup2.csv")
dbutils.fs.rm("dbfs:/Volumes/workspace/default/volumewd38_datalake/dbfs_cloudfs_data/accounts_backup2.csv")

# COMMAND ----------

# MAGIC %md
# MAGIC ####How to run a Spark SQL Queries inside a notebook using %sql magic command

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists default.cities3(id int,city string);
# MAGIC insert into default.cities3 values(3,'Mumbai'),(4,'Lucknow');
# MAGIC select count(*) from cities3;

# COMMAND ----------

#If we want to perform both Func based prog & Declartive prog.
spark.sql("select * from cities3").count()

# COMMAND ----------

# MAGIC %sql
# MAGIC update cities3 set city='Kolkata' where id=4;
# MAGIC select * from cities3;

# COMMAND ----------

# MAGIC %sql
# MAGIC --We are performing DDL operations which inturn access the metadata from Unitycatalog..
# MAGIC show create table cities3;

# COMMAND ----------

# MAGIC %md
# MAGIC ####How to run a Python Program inside a notebook using %python  magic command or by default the cell will be enabled with python interpretter only

# COMMAND ----------

def sqrt(a):
    return a*a

# COMMAND ----------

print("square root function call ",sqrt(10))

# COMMAND ----------

# MAGIC %md
# MAGIC In the python magic cell itself, we already have spark session object instantiated, <br>
# MAGIC so we can lavishly write spark programs

# COMMAND ----------

# MAGIC %md
# MAGIC ####How to install additional libraries in this current Python Interpreter using %pip magic command

# COMMAND ----------

# MAGIC %pip install pandas