**Reads data from data files, place it in database, order racers by time and print pretty report in the browser using Flask and jinja2.**

-----

## Description

This app reads data from 2 files, order racers by time and print report that shows their time for the best loop, for example:

```bash
1. Daniel Ricciardo      | RED BULL RACING TAG HEUER    | 1:12.013

2. Sebastian Vettel      | FERRARI 						| 1:12.415

3. ...

16. Brendon Hartley      | SCUDERIA TORO ROSSO HONDA 	| 1:13.179

17. Marcus Ericsson  	 | SAUBER FERRARI  				| 1:13.265

```

-----

## Running

 The script runs the local server *http://localhost:5000/*, where you can navigate and find information about Monaco 2018 racing.

## How to use

1. To see the full report, go to *http://localhost:5000/report*.

2. To see the list with drivers go to *http://localhost:5000/report/drivers*.

3. To get an information about specific driver, you can tap on his code-nickname on the right in *drivers* list. 
It includes his position, full name, team, best lap time and short info from Wikipedia with external link to the Wikipedia's page with full information.

Also you can write down the code in the search-field on the middle of every page.

4. You can change the order parameter (ascending or descanding) by pressing each of buttons with arrows right above on the navigation bar.

5. If the data is incorrect, you will receive an accordant Error:
```bash
*** ERROR. Marcus Ericsson   | SAUBER FERRARI  	 ----- INVALID DATA! -----
```

The *data* here is 2 log files start.log and end.log that contain start and end data of the best lap for each racer of Formula 1 - Monaco 2018 Racing and the txt file with abbreviatures for the encrypting.

-----

## Installing

You should install this module directly using pip:
```bash
pip install -i https://test.pypi.org/simple/ report-of-racing-using-flask-by-r4bc1
```


[Also you can find this package here.](https://test.pypi.org/project/report-of-racing-by-r4bc1/)**


-----

## Requirements

Click==7.0

Flask==1.0.2

itsdangerous==1.1.0

Jinja2==2.10

MarkupSafe==1.1.0

Werkzeug==0.14.1

wikipedia==1.4.0

-----
## How it works

To operate with the data files it has 2 functions:
**encryption_of_abbreviations(file_path)**, **encryption_of_log(file_path)**.

Each of them makes a dictionary from the according data file, where the keys are the drivers shortcuts, and values - their names, time etc.

The **build_report(folder_path)** function uses functions described above to get this data in a correct way and makes the final dictionary that contains information about each driver and his lap time.


The **prepare_the_report(data, order)** takes the dictionary from the **build_report(folder_path)** function, turning it tot the OrderedDict, order by the time. The *order* argument is used for telling function in what manner represent the result - ascending or descending. Then it adds drivers and their final time to the list.
If the data for one or more racers is incorrect - it shows this racer with according message:

```bash
***** ERROR. Marcus Ericsson   | SAUBER FERRARI  	 - INVALID DATA!
```

## Testing

To test this application, type in the command promt the following:
```bash
py test_server.py
```

To get described report about testing, you have to install via pip the *coverage* module, and type in:
```bash
coverage run -m unittest discover
```
```bash
coverage report
```

This will return you a list inside PowerShell with the results. To convert it to the .html file and than open in web browser, use:
```bash
coverage html
```