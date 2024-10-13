def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    return tuple(azara_record[1]) == rui_record[1]


def create_record(azara_record, rui_record):
    return azara_record + rui_record if compare_records(azara_record, rui_record) else 'not a match'


def clean_up(combined_record_group):
    return '\n'.join(str((item[0], item[2], item[3], item[4])) for item in combined_record_group) + '\n'
