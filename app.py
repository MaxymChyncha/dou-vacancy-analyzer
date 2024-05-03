from data_parsing.items import VACANCY_FIELDS
from data_parsing.parse import DOUWebParser
from data_parsing.writer import CSVFileWriter


def main():
    parser = DOUWebParser()
    data = parser.get_all_vacancies()
    writer = CSVFileWriter(file_name="data", column_fields=VACANCY_FIELDS)
    writer.write_in_csv_file(data)


if __name__ == "__main__":
    main()
