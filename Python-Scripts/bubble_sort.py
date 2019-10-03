def bubble_sort(data):
    new_data = data
    for i in range(len(new_data)):
        if new_data[i] <= new_data[i + 1]:
            continue
        else:
            new_data[i] = new_data[i + 1]
    return new_data
        
a = [3, 1, 4, 1, 5, 9, 2, 6]
print(f'The original list {a} sorted:  {bubble_sort(a)}.')