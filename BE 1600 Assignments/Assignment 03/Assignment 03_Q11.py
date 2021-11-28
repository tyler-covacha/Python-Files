course_room_number = {'CS101':'3004','CS102':'4501','CS103':'6755','NT110':'1244','CM241':'1411'}
course_instructor = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
course_time = {'CS101':'8:00 am','CS102':'9:00 am','CS103':'10:00 am','NT110':'11:00 am','CM241':'1:00 pm'}

user_course_number = input('Enter a course number: ')
if user_course_number not in course_room_number:
    print(user_course_number,'is an invalid course number')
else:
    print('The details for course',user_course_number,'are:')
    print('Room:',course_room_number[user_course_number])
    print('Instructor:',course_instructor[user_course_number])
    print('Time:',course_time[user_course_number])
