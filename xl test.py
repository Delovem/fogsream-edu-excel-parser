import openpyxl
wb = openpyxl.load_workbook('avtovoz_cars.xlsx')

sheet = wb['Лист1']

inp_brand = input('Введите марку авто: ').lower()

row_count = sheet.max_row

def carfinder(inp_brand):
    for row in range(1, row_count):
        brand = sheet[row][0].value
        model = sheet[row][1].value

        if brand.lower() == inp_brand or inp_brand in brand.lower():
            print(brand, model)


carfinder(inp_brand)

