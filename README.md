# Justice Scraper

This program scrapes company information from the official register available at justice.cz. It was originally done as a project during my university studies, but I also use it to generate structured information about a company when inputting in company valuation documents.

Created by Adam Tůma

## Download

In the folder /JusticeScraper1.0 there are both Windows (.exe) and macOS (.app) versions of the program available, which can be executed with no installation.

*The Justice Scraper 2.0 version currently only updated for macOS.

## Usage of Justice Scraper
Just **input IČO** of a company to the program and choose whether to include "ostatní skutečnosti" in the file as well, and also whether to download the original pdf file from the justice.cz server.

The program will then **output .docx** file in the directory in which the program is.

![process](https://github.com/adamtuma/justice_scraper/blob/main/examples/process.png)

Examples of output documents for top 100 companies in the Czech Republic can be seen *'/examples/docs'*

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
The function will draw a map with markers for companies included in a dataframe. See map.html in examples for better visualization.

![map](https://github.com/adamtuma/justice_scraper/blob/main/examples/map.png)

## Contributing
Please hit me up in case of encountering some bugs.

## License
This tool is **not free to use** for business purposes. Please contact me, if you want to use this tool in your business.
