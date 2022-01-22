# KVB Station Infos

This repository contains the list of KVB stations with a link to the additional info pages, like [Haltstellen der KVB](https://www.kvb.koeln/haltestellen/index.html).

---

## Data

The file `stations.csv` contains the name of the KVB stations and the link to the additional info pages. The file is a UTF-8 encoded text file and Comma Separated Value (CSV) formatted with a comma `,` as delimiter of the fields.

### Columns

Column Name | Notes
----------- | -----
`name` | Name of the station in German.
`infolink` | Link to the station information page.

## Tests

The tests ensure the consistency of every station in the list. Content errors aren't covered with these tests. 

```bash
pip3 install -r requirements.txt 
python3 -m pytest -q tests/cvs_format_tests.py
```
