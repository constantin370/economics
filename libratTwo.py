def ROE(clear_profit: float, revenue: float, Assets_at_the_last_reporting_date: float, own_capital: float)-> float:
    result = round((clear_profit / revenue) * (revenue / Assets_at_the_last_reporting_date) * (Assets_at_the_last_reporting_date / own_capital) * 100, 2)
    return result 

def Check_Data_One(control_panel: str) -> int:
    """Функция проверки и перевода данных c str во int"""
    try: 
        control_panel = int(control_panel)
        return control_panel
    except ValueError:
        print("Проверьте вводимые данные!")
        exit()

def Check_Data_Two(num: str) -> float:
    """Функция проверки и перевода данных c str во float"""
    try: 
        num = float(num)
        return num
    except ValueError:
        print("Вы ввели не число!")
        exit()

       