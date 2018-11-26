import bpy

sel_obj = bpy.context.selected_objects

print('starting...')

output = ''

file = open('blender_road.txt', 'w')

total = 0

for i in sel_obj:
    output += str(i.location[0]) + ' ' + str(i.location[1]) + '\n'
    print(output + i.name)
    total += 1
 
print(str(total-1) + '\n' + output, file=file)
file.close()
print('done')
