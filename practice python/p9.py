'''
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
'''
exam_st_date = (11, 12, 2014)

#we cannot change any things in tuple. so we cannot use replace function
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

print( "The examination will start from : %i / %i / %i"%exam_st_date)


# exam_st_date_list = list(exam_st_date)#convert in list