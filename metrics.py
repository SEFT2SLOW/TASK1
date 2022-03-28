import sys
import psutil
import pandas as pd
from tabulate import tabulate

try:
    metric_to_print = sys.arvg[1]
except Exception:
    print ("Please select one argument (cpu | mem)")
    sys.exit(1)
    
    
if metric_to_print == "cpu":
    print("CPU")
    print("---")
    print(" ")
    print("cores")
    print("-----")
    print("-")
    print(psutil.cpu_count)
    print("-")
    print(" ")
    print("load average")
    print("-" * 12)
    table = [["1","5","15"], [psutil.getloadavg()[0], psutil.getloadavg()[1], psutil.getloadavg()[2]]]
    print(tabulate(table, headers = "firstrow"))
    print(" ")
    print("times")
    print("-----")
    
elif metric_to_print == "mem":
    print("MEMORY")
    print("-----")
    print(" ")
    print("virtual memory")
    print("-" * 15)
    data_virtual = dict(psutil.virtual_memory()._asdict())
    new_data_virtual = []
    for key, value in data_virtual.items():
        new_data_virtual.append([key, value])
    print(tabulate(new_data_virtual, tablefmt="simple"))
    print(" ")
    print("swap")
    print("----")
    data_swap = dict(psutil.swap_memory()._asdict())
    new_data_swap = []
    for key, value in data_swap.items():
        new_data_swap.append([key, value])
    print(tabulate(new_data_swap, tablefmt="simple"))

else:
    print("Wrong argument. Use (cup | mem)")
