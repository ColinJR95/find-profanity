#get a file 

fo = open('test.txt', 'w')
#get some info
print('The name of file', fo.name)

#is the file closed?

print('is it closed', fo.closed)
#shows what opening mode it is in
print('what mode is it in?: ', fo.mode)
#write to file
fo.write('Straight up im tryna fuck')
fo.write('   ,thats crazy')
fo.close()

#if you want to open the file again and need to edit make sure that you append

fo = open('test.txt', 'a')
fo.write('   yo')
fo.close()

fo = open('test.txt', 'r+')

profanity = fo.read()
if 'fuck' in open('test.txt').read():
    print("yes it is")


 


