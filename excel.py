import xlsxwriter

data = [
	{
		'name': "Edan Stein",
		'phone': "1-411-426-8735",
		'email': "facilisis.magna@aol.couk",
		'address': "594-6075 Elementum Ave",
		'country': "Belgium"
	},
	{
		'name': "Gretchen Whitfield",
		'phone': "(323) 253-9734",
		'email': "ipsum@protonmail.net",
		'address': "Ap #783-9102 Augue. Rd.",
		'country': "Netherlands"
	},
	{
		'name': "Violet Brooks",
		'phone': "1-389-367-4883",
		'email': "montes.nascetur.ridiculus@outlook.edu",
		'address': "Ap #814-4695 Odio. Street",
		'country': "India"
	},
	{
		'name': "Ethan Espinoza",
		'phone': "(428) 503-8130",
		'email': "vestibulum.lorem@yahoo.couk",
		'address': "3416 Suspendisse Rd.",
		'country': "Russian Federation"
	},
	{
		'name': "Martin Dunlap",
		'phone': "1-341-689-0165",
		'email': "natoque.penatibus@aol.couk",
		'address': "Ap #593-870 Rhoncus. Ave",
		'country': "Poland"
	}
]

workbook = xlsxwriter.Workbook("AllAboutPythonExcel.xlsx")
worksheet = workbook.add_worksheet("firstSheet")

worksheet.write(0, 0, "#")
worksheet.write(0, 1, "Name")
worksheet.write(0, 2, "Phone")
worksheet.write(0, 3, "Email")
worksheet.write(0, 4, "Address")
worksheet.write(0, 5, "Country")

for index, entry in enumerate(data):
    worksheet.write(index+1, 0, str(index))
    worksheet.write(index+1, 1, entry["name"])
    worksheet.write(index+1, 2, entry["phone"])
    worksheet.write(index+1, 3, entry["email"])
    worksheet.write(index+1, 4, entry["address"])
    worksheet.write(index+1, 5, entry["country"])

workbook.close()