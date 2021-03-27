# calendar-util
Simple calendar support for python `datetime.date`

## Setup

1. Install via pip (`pip install calendarutil`)
2. or via git (`git clone "https://github.com/github-suraj/calendar-util"`)

## Usage

### 1. Get first Monday of month 
```python
>>> from calendarutil.util import first
>>> first.first_monday_of_month(2021, 4)
datetime.date(2021, 4, 5)
```

### 2. Get list of first Monday of month for a year
```python
>>> from calendarutil.from_year import first
>>> first.first_monday_of_month(2021)        
[datetime.date(2021, 1, 4), datetime.date(2021, 2, 1), datetime.date(2021, 3, 1), datetime.date(2021, 4, 5), datetime.date(2021, 5, 3), datetime.date(2021, 6, 7), datetime.date(2021, 7, 5), datetime.date(2021, 8, 2), datetime.date(2021, 9, 6), datetime.date(2021, 10, 4), datetime.date(2021, 
11, 1), datetime.date(2021, 12, 6)]
```

### 3. Get list of first Monday of month for a date range
```python
>>> from datetime import date
>>> from calendarutil.from_range import first
>>> dt1 = date(2021, 3, 1)    
>>> dt2 = date(2021, 9, 1)
>>> first.first_monday_of_month(dt1, dt2)
[datetime.date(2021, 3, 1), datetime.date(2021, 4, 5), datetime.date(2021, 5, 3), datetime.date(2021, 6, 7), datetime.date(2021, 7, 5), datetime.date(2021, 8, 2), datetime.date(2021, 9, 6)]
```
## Supported frequency

- first
- second
- third
- fourth
- last

## Supported weekday

- monday
- tuesday
- wednesday
- thursday
- friday
- saturday
- sunday