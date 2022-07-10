# Interview Outline - Meter Readings
* All csv, database, code is located in InterviewMeterReadings dir
* Googling / internet research is allowed and encouraged
* Feel free to ask for clarification at any time
* We will request a screen share through teams

## Step 1: Reading CSV files 
* Open the file sample_readings.csv for reading 
* Read all lines from the file and display them in the application 
 
## Step 2: Organize the data in a list 
* The csv contains the following columns (without a header) 
  * Serial number (string) 
  * Manufacturer name (string) 
  * Manufacturer model (string) 
  * Install date (date) 
  * Address (string) 
  * Latitude 
  * Longitude 
  * TotalDailyUsage (in kWh) 
  * Unit of measure (hard-coded “kWh”) 
  * Reading timestamp (date/time), reading value (kWh) 
  * Repeat this 24 times for hourly readings, starting at midnight (00:00) up to 23:00 
    * Example row: 12345123,Elster,REX,2019/01/01,123 Elm Street,42.567,-80.124,25,kWh,2020/08/01 00:00,1.3,2020/08/01 01:00,1.2, …... 
* Read all lines and add them to a list 
* Sort this list by Manufacturer name and then by serial number 
* Remove previous displays and display a full list of Manufacturers and serial numbers  

## Step 3: Create Database Tables for data 
* From the data above, create database table(s) to represent this data 
* Insert rows from the data into your new tables: Display if the row(s) have been inserted (remove  previous displays) 
* Choose a serial number and display the peak meter reading, low meter reading, avg meter reading and the total number of readings 
* Using the same serial number and information but this time group them per day 

## Step 4: Modify the application to accept different file names 
* Allow the application to load other files 

## Step 5: SQL Queries
Consider the following reporting patterns we want to support. Write SQL queries to meet these requirements, and include them in SQL Scripts folder as sql files.
* Get a list of all unique meters and meter attributes
* Get a list of readings for a meter, given a serial number and date range.
* Calculate the total usagein kWhfor every meter over a date range (that is, how much electricitywas used by each meter, for billing purposes)

## Step 6: Gaps 
* Load sample_readings_gaps.csv file into your application 
* This file is missing some readings
* Develop an algorithm to fill in the blanks and estimate these missing values
