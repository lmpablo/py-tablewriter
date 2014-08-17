py-tablewriter
==============

Python class that converts a dictionary to an ASCII table

Sample Usage:

```python
tbl = [
    {
        'fname': 'Bill',
        'lname': 'Gates',
        'worth': 76,
        'source': 'Microsoft'
    }, 
    {
        'fname': 'Amancio',
        'lname': 'Ortega',
        'worth': 64,
        'source': 'retail'
    },
    {
        'fname': 'Warren',
        'lname': 'Buffet',
        'worth': 58.2,
        'source': 'Berkshire Hathaway'
    },
    {
        'fname': 'Larry',
        'lname': 'Ellison',
        'worth': 40,
        'source': 'Oracle'
    },
]
title = "Forbes Billionaires"
headers = ["fname", "lname", "worth", "source"]
settings = {
    '$uppercase_headers': False,
    'age': {
        'align': 'left'
    },
    'source': {
        'width': 50,
        'align': 'center'
    },
    'worth': {
        'prefix': '$',
        'align': 'right',
        'postfix': 'B'
    }
}

writer = TableWriter(padding=2, min_width=20)
writer.write_table(tbl, title, headers, settings)
```

Outputs:
```
+-----------------------------------------------------------------------------------------------------------------+
|                                               Forbes Billionaires                                               |
+-----------------------------------------------------------------------------------------------------------------+
|        fname       |        lname       |        worth       |                      source                      |
+-----------------------------------------------------------------------------------------------------------------+
|        Bill        |        Gates       |              $76B  |                     Microsoft                    |
|       Amancio      |       Ortega       |              $64B  |                      retail                      |
|       Warren       |       Buffet       |            $58.2B  |                Berkshire Hathaway                |
|        Larry       |       Ellison      |              $40B  |                      Oracle                      |
+-----------------------------------------------------------------------------------------------------------------+
```
