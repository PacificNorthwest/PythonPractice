class RecordsIterator:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path, 'r') as file:
            for record in file:
                yield record

records = RecordsIterator('records.txt')
for i, record in enumerate(records):
    print(f'{i}: {record}', end='')
