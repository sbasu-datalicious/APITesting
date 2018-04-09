from Tools import Request
from Tools import DBConnect

req = Request.Request()
qry = DBConnect.DBConnect()

# Validae API with empty PayLoad
def test_negative_TestCase1_emptyPayLoad():
    """

    :return:
    """
    input_data = {}
    info = req.post_request('products', input_data)

    tc = 'Test Case-1: Empty payload'
    expected_error_message = 'No product data specified to create product'
    expected_code = 'woocommerce_api_missing_product_data'

    verify_negative_test_response(info, tc, expected_error_message, expected_code)

    print "Test Case-1: Empty payload, PASS"

# Validate API with missing key title
def test_negative_TestCase2_missingTitleKey():
    """

    :return:
    """
    input_data = {}
    product = {}
    product["regular_price"] = '19.99'
    product["type"] = 'simple'

    input_data['product'] = product
    info = req.post_request('products', input_data)

    tc = 'Test Case-2: missing title key in payload'
    expected_error_message = 'Missing parameter title'
    expected_code = 'woocommerce_api_missing_product_title'

    verify_negative_test_response (info, tc, expected_error_message, expected_code)

    print "Test Case-2: empty product title, PASS"


# Code to validate API for empty string in payload
def test_negative_TestCase3_emptyStringForTitleInPayLoad():
    """

    :return:
    """
    input_data = {}
    product = {}
    product["regular_price"] = '19.99'
    product["type"] = 'simple'
    product['title'] = ''

    input_data['product'] = product
    info = req.post_request ('products', input_data)

    print info

    tc = 'Test Case-3: Empty string for title in payload'
    expected_message = "Content, title, and excerpt are empty."
    expected_error_code = "woocommerce_api_cannot_create_product"

    verify_negative_test_response(info, tc, expected_message, expected_error_code)

    print "Test Case-2: empty string for title, PASS"


# Assertion code
def verify_negative_test_response(response_list, test_case, exp_err_msg, exp_err_code):
    """

    :return:
    """
    # Verify response code
    response_code = response_list[0]
    assert response_code == 400, "Response code is not correct for Test Case:-{tc}, " \
                                 "Expected 400. Actual:{act}".format (tc=test_case, act=response_code)

    # Verify there is key 'errors' in the response
    response_body = response_list[1]
    assert "errors" in response_body.keys ( ), "Test Case-1: empty payload, the keyword errors " \
                                               "is not present in the response body"

    # Verify the content of the error message
    act_error_msg = response_body['errors'][0]['message']
    assert act_error_msg == exp_err_msg, "Test Case {tc} failed. The error message is not as expected. " \
                                         "Expected message: {exp}, Actual msg: {act}".format(tc=test_case,
                                                                                             exp=exp_err_msg,
                                                                                             act=act_error_msg)

    # Verify the error code in the respopnse
    act_error_code = response_body['errors'][0]['code']
    assert act_error_code == exp_err_code, "Test Case {tc} failed. The error code is not as expected. " \
                                         "Expected code: {exp}, Actual code: {act}".format (tc=test_case,
                                                                                              exp=exp_err_code,
                                                                                              act=act_error_code)

test_negative_TestCase1_emptyPayLoad()
test_negative_TestCase2_missingTitleKey()
test_negative_TestCase3_emptyStringForTitleInPayLoad()