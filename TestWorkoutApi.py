import unittest
from WorkoutApi import ServerApi


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ENDPOINT:/np/workouts-partner/v1.0/exercisers/{exerciserUuid}/workouts
    # valid access token, exceciserUuid, limit, page
    def test_1_1_check_the_endpoint_with_valid_access_token_exerciseruuid_limit_page(self):
       api = ServerApi()
       self.assertEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    1).status_code)

    # invalid access token
    def test_1_2_check_the_endpoint_with_invalid_access_token(self):
       api = ServerApi()
       self.assertEqual(401, api.workoutByExceciserUuid('vrgabdejkls1g6hj8kkjhyedgs3dvlll',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    1).status_code)

     # missing access token
    def test_1_3_check_the_endpoint_with_missing_access_token(self):
       api = ServerApi()
       self.assertEqual(403, api.workoutByExceciserUuid('',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    1).status_code)

    # invalid exceciserUuid
    def test_1_4_check_the_endpoint_with_invalid_exerciseruuid(self):
       api = ServerApi()
       self.assertEqual(404, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'ddddd32d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    1).status_code)
    # missing exceciserUuid
    def test_1_5_check_the_endpoint_with_missing_exerciseruuid(self):
       api = ServerApi()
       self.assertEqual(404, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    '',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    1).status_code)


    # invalid page - negative
    def test_1_6_check_the_endpoint_with_invalid_page_negative(self):
       api = ServerApi()
       self.assertEqual(400, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    -1).status_code)

    # invalid page - zero
    def test_1_7_check_the_endpoint_with_invalid_page_zero(self):
       api = ServerApi()
       self.assertEqual(400, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    0).status_code)



    # invalid page - float values
    def test_1_8_check_the_endpoint_with_invalid_page_float_values(self):
       api = ServerApi()
       self.assertEqual(400, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    '1.5').status_code)



    # invalid page - non numeric values
    def test_1_9_check_the_endpoint_with_invalid_page_non_numeric_values(self):
       api = ServerApi()
       self.assertEqual(400, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1000,\
                                                    'g').status_code)



    # invalid limit - negative
    def test_1_10_check_the_endpoint_with_invalid_limit_negative(self):
       api = ServerApi()
       self.assertEqual(400, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    -1,\
                                                    1).status_code)

    # invalid limit - > 1000
    def test_1_11_check_the_endpoint_with_invalid_limit_more_1000(self):
       api = ServerApi()
       self.assertEqual(400, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1001,\
                                                    1).status_code)


    # invalid limit - zero
    def test_1_12_check_the_endpoint_with_invalid_limit_zero(self):
       api = ServerApi()
       self.assertEqual(400, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    0,\
                                                    1).status_code)

    # invalid limit - float
    def test_1_13_check_the_endpoint_with_invalid_limit_float(self):
       api = ServerApi()
       self.assertEqual(400, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    1.1,\
                                                    1).status_code)


    # invalid limit - non numeric values
    def test_1_14_check_the_endpoint_with_invalid_limit_non_numeric_value(self):
       api = ServerApi()
       self.assertEqual(400, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '',\
                                                    'e',\
                                                    1).status_code)


    # valid date
    def test_1_15_check_the_endpoint_with_valid_modifiedat(self):
       api = ServerApi()
       self.assertEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '%5B2018-01-01T00%3A00%3A00Z%2C%202018-12-31T23%3A59%3A59Z%5D',\
                                                    1000,\
                                                    1).status_code)



    # invalid date - no brackets
    def test_1_16_check_the_endpoint_with_invalid_modifiedat_missing_brackets(self):
       api = ServerApi()
       self.assertEqual(400, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '2018-01-01T00%3A00%3A00Z%2C%202018-12-31T23%3A59%3A59Z',\
                                                    1000,\
                                                    1).status_code)


    # invalid date - single date, not a period
    def test_1_17_check_the_endpoint_with_invalid_modifiedat_single_date(self):
       api = ServerApi()
       self.assertEqual(400, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    '%5B2018-01-01T00%3A00%3A00Z',\
                                                    1000,\
                                                    1).status_code)


    # invalid date - non numerics values
    def test_1_18_check_the_endpoint_with_invalid_modifiedat_non_numeric_values(self):
       api = ServerApi()
       self.assertEqual(400, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    '',\
                                                    'z@]',\
                                                    1000,\
                                                    1).status_code)

    # valid categoryId
    def test_1_19_check_the_endpoint_with_valid_categoryid(self):
       api = ServerApi()
       self.assertEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    12,\
                                                    '',\
                                                    1000,\
                                                    1).status_code)

    # invalid categoryId - negative
    def test_1_20_check_the_endpoint_with_invalid_categoryid_negative(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    -1,\
                                                    '',\
                                                    1000,\
                                                    1).status_code)

    # invalid categoryId - zero
    def test_1_21_check_the_endpoint_with_invalid_categoryid_zero(self):
       api = ServerApi()
       self.assertNotEqual(200, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    0,\
                                                    '',\
                                                    1000,\
                                                    1).status_code)


    # invalid categoryId - float
    def test_1_22_check_the_endpoint_with_invalid_categoryid_float(self):
       api = ServerApi()
       self.assertEqual(400, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    1.1,\
                                                    '',\
                                                    1000,\
                                                    1).status_code)


    # invalid categoryId - non numeric values
    def test_1_23_check_the_endpoint_with_invalid_categoryid_non_numeric_values(self):
       api = ServerApi()
       self.assertEqual(400, api.workoutByExceciserUuid('abdejkls12ap4dfololjnbdgs3dvfaa',\
                                                    'd471432d-0821-47f2-b2b5-8636ffb280d0',\
                                                    'd',\
                                                    '',\
                                                    1000,\
                                                    1).status_code)


    # ENDPOINT:/np/workouts-partner/v1.0/workouts/{workoutId}
    # valid access token and workoutId
    def test_2_1_check_the_endpoint_with_valid_access_token_workoutid(self):
       api = ServerApi()
       self.assertEqual(200, api.workoutByWorkoutId('abdejkls12ap4dfololjnbdgs3dvfaa', 219453846).status_code)

    # invalid access token
    def test_2_2_check_the_endpoint_with_invalid_access_token(self):
         api = ServerApi()
         self.assertEqual(401, api.workoutByWorkoutId('ghetaejkls12ap4dfo3erry425dmmtunv', 219453846).status_code)

    # missing access token
    def test_2_3_check_the_endpoint_with_missing_access_token(self):
         api = ServerApi()
         self.assertEqual(403, api.workoutByWorkoutId('', 219453846).status_code)

    # missing workoutId
    def test_2_4_check_the_endpoint_with_missing_workoutid(self):
         api = ServerApi()
         self.assertEqual(404, api.workoutByWorkoutId('abdejkls12ap4dfololjnbdgs3dvfaa', '').status_code)

    # invalid workoutId
    def test_2_5_check_the_endpoint_with_invalid_workoutid(self):
         api = ServerApi()
         self.assertEqual(404, api.workoutByWorkoutId('abdejkls12ap4dfololjnbdgs3dvfaa', 1).status_code)

    # invalid workouyId - negative
    def test_2_6_check_the_endpoint_with_invalid_workoutid_negative(self):
         api = ServerApi()
         self.assertEqual(404, api.workoutByWorkoutId('abdejkls12ap4dfololjnbdgs3dvfaa', -1).status_code)

    # invalid workouyId - zero
    def test_2_7_check_the_endpoint_with_invalid_workoutid_zero(self):
         api = ServerApi()
         self.assertEqual(404, api.workoutByWorkoutId('abdejkls12ap4dfololjnbdgs3dvfaa', 0).status_code)


    # invalid workouyId - float
    def test_2_8_check_the_endpoint_with_invalid_workoutid_float(self):
         api = ServerApi()
         self.assertEqual(400, api.workoutByWorkoutId('abdejkls12ap4dfololjnbdgs3dvfaa', 1.1).status_code)


    # invalid workouyId - non numeric values
    def test_2_9_check_the_endpoint_with_invalid_workoutid_non_numeric_values(self):
         api = ServerApi()
         self.assertEqual(400, api.workoutByWorkoutId('abdejkls12ap4dfololjnbdgs3dvfaa', 'fge').status_code)

    # invalid workouyId - service symbols
    def test_2_10_check_the_endpoint_with_invalid_workoutid_service_symbols(self):
         api = ServerApi()
         self.assertEqual(404, api.workoutByWorkoutId('abdejkls12ap4dfololjnbdgs3dvfaa', '#$@').status_code)


if __name__ == '__main__':
    unittest.main()