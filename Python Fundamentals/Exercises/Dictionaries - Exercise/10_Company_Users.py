# company_log = {}
#
# while True:
#     command = input()
#     if command == 'End':
#         break
#     company, employee = command.split(' -> ')
#
#     if company not in company_log:
#         company_log[company] = []
#         company_log[company].append(employee)
#     else:
#         if employee not in company_log[company]:
#             company_log[company].append(employee)
#
#
# company_log = dict(sorted(company_log.items()))
#
# for k in company_log.keys():
#     print(f'{k}')
#     for v in company_log[k]:
#         print(f'-- {v}')





# company_info = {}
#
# command = input()
# while command != 'End':
#     cmd_info = command.split(' -> ')
#     company_name = cmd_info[0]
#     employee_id = cmd_info[1]
#
#     if company_name not in company_info.keys():
#         company_info[company_name] = []
#
#     if employee_id not in company_info[company_name]:
#             company_info[company_name].append(employee_id)
#
#     command = input()
#
# for (company, employee_ids) in company_info.items():     # for (company, employee_ids) in sorted(company_info.items(), key=lambda kvp: kvp[0]):
#     print(company)
#
#     for emp_id in employee_ids:
#         print(f'-- {emp_id}')




company_log = {}

while True:
    command = input()
    if command == 'End':
        break
    company, employee = command.split(' -> ')

    if company not in company_log:
        company_log[company] = []
        company_log[company].append(employee)
    else:
        if employee not in company_log[company]:
            company_log[company].append(employee)

for k in company_log.keys():
    print(f'{k}')
    for v in company_log[k]:
        print(f'-- {v}')