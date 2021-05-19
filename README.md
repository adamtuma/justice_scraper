# Justice Scraper

This program scraper company information from the official register available at justice.cz

Created by Adam Tůma

## Download

In the folder /JusticeScraper1.0 there are both Windows (.exe) and macOS (.app) versions of the program available, which can be executed with no installation.

## Usage of Justice Scraper
Just **input IČO** of a company to the program

The program will then **output .docx** file in the directory in which the program is.

Examples of output documents for top 100 companies in the Czech Republic can be seen *'/examples/docs'*

![process](https://github.com/adamtuma98/justice_scraper/blob/main/examples/process.png?raw=true)

## Additional features included in justice.ipynb
The Jupyter Notebook has other useful functions which are not used within the main program.

Here are examples of functions available:
```python
getBasicInfo(IČOs)
```
Providing a list of IČOs to this function will return pandas dataframe including the main basic information for all companies:
- Company name / Název společnosti
- Date of registration / Datum vzniku
- File number / Spisová značka
- Address / Sídlo
- Legal form / Právní forma

```python
getCoordinates(df)
```
Once provided with the output of getBasicInfo() the function will append latitude and longitude of all company addresses.

```python
getMap(df)
```
The function will draw a map with markers for companies included in a dataframe.

![map](https://github.com/adamtuma98/justice_scraper/blob/main/examples/map.png?raw=true)

## Contributing
Please hit me up in case of encountering some bugs.