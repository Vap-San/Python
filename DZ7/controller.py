import view
import dic
from logg import logging

#type_value = 0


def button_click():
    #global type_value

    type_value = view.choice_type_numbers()
   
    if type_value == "1":
        value_a = view.get_value_q()
        value_b = view.get_value_q()
        print(f"Исходные числа: {value_a}, {value_b}")
    else:
        value_a = view.get_value_complex()
        value_b = view.get_value_complex()
        print(f"Исходные числа: {value_a}, {value_b}")

    oper = view.get_operator()

    func = dic.dic_procedure[oper]
    func.init(value_a, value_b)
    result = func.do_it()

    operation = dic.dic_operation[oper]
    symbol = dic.dic_symbol[oper]

    view.get_result(result)
    logging.info(f"{operation}: {value_a} {symbol} {value_b} = {result}")
