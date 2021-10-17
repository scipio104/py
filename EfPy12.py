pantry=[
    ('avocados',1.25),
    ('bananas',2.5),
    ('cherries',15),
]
for i,(item,count) in enumerate(pantry):
    print('#%d: %-10s = %.2f' % (
    i+1,
    item.title(),
    round(count)))
