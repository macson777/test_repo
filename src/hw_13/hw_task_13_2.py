class Book:
    def __init__(self, number_of_pages, year, autor, price):
        if number_of_pages < 0:
            raise Exception
        self.number_of_pages = number_of_pages
        self.year = year
        self.autor = autor
        self.price = price


def main():
    try:
        my_object = Book(-5, 1500, 'Iosif', 2000)
    except Exception:
        print('something is wrong')
if __name__ == '__main__':
    main()