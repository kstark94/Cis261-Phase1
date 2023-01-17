#
#
#
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
#for the next three functions, you need to convert the input to a float, e.g., varname = float(input('descripion of input:  '))
#write the GetHoursWorked function
def GetHoursWorked():
    hours = float(input("Enter the number of hours worked: ")) 
    return hours

#write the GetHourlyRate function
def GetHourlyRate():
    GethourlyRate = float(input("How much is this emplyee paid an hour: ")) 
    return hourlyrate
# write the GetTaxRate function

def GetTaxRate():
    taxrate = float(input("How much is this employee taxed: ")) 
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print("Name:  ", empname) 
    print("Hours Worked: ", f"{hours:,.2f}")
    # write the lines of code to display hourlyrate, grosspay, taxrate, incometax and netpay with correct formatting
    # taxrate needs to be formatted as percentage
    print("Employee: " (empname))
    print("Hours: " (hours))
    print("Hourly Wage: " (hourlyrate))
    print("Gross Pay: " (grosspay))
    print("Taxrate: {taxrate:,.2%}" (taxrate))
    print("Income Tax: "(incometax))
    print("Net Pay: "(netpay))

def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    # write the code to print  TotGrossPay, TotTax, and TotNetpay with 2 decimal places
    print(f"Total gross pay: {TotGrossPay:,.2f}")
    print(f"Total tax: {TotTax:,.2f}")
    print(f"Total pay: {TotNetPay:,.2f}")

if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        # write the code to assign to hours the return value from GetHoursWorked
         
        # write the code to assign to hourlyrate the return value from GetHourlyRate
        
        # write the code to assign to taxrate the return value from GetTaxRate
       
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        TotHours += hours
        # write the code to increment the other total variables with the appropriate values



    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
