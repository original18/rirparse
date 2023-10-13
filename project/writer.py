import os
import xlsxwriter
from parse import array
from values import cell_size, col, desc, file_name, iter_desc


def writer(parametr):
    book = xlsxwriter.Workbook(os.path.abspath(file_name))
    page = book.add_worksheet("Удочки")

    if os.path.exists(file_name):
        os.remove(file_name)

    row = 0
    column = 0

    for i in col:
        page.set_column(i, cell_size)

    for i in iter_desc:
        page.write(row, column+i, desc[i])

    row += 1

    for item in parametr:
        for key in item:
            for i in iter_desc:
                if desc[i] == key:
                    page.write(row, column+i, item[desc[i]])
                    continue
                else:
                    continue

            # Суть происходящего выше здесь
            # if key == "Название":
            #     page.write(row, column, item["Название"])
            #     continue
            # elif key == "Фото":
            #     page.write(row, column+1, item["Фото"])
            #     continue
            # elif key == "Тип":
            #     page.write(row, column+2, item["Тип"])
            #     continue
            # elif key == "Бренд":
            #     page.write(row, column+3, item["Бренд"])
            #     continue
            # elif key == "Модель":
            #     page.write(row, column+4, item["Модель"])
            #     continue
            # elif key == "Транспортная длина":
            #     page.write(row, column+5, item["Транспортная длина"])
            #     continue
            # elif key == "Кол-во секций":
            #     page.write(row, column+6, item["Кол-во секций"])
            #     continue
            # elif key == "Вес":
            #     page.write(row, column+7, item["Вес"])
            #     continue
            # elif key == "Длина":
            #     page.write(row, column+8, item["Длина"])
            #     continue
            # elif key == "Тест от":
            #     page.write(row, column+9, item["Тест от"])
            #     continue
            # elif key == "Тест до":
            #     page.write(row, column+10, item["Тест до"])
            #     continue
            # else:
            #     continue

        row += 1
    book.close()


writer(array())
