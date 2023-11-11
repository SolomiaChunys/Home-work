students = {'Rose': [5, 4, 3], 'Lisa': [5, 4, 5], 'Tomas': [4, 3, 3]}
result = {'best': ("", 1), 'worst': ("", 6)}

for name, marks in students.items():
    average = round(sum(marks) / len(marks), 1)
    if average >= float(result.get('best')[1]):
        result['best'] = (name, average)
    if average <= float(result.get('worst')[1]):
        result['worst'] = (name, average)

print(f"One of the best is {result.get('best')[0]} with average mark: {result.get('best')[1]}")
print(f"One of the worst is {result.get('worst')[0]} with average mark: {result.get('worst')[1]}")