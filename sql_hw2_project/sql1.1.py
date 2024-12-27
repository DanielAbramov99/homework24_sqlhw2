# 1
# -- select Courses.*, Lecturers.name from Courses
# -- inner join Lecturers on Courses.lecturer_id = Lecturers.lecturer_id
# 2
# -- select Courses.*, Lecturers.name from Courses
# -- left join Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id
# 3
# -- select Lecturers.*, Courses.name, Courses.course_id from Lecturers
# -- left join Courses ON Lecturers.lecturer_id = Courses.lecturer_id
# 4
# -- select Courses.*, Lecturers.name from Courses
# -- left join Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id
# -- where Courses.lecturer_id is NULL
# 5
# -- select Lecturers.*, Courses.name, Courses.course_id from Lecturers
# -- left join Courses ON Lecturers.lecturer_id = Courses.lecturer_id
# -- where Lecturers.lecturer_id is NULL
# 6
# -- select Courses.*,  Lecturers.name from Courses
# -- full join Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id
# 7
# -- select Courses.*,  Lecturers.name from Courses
# -- full join Lecturers ON Courses.lecturer_id = Lecturers.lecturer_id
# -- where Courses.lecturer_id is NULL or Lecturers.lecturer_id is NULL
# 8
# -- select Lecturers.* from Lecturers
# -- where Lecturers.name like "%i%"
# 9
# -- select count(*) as lecturers_amount from Lecturers
# 10
# -- select count(*) as courses_amount from Courses
# 11
# -- alter table Courses
# -- add weekly_hours integer
# -- update Courses set weekly_hours = 4 where Courses.name = "Mathematics";
# -- update Courses set weekly_hours = 6 where Courses.name = "Physics";
# -- update Courses set weekly_hours = 4 where Courses.name = "Chemistry";
# -- update Courses set weekly_hours = 8 where Courses.name = "Economics";
# -- update Courses set weekly_hours = 4 where Courses.name = "Biology";
# -- update Courses set weekly_hours = 4 where Courses.name = "Sociology";
# -- update Courses set weekly_hours = 6 where Courses.name = "Art History";
# -- update Courses set weekly_hours = 6 where Courses.name = "Music Theory";
# -- update Courses set weekly_hours = 6 where Courses.name = "Philosophy";
# -- update Courses set weekly_hours = 4 where Courses.name = "Environmental Studies";
# -- update Courses set weekly_hours = 4 where Courses.name = "Computer Science";
# -- update Courses set weekly_hours = 4 where Courses.name = "Statistics";
# -- update Courses set weekly_hours = 4 where Courses.name = "Psychology";
# 12
# -- select count(*) as hours_count, weekly_hours from courses
# -- group by weekly_hours
# 13
# -- select Lecturers.*, Courses.name, Courses.weekly_hours from Lecturers
# -- inner join Courses on Lecturers.lecturer_id = Courses.lecturer_id
# -- where weekly_hours == 8
# 14
# -- delete from Courses where weekly_hours == 4 and Courses.lecturer_id is NULL
