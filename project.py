import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def read_sales():
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data


def write_sales():
    data = read_sales()
    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
    return sales


def write_expenditures():
    data = read_sales()
    expenditure = []
    for row in data:
        expenditures = int(row['expenditure'])
        expenditure.append(expenditures)
    return expenditure


def monthly_sales():
    sales = write_sales()
    expenditure = write_expenditures()

    monthly_profit = [a - b for a, b in zip(sales, expenditure)]

    percentage_change = [int(0)]
    for previous, current in zip(sales, sales[1:]):
        percentage = round((((int(current) - int(previous)) / int(previous)) * 100), 1)
        percentage_change.append(percentage)

    print(f'\nList of total sales each month: £{sales}\n')
    print(f'List of total expenditures each month: £{expenditure}\n')
    print(f'List of total monthly profits: £{monthly_profit}\n')
    print(f'List of monthly sales changes as a percentage: {percentage_change}')

    print('\nThe total sales each month are:')
    for i, m in enumerate(zip(months, sales), start=1):
        print(m[0], ': £', m[1])

    print('\nThe total expenditures each month are:')
    for i, m in enumerate(zip(months, expenditure), start=1):
        print(m[0], ': £', m[1])

    print('\nThe total monthly profits are:')
    for i, m in enumerate(zip(months, monthly_profit), start=1):
        print(m[0], ': £', m[1])

    print('\nThe monthly sales changes as a percentage are:')
    for i, m in enumerate(zip(months, percentage_change), start=1):
        print(m[0], ':', m[1], '%')

    y_data_sales = np.array(sales)
    y_data_expenditures = np.array(expenditure)
    y_data_profits = np.array(monthly_profit)

    fig, axis = plt.subplots(nrows=2, ncols=1, figsize=(10, 7))
    fig.tight_layout(pad=4.0)
    fig.canvas.set_window_title('Sales Statistics (2018)')

    plt.subplot(2, 1, 1)
    plt.title('Total Sales and Expenditures Each Month (2018)', fontsize=14, fontweight='bold')
    plt.ylabel('Value (£)', fontsize=12)
    plt.xlabel('Month', fontsize=12)
    plt.ylim(0, 8000)
    plt.plot(months, y_data_sales, '-o', label='Sales')
    plt.plot(months, y_data_expenditures, '--o', label='Expenditures')
    plt.grid(alpha=0.3)
    plt.legend(loc=(0.2, 0.78), framealpha=1.0, edgecolor='k')

    plt.subplot(2, 1, 2)
    plt.title('Total Monthly Profits (2018)', fontsize=14, fontweight='bold')
    plt.ylabel('Profits (£)', fontsize=12)
    plt.xlabel('Month', fontsize=12)
    plt.ylim(-2500, 6000)
    plt.grid(alpha=0.3)
    plt.axhline(linestyle='--', color='k', alpha=0.4)
    plt.plot(months, y_data_profits, '-o', c='#008000')

    plt.tight_layout()
    plt.savefig('../CFG_Python_Data_Analysis_Project/salesgraphs.png', dpi=300)

    max_sale_value = max(sales)
    max_sale_index = sales.index(max_sale_value)

    if max_sale_index == 0:
        max_sale_month = 'January'
    elif max_sale_index == 1:
        max_sale_month = 'February'
    elif max_sale_index == 2:
        max_sale_month = 'March'
    elif max_sale_index == 3:
        max_sale_month = 'April'
    elif max_sale_index == 4:
        max_sale_month = 'May'
    elif max_sale_index == 5:
        max_sale_month = 'June'
    elif max_sale_index == 6:
        max_sale_month = 'July'
    elif max_sale_index == 7:
        max_sale_month = 'August'
    elif max_sale_index == 8:
        max_sale_month = 'September'
    elif max_sale_index == 9:
        max_sale_month = 'October'
    elif max_sale_index == 10:
        max_sale_month = 'November'
    else:
        max_sale_month = 'December'

    print(f'\nThe maximum sale month was {max_sale_month}, with a total of £{max_sale_value} worth of sales.')

    min_sale_value = min(sales)
    min_sale_index = sales.index(min_sale_value)

    if min_sale_index == 0:
        min_sale_month = 'January'
    elif min_sale_index == 1:
        min_sale_month = 'February'
    elif min_sale_index == 2:
        min_sale_month = 'March'
    elif min_sale_index == 3:
        min_sale_month = 'April'
    elif min_sale_index == 4:
        min_sale_month = 'May'
    elif min_sale_index == 5:
        min_sale_month = 'June'
    elif min_sale_index == 6:
        min_sale_month = 'July'
    elif min_sale_index == 7:
        min_sale_month = 'August'
    elif min_sale_index == 8:
        min_sale_month = 'September'
    elif min_sale_index == 9:
        min_sale_month = 'October'
    elif min_sale_index == 10:
        min_sale_month = 'November'
    else:
        min_sale_month = 'December'

    print(f'The minimum sale month was {min_sale_month}, with a total of £{min_sale_value} worth of sales.')

    year_total_sales = sum(sales)
    print(f'\nTotal sales of the year 2018: £{year_total_sales}')

    sale_year_avg = round((year_total_sales / 12), 2)
    print(f'Average yearly sale of 2018: £{sale_year_avg}')

    year_total_expenditures = sum(expenditure)
    print(f'\nTotal expenditures of the year 2018: £{year_total_expenditures}')

    expenditures_year_avg = round((year_total_expenditures / 12), 2)
    print(f'Average yearly expenditure of 2018: £{expenditures_year_avg}\n')

    year_total_profit = year_total_sales - year_total_expenditures
    print(f'Total profit in 2018: £{year_total_profit}')

    profit_year_avg = round((year_total_profit / 12), 2)
    print(f'Average yearly profit of 2018: £{profit_year_avg}')


