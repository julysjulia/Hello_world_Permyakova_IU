right = 'направо'
left = "налево"
straight = "прямо"
desination = input()
if desination == right:
    print('Направо пойдёшь — коня потеряешь, себя спасёшь')
elif desination == left:
    print('налево пойдёшь — себя потеряешь, коня спасёшь')
elif desination == straight:
    print('прямо пойдёшь — и себя, и коня потеряешь')
else:
    print('а другого не дано')