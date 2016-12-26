# This program is a learning exercise for dictionaries in perl
# Parse through a dict and print
months = {
	1: 'January',
	2: 'February',
	3: 'March',
	4: 'April',
	5: 'May',
	6: 'June',
	7: 'July',
	8: 'August',
	9: 'September',
	10: 'October',
	11: 'November',
	12: 'December'
}
# print "Enter month>" 
# month=raw_input()
# month=int(month)
#  Simple command to get an item in a dictionary
# print "The month is %s" % months.get(month)
# Print all elements one by one
for a,b in months.items():
	# print a,'is the month of',b
	print "%d is the month of %s" % (a,b)