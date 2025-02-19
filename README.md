# python-scripts

A repository to store my Python script templating.

## Usage of find_gift_in_budget.py

```bash
$ python3 ./find_gift_in_budget.py --help

usage: find_gift_in_budget.py [-h] -b BUDGET [-c CATEGORY] [--id ID]

options:
  -h, --help                        show this help message and exit
  -b BUDGET, --budget BUDGET        User's budget to find products
  -c CATEGORY, --category CATEGORY  Store category to filter products on.
  --id ID 
```

```bash
$ python3 ./find_gift_in_budget.py -b 20
Creating products-in-budget-20240222-1313 that contains products that are within the budget...

$ python3 ./find_gift_in_budget.py --budget 20 --category electronics
There are no products in budget.

$ python3 ./find_gift_in_budget.py --budget 200 --category jewelery
Creating products-in-budget-20240222-1315.json that contains products that are within the budget.
```
