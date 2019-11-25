# continue statements in for loop
# 処理のスキップ
# if vau == 'a':  ====> Trueの時、処理をスキップする

for vau in 'daiki and sei are my new friends':
    if vau == 'a':
        continue
    print(f'this stetement has {vau}')

# 'this stetement has',vau   ===   f'this stetement has {vau}'

print('---------------------------------------')

sounds = ['fan','chair','myself']
for sound in sounds[:-1]:
    print(sound)


print('---------------------------------------')


