"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 13-Nov-2024
    Project: Report Automation
"""
from datetime import datetime
import csv
import matplotlib.pyplot as plt
from docxtpl import DocxTemplate, InlineImage
import docx2pdf

input_location = "automation/salesreportautomation"
output_location = "automation/salesreportautomation/output"
 
# Get the report start date and end date from user
def get_dates():
    """
        Description: Gets the user input for start date and end date of sales duration
        Parameters: None
        Returns: startdate and enddate
    """ 
    while True:
        print("Please Enter the Start Date and End Date in YYYY-MM-DD format..")    
        startdate = datetime.fromisoformat(input("Enter Start Date: "))
        startdate = startdate.date()
        enddate = datetime.fromisoformat(input("Enter End Date: "))
        enddate = enddate.date()
        if startdate <= enddate:
            return startdate, enddate
        else:
            print("startdate should be less than end date.")
            continue

# Extract and format the sales data based on dates duration
def get_sales_data(startdate, enddate):
    """
        Description: Read the CSV file to parse the sales data, convert the Date string 
        to DateTime format.
        Parameters: Two Dates - Start Date and End Date for sales duration
        Returns: Sales data as Dictionary for the duration of selected dates by user
        and column names of the report
    """
    selected_sales_data = []
    with open(f'{input_location}/daily_sales_data.csv', 'r') as rcsv:
        csv_reader = csv.DictReader(rcsv)
        # read the CSV and load the sales date
        for sales_data in csv_reader:
            # converting the date value from String format to Datetime format
            sales_data['Date'] = datetime.fromisoformat(sales_data['Date']).date()
            if (sales_data['Date'] >= startdate) and (sales_data['Date'] <= enddate):
                # Converting String from CSV to Numbers for Sale: Int, Revenue & Order val: Float, 
                sales_data['Sales'] = int(sales_data['Sales'])
                sales_data['Revenue'] = float(sales_data['Revenue'])
                sales_data['AvgOrder'] = float(sales_data['AvgOrder'])
                # Appending each dictionary in the selected date range to the list  
                selected_sales_data.append(sales_data)
        # Sales data dict keys
        sales_data_cols = list(selected_sales_data[0].keys())
    return sales_data_cols, selected_sales_data

# draw the graph based on the sales data
def draw_sales_graph(selected_sales_data):
    """
        Description: Draw the graph with sales data and save as jpg image
        Parameters: Sales Data Dictionary for slected periods by user
        Returns: The saved graph image location 
    """
    dates = []
    revenue = []
    for sales in selected_sales_data:
        for key, val in sales.items():
            if key == 'Date':
                dates.append(val)
            if key == 'Revenue':
                revenue.append(val)
    fig = plt.figure(figsize= (7.4, 4.9))
    
    # plotting a bar chart
    plt.bar(dates, revenue, width = 0.8, color = ['red', 'green'])
    plt.xlabel('Sales Dates')
    plt.ylabel('Sales Revenues')
    plt.title('Sales Revenue for Selected Dates')
    fig.autofmt_xdate(rotation=45)
    plt.savefig(f'{output_location}/sales.png')           
    # Sales Graph Location
    sales_graph = f'{output_location}/sales.png'
    return sales_graph

# Generate the docx report
def get_report_docx(startdate, enddate, sales_data_cols, selected_sales_data, sales_graph):
    doc = DocxTemplate(f'{input_location}/sales_report_template.docx')
    data = { "startdate": startdate, 
            "enddate": enddate,
            "sales_data_cols": sales_data_cols,
            "selected_sales_data": selected_sales_data,
            "sales_graph": InlineImage(doc, sales_graph)
            }
    doc.render(data)
    docx_report_name = f'{output_location}/sales_report_{startdate}_{enddate}.docx'
    doc.save(docx_report_name)
    print('docx report generated successfully')
    return docx_report_name

# Generate the pdf report
def get_report_pdf(startdate, enddate, docx_report_name):
    pdf_report_name = f'{output_location}/sales_report_{startdate}_{enddate}.pdf'
    # creating the pdf report
    docx2pdf.convert(docx_report_name, pdf_report_name)
    print('pdf report generated successfully')


if __name__ == '__main__':    
    # get the Start Date and End Date from User for Custom Sales Report    
    startdate, enddate = get_dates()
    # print(startdate, enddate)
    # get Sales Report Columns and Data for selected dates
    sales_data_cols, selected_sales_data = get_sales_data(startdate, enddate)
    # print(sales_data_cols)
    # print(selected_sales_data)
    sales_graph = draw_sales_graph(selected_sales_data)

    # Creating the docx report from the selected sales data
    docx_report_name = get_report_docx(startdate, enddate, sales_data_cols, selected_sales_data, sales_graph)

    # Creating the pdf report from the docx report
    get_report_pdf(startdate, enddate, docx_report_name)
