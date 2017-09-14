A **C**omma **S**eparated **V**alues (CSV) file is a useful way to store tabulated data. This type of file is simple for programming languages to read, and it can easily be imported into other applications such as Spreadsheets.

- First, you need to import the `writer` class from the `csv` module.

```python
from csv import writer
```

- Next, create a new file, and specify that each line of data is going on a new line.

```python
import csv
with open('some.csv', 'w', newline='') as f:
```

- Then set up a writer object to write lines to the CSV file.

```python
import csv
with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
```

- Then you can write a line of data. By default, the data needs to be in form of a list.

```python
import csv
with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Here', 'is', 'some', 'data'])
```
