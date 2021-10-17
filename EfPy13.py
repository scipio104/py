key='my_var'
value=1.234
formatted= '{}={}'.format(key,value)
print(formatted)

old_way='%-10s=%.2f' % (key,value)

new_way='%(key)-10s = %(value).2f' % {
    'key':key, 'value':value}

reordered='%(key)-10s = %(value).2f' % {
    'value':value, 'key': key}

print(old_way)
print(new_way)
print(reordered)
