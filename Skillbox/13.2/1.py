def sum_numb(number):
    count = 0
    for i in range(1 , number + 1):
        count += i
    return count

inp_numb = int(input('Enter number: '))

result_promt = sum_numb(inp_numb)
print('Sum from 1 to',inp_numb,':',result_promt)
final_res = sum_numb(result_promt)
print('Sum from 1 to',result_promt,':', final_res)

