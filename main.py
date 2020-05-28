inss_table = {
  '1': {'sal_range': [0, 1045], 'value': 0.075, 'fixed': False},
  '2': {'sal_range': [1045.01, 2089.6], 'value': 0.09, 'fixed': False},
  '3': {'sal_range': [2089.61, 3134.4], 'value': 0.12, 'fixed': False},
  '4': {'sal_range': [3134.41, 6101.06], 'value': 0.14, 'fixed': False},
  '5': {'sal_range': [6101.07, 9999999999], 'value': 713.08, 'fixed': True},
}

raw_salary = 9000

for _, inss in inss_table.items():
  if raw_salary > inss['sal_range'][0] and raw_salary < inss['sal_range'][1]:
    inss_discount = inss['value']
    if not inss['fixed']:
      