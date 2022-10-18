# Program Heading
print("This program calculates the total cost of an order and prints a billing statement");

# Tax Rate
TAX_RATE = 0.0825

# Input Statements
Cost = float(input("Widget Cost (Please Enter Dollar Amount):"));
Quantity = float(input("# of Widgets to be Purchased (Please Enter Whole Number):"));
Discount_Rate = float(input("Discount to be Applied (Please Enter Decimal Value):"));

# Calculations
Sub_1 = Cost * Quantity;
Discount = Sub_1 * Discount_Rate;
Sub_2 = Sub_1 - Discount;
Tax = Sub_2 * TAX_RATE;
Total = Sub_2 + Tax;

# 2 Decimal Points
Sub_1 = "{:.2f}".format(Sub_1);
Discount = "{:.2f}".format(Discount);
Sub_2 = "{:.2f}".format(Sub_2);
Tax = "{:.2f}".format(Tax);
Total = "{:.2f}".format(Total);

# Billing Statement
print("Subtotal Before Discount: $ {:>8}".format(Sub_1));
print("Discount Applied:         $ {:>8}".format(Discount));
print("Subtotal After Discount:  $ {:>8}".format(Sub_2));
print("Tax:                      $ {:>8}".format(Tax));
print("Final Total:              $ {:>8}".format(Total));

# print("Kyle Hackett");
