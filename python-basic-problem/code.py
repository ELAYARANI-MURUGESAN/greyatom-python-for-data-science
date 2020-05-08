# --------------
#step 1:
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class=class_1+class_2
print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)
#step 2:
courses={"Math":65,"English":70,"History":80,"French":70,"Science":60}
values=(65,70,80,70,60)
total=sum(values)
print(total)
percentage=total/500 *100
print(percentage)
#step 3:
mathematics={"Geoffrey Hinton":78,"Andrew Ng":95,"Sebastian Raschka":65,"Yoshua Benjio":50,"Hilary Mason":70,"Corinna Cortes":66,"Peter Warden":75}
values=(78,95,65,50,70,66,75)
max_value=max(values)
print(max_value)
max_marks_scored=max(courses,key=courses.get)
print(max_marks_scored)
topper=max(mathematics,key=mathematics.get)
print(topper)
#step 4:
last_name=(topper.split()[1])
print(last_name)
first_name=(topper.split()[0])
print(first_name)
full_name=last_name+" "+ first_name
print(full_name)
certificate_name=full_name.upper()
print(certificate_name)




