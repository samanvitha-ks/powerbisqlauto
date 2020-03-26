# powerbisqlauto
PowerBI SQL automation

Apporach:

1.	Create PBIX Reports for all the DAX functions or Use existing DAX functions
Deepa: Best to use the existing or a simple dashboard with few functions
2.	Trace SQL query generated for each DAX function – Both SC930 and PowerBI Trace file.
Deepa: As we discussed, Just pick one simple generated SQL query for POC.
3.	Prepare an input file with all the Queries traced.
4.	Develop a python script to run input file against the database and export the SQL results 
5.	Manually capture the Expected result from PBIX report for each of the DAX function in an excel
6.	Compare the Step 4 results with step 5.
7.	Develop a report with PASS or FAIL or Error Status.