def total_sales():
    data = read_sales()
    sales = []
    running_total = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

        total = sum(sales)
        running_total.append(total)

    print('\nThe running sales totals of each month are:')
    for i, m in enumerate(zip(months, running_total), start=1):
        print(m[0], ': £', m[1])


def read_sales_pandas():
    print('\nThe sales and expenditures data from each month in 2018:')
    df = pd.read_csv('sales.csv')
    print(df)
    print('')

    sales_info = df.describe()
    print('The sales and expenditures statistics from each month in 2018:')
    print(sales_info[['sales', 'expenditure']])


def seasonal_sales():
    sales = write_sales()
    expenditure = write_expenditures()

    winter_sales = sales[-1] + sales[0] + sales[1]
    spring_sales = sales[2] + sales[3] + sales[4]
    summer_sales = sales[5] + sales[6] + sales[7]
    autumn_sales = sales[8] + sales[9] + sales[10]

    print(f'\nTotal winter sales: £{winter_sales}')
    print(f'Total spring sales: £{spring_sales}')
    print(f'Total summer sales: £{summer_sales}')
    print(f'Total autumn sales: £{autumn_sales}\n')

    sales_season = input('What sales season is it? ').lower()

    if (sales_season == 'winter' and winter_sales >= 10000) or \
            (sales_season == 'spring' and spring_sales >= 10000) or \
            (sales_season == 'summer' and summer_sales >= 10000) or \
            (sales_season == 'autumn' and autumn_sales >= 10000):
        print('You are getting a 20% pay rise!')
    elif (sales_season == 'winter' and winter_sales >= 8000) or \
            (sales_season == 'spring' and spring_sales >= 8000) or \
            (sales_season == 'summer' and summer_sales >= 8000) or \
            (sales_season == 'autumn' and autumn_sales >= 8000):
        print('You are getting a 10% pay rise!')
    else:
        print('You are not getting a pay rise - work harder!')

    winter_expenditures = expenditure[-1] + expenditure[0] + expenditure[1]
    spring_expenditures = expenditure[2] + expenditure[3] + expenditure[4]
    summer_expenditures = expenditure[5] + expenditure[6] + expenditure[7]
    autumn_expenditures = expenditure[8] + expenditure[9] + expenditure[10]

    winter_profit = winter_sales - winter_expenditures
    spring_profit = spring_sales - spring_expenditures
    summer_profit = summer_sales - summer_expenditures
    autumn_profit = autumn_sales - autumn_expenditures

    print(f'\nTotal winter profit: £{winter_profit}')
    print(f'Total spring profit: £{spring_profit}')
    print(f'Total summer profit: £{summer_profit}')
    print(f'Total autumn profit: £{autumn_profit}\n')

    quarter = input("What season is this? ").lower()

    if (quarter == 'winter' and winter_profit >= 10000) or \
            (quarter == 'spring' and spring_profit >= 10000) or \
            (quarter == 'summer' and summer_profit >= 10000) or \
            (quarter == 'autumn' and autumn_profit >= 10000):
        print('Business is good!')
    elif (quarter == 'winter' and winter_profit < 0) or \
            (quarter == 'spring' and spring_profit < 0) or \
            (quarter == 'summer' and summer_profit < 0) or \
            (quarter == 'autumn' and autumn_profit < 0):
        print('Wait - we need to downsize and fire people!')
    else:
        print('Business is okay')


months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

monthly_sales()
total_sales()
read_sales_pandas()
plt.show()
seasonal_sales()
