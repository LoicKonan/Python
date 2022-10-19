## Project 01 - Cost of Widget

### Loic Konan

### Description

> This program that will calculate the total cost of widgets and print a billing statement.
> Constant => TAX_RATE = 0.0825
> Input. Write an input statement with an appropriate prompt for each:

* 1. Cost of one widget.
* 2. Total number of widgets to be purchased (quantity).
* 3. Discount rate. This must be entered as a decimal value. Ex. 40% discount will be entered as 0.40 when the program runs.

> Calculations. Write an assignment statement for each:

* 1. Subtotal1: Cost * Quantity
* 2. Discount: Subtotal * Discount Rate
* 3. Subtotal2: Subtotal1 - Discount
* 4. Tax Amount: Subtotal2 * TAX_RATE
* 5. Total: Subtotal2 + Tax Amount

> Output.
>
> * Print out a billing statement. You may choose what values to include in the statement. At a minimum, the statement should print the total due.


### RUN

```bash
python main.py
```

### Output Example
    
        ```bash
        Enter the cost of one widget: 10
        Enter the quantity of widgets to be purchased: 5
        Enter the discount rate: 0.40
    
        Subtotal: 50.0
        Discount: 20.0
        Tax Amount: 4.25
        Total: 25.75
        ```
        
### Files

|   #   | File               | Description | Status                  |
| :---: | ------------------ | ----------- | ----------------------- |
|   1   | [main.py](main.py) | Solution    | :ballot_box_with_check: |
