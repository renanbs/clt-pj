inss_table = [
    {'sal_range': [0, 1045], 'value': 0.075, 'fixed': False},
    {'sal_range': [1045.01, 2089.6], 'value': 0.09, 'fixed': False},
    {'sal_range': [2089.61, 3134.4], 'value': 0.12, 'fixed': False},
    {'sal_range': [3134.41, 6101.06], 'value': 0.14, 'fixed': False},
    {'sal_range': [6101.07, 9999999999], 'value': 713.08, 'fixed': True}
]

irpf_table = [
    {'sal_range': [0, 1093.98], 'value': 0},
    {'sal_range': [1093.99, 2826.65], 'value': 0.075},
    {'sal_range': [2826.66, 3751.05], 'value': 0.15},
    {'sal_range': [3751.06, 4664.68], 'value': 0.225},
    {'sal_range': [4664.69, 9999999999], 'value': 0.275}
]


def _obtain_inss_discount(raw_salary: float):
    discount = 0
    found_range = False
    for inss in reversed(inss_table):
        if not found_range:
            if inss['sal_range'][0] < raw_salary < inss['sal_range'][1]:
                if not inss['fixed']:
                    discount = (raw_salary - inss['sal_range'][0]) * inss['value']
                    found_range = True
                    continue
                discount = inss['value']
                break
        else:
            discount = discount + (inss['sal_range'][1] - inss['sal_range'][0]) * inss['value']
    return discount


def _obtain_irpf_discount(base_salary: float):
    discount = 0
    found_range = False
    for irpf in reversed(irpf_table):
        if not found_range:
            if irpf['sal_range'][0] < base_salary < irpf['sal_range'][1]:
                discount = (base_salary - irpf['sal_range'][0]) * irpf['value']
                found_range = True
        else:
            discount = discount + (irpf['sal_range'][1] - irpf['sal_range'][0]) * irpf['value']

    return discount


if __name__ == '__main__':
    raw_salary = 9000
    inss_discount = _obtain_inss_discount(raw_salary)
    irpf_base_salary = raw_salary - inss_discount
    irpf_discount = _obtain_irpf_discount(irpf_base_salary)
    print(irpf_discount)
