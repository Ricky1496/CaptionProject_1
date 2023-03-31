from utilities import read_utils

test_invalid_login_data = read_utils.get_csv_as_list("../test_data/test_invalid_data.csv")

test_valid_user = read_utils.get_sheet_as_list("../test_data/agoda_test_data.xlsx",
                                               "test_valid_user")

test_invalid_user = read_utils.get_sheet_as_list("../test_data/agoda_test_data.xlsx",
                                                 "test_invalid_user")