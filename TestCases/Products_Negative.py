from Tools import Request
from Tools import DBConnect

req = Request.Request()
qry = DBConnect.DBConnect()

def test_negative_TestCase1_emptyPayLoad():
    """

    :return:
    """
    print "Testing products endpoint with payload being empty JSON"

    input_data = {}
    info = req.post_request('products', input_data)

    response_code = info[0]
    assert response_code == 400, "Test Case-1: Empty payload, " \
                                 "Expected 400. Actual:{act}".format(act=response_code)

    response_body = info[1]
    assert "errors" in response_body.keys(), "Test Case-1: empty payload, the keyword errors " \
                                                              "is not present in the response body"

    exp_error_msg = "No product data specified to create product"
    act_error_msg = response_body['errors'][0]['message']
    assert exp_error_msg == act_error_msg, "Test Case-1: Empty payload. " \
                                           "The error message does not match"

    exp_error_code = "woocommerce_api_missing_product_data"
    act_error_code = response_body['errors'][0]['code']
    assert exp_error_code == act_error_code, "Test Case-1: Empty payload. " \
                                             "The error code does not match"

    print "Test Case-1: Empty payload, PASS"

test_negative_TestCase1_emptyPayLoad()