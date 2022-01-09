import xlsxwriter

def generate_excel(workbook_name: str, worksheet_name: str, headers_list: list, data: list):

    # Creating workbook
    workbook = xlsxwriter.Workbook(workbook_name)
    
    # Creating worksheet
    worksheet = workbook.add_worksheet(worksheet_name)

    # Adding headers
    for index, header in enumerate(headers_list):
        worksheet.write(0, index, str(header).capitalize())

    # Adding data
    for index1, entry in enumerate(data):
        for index2, header in enumerate(headers_list):
            worksheet.write(index1+1, index2, entry[header])

    # Close workbook
    workbook.close()

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

generate_excel("TestWorkbook.xlsx", "FirstSheet", ["name", "phone", "email", "address", "country"], data)