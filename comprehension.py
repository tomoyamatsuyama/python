#内包表記

print([i for i in range(10)]) #1-9

print([i * 3 for i in range(10)])

print([i for i in range(10) if i % 2 == 0])

print(i for i in range(10) if i % 2 == 0) #ジェネレーター型
print({i for i in range(10) if i % 2 == 0}) #集合型
