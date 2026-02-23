donor = input('группа крови донора:').strip().upper()
pacient = input('группа крови пациета:').strip().upper()
if donor == pacient or donor == 'O':
    print('можно!')
else:
    print('нельзя!')
