# MemoryCasheDataBase_Client

![PyPI](https://img.shields.io/pypi/v/clubhouse_api?color=orange) ![Python 3.6, 3.7, 3.8](https://img.shields.io/pypi/pyversions/clubhouse?color=blueviolet) ![GitHub Pull Requests](https://img.shields.io/github/issues-pr/peopl3s/club-house-api?color=blueviolet) ![License](https://img.shields.io/pypi/l/clubhouse-api?color=blueviolet) ![Forks](https://img.shields.io/github/forks/peopl3s/club-house-api?style=social)

**Python API module for MemoryCasheDataBase_Server** - this module is a Python client library for connect to DB MemoryCasheDataBase_Server


**MemoryCasheDataBase** is collaborative project management that streamlines and refines your existing workflow. The intuitive and powerful project management platform loved by software teams of all sizes. [Clubhouse](https://clubhouse.io) is here.


## Installation

Install the current version with [PyPI](https://pypi.org/project/MemoryCasheDataBase_Client/):

```bash
pip install MkCasheDB_API 
```

## Start project 
```python 
import MkCasheDB_API; 

```


## Example

Add record(s) in DataBase.

```python

NewMemoryCasheDataBase_Client : MkCasheDB_API.MemoryCasheDataBase_Client = MkCasheDB_API.MemoryCasheDataBase_Client()

print(NewMemoryCasheDataBase_Client.AddRangeRecords( RequestDictionary = dict( ( ( "Key", "Value" ), ( "Key #2", "Value #2" ) ) ) )) 

``` 

Change record(s) in DataBase. 

```python 

NewMemoryCasheDataBase_Client : MkCasheDB_API.MemoryCasheDataBase_Client = MkCasheDB_API.MemoryCasheDataBase_Client()

print(NewMemoryCasheDataBase_Client.ChangeRangeRecords( RequestDictionary = dict( ( ( "Key", "ValueNew" ), ) ) )) 

```	

Get record(s) from DataBase. 

```python 

NewMemoryCasheDataBase_Client : MkCasheDB_API.MemoryCasheDataBase_Client = MkCasheDB_API.MemoryCasheDataBase_Client()

print(NewMemoryCasheDataBase_Client.GetRangeRecords( RequestTuple = ( "Key", "Key #2" ) )) 

``` 

Delete record(s) from DataBase. 

```python 

NewMemoryCasheDataBase_Client : MkCasheDB_API.MemoryCasheDataBase_Client = MkCasheDB_API.MemoryCasheDataBase_Client()

print(NewMemoryCasheDataBase_Client.DeleteRangeRecords( RequestTuple = ( "Key #2", ) )) 

``` 

Add file in DataBase. 

```python 

NewMemoryCasheDataBase_Client : MkCasheDB_API.MemoryCasheDataBase_Client = MkCasheDB_API.MemoryCasheDataBase_Client() 

with open("Image.JPG", "rb") as FileRead: 
    print(NewMemoryCasheDataBase_Client.AddFile("ImageDB", FileRead.read())); 

```

Get file from DataBase. 

```python 

NewMemoryCasheDataBase_Client : MkCasheDB_API.MemoryCasheDataBase_Client = MkCasheDB_API.MemoryCasheDataBase_Client() 

with open("ImageCopy.JPG", "wb") as FileWrite: 
    FileWrite.write(NewMemoryCasheDataBase_Client.GetFile("ImageDB")); 

``` 


## Contributing

Bug reports and/or pull requests are welcome


## License

The module is available as open source under the terms of the [Apache License, Version 2.0](https://opensource.org/licenses/Apache-2.0)


