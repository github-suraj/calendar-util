# calendar-util
Simple calendar support for python `datetime.date`

## Setup

1. Install via pip (`pip install calendarutil`)
2. or via git (`git clone "https://github.com/github-suraj/calendar-util"`)

## Usage : 1 : get date on a particular day of month

### 1. Get first Monday of month

In this module, all the methods take input arguments as `year` and `month`.

```python
>>> from calendarutil.month import util
>>> util.first_monday_of_month(2021, 4)
datetime.date(2021, 4, 5)
```

### 2. Get list of first Monday of month for a year

In this module, all the methods take input argument as `year`.

```python
>>> from calendarutil.month import from_year
>>> from_year.first_monday_of_month(2021)
[datetime.date(2021, 1, 4), datetime.date(2021, 2, 1), datetime.date(2021, 3, 1), datetime.date(2021, 4, 5), datetime.date(2021, 5, 3), datetime.date(2021, 6, 7), datetime.date(2021, 7, 5), datetime.date(2021, 8, 2), datetime.date(2021, 9, 6), datetime.date(2021, 10, 4), datetime.date(2021, 
11, 1), datetime.date(2021, 12, 6)]
```

### 3. Get list of first Monday of month for a date range

In this module, all the methods take input arguments as `date object` for `start` and `end` date.

```python
>>> from datetime import date
>>> from calendarutil.month import from_range
>>> dt1 = date(2021, 3, 1)
>>> dt2 = date(2021, 9, 1)
>>> from_range.first_monday_of_month(dt1, dt2)
[datetime.date(2021, 3, 1), datetime.date(2021, 4, 5), datetime.date(2021, 5, 3), datetime.date(2021, 6, 7), datetime.date(2021, 7, 5), datetime.date(2021, 8, 2), datetime.date(2021, 9, 6)]
```
#### Supported frequency

- first
- second
- third
- fourth
- last

#### Supported weekday

- monday
- tuesday
- wednesday
- thursday
- friday
- saturday
- sunday

## Usage : 2 : get date on first/last day/weekday of month

In this module, all the methods take input arguments as `year` and `month`.

### 1. Get first day of month 
```python
>>> from calendarutil.month import first_day_of_month
>>> first_day_of_month(2021, 5)
datetime.date(2021, 5, 1)
```

### 2. Get first weekday of month 
```python
>>> from calendarutil.month import first_weekday_of_month
>>> first_weekday_of_month(2021, 5)
datetime.date(2021, 5, 3)
```

### 3. Get last day of month 
```python
>>> from calendarutil.month import last_day_of_month
>>> last_day_of_month(2021, 2) 
datetime.date(2021, 2, 28)
```

### 4. Get last weekday of month 
```python
>>> from calendarutil.month import last_weekday_of_month
>>> last_weekday_of_month(2021, 2)
datetime.date(2021, 2, 26)
```

## Usage : 3 : get date on first/last day/weekday of quarter

In this module, all the methods take input arguments as `year` and `quarter number`.

### 1. Get first day of quarter 
```python
>>> from calendarutil.quarter import first_day_of_quarter
>>> first_day_of_quarter(2022, 1)
datetime.date(2022, 1, 1)
```

### 2. Get first weekday of quarter 
```python
>>> from calendarutil.quarter import first_weekday_of_quarter
>>> first_weekday_of_quarter(2022, 1)
datetime.date(2022, 1, 3)
```

### 3. Get last day of quarter 
```python
>>> from calendarutil.quarter import last_day_of_quarter
>>> last_day_of_quarter(2022, 4)
datetime.date(2022, 12, 31)
```

### 4. Get last weekday of quarter 
```python
>>> from calendarutil.quarter import last_weekday_of_quarter
>>> last_weekday_of_quarter(2022, 4)
datetime.date(2022, 12, 30)
```

## Show your Support
Give us a :star2: if this project helped you!

## License
Copyright © 2021 [Suraj Jaiswal](https://github.com/github-suraj)
