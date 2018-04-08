from Tools import Request
from Tools import DBConnect
import json

req = Request.Request()
qry = DBConnect.DBConnect()

def test_create_product():
    """

    :return:
    """
    global product_id
    global title
    global price

    title = 'Test_API_1'
    price = '9.99'
    input_data = {
        'product':{
            'title': title,
            'type': 'simple',
            'regular_price': price
        }
    }

    info = req.post_request('products', input_data)
    response_code = info[0]
    response_body = info[1]
    # print json.dumps(info[1], indent=4)

    assert response_code == 201, "The status code is not as expected. " \
                                   "Expected status code is: {act_code}".format(act_code=response_code)

    response_title = response_body["product"]["title"]
    response_price = response_body["product"]["regular_price"]
    product_id = response_body["product"]["id"]

    assert response_title == title, "Actual and expected titles are different. " \
                                    "The expected response title is: {}".format(response_title)

    assert response_price == price, "Actual and expected prices are different. " \
                                    "The expected response price is : {}".format(response_price)

    # print 'id is : {}'.format(product_id)

    print "Create_product test PASSED"


def test_verify_product_db():
    """

    :return:
    """
    sql_query = '''select p.post_title,p.post_type,pm.meta_value FROM wpnrv7_posts p JOIN wpnrv7_postmeta pm ON p.id=pm.post_id 
    WHERE p.id={} AND pm.meta_key='_regular_price';
    '''.format(product_id)

    query_response = qry.select_query('wp133', sql_query)

    db_title = query_response[0][0]
    db_type = query_response[0][1]
    db_regular_price = query_response[0][2]

    assert db_title == title, "Expected title and actual title do not match. " \
                              "Actual title is: {}".format(db_title)

    assert db_type == 'product', "Expected db_type and actual db_type do not match. " \
                              "Actual db_type is: {}".format(db_type)

    assert db_regular_price == price, "Expected price and Actual price do not match. " \
                                      "Actual price is: {}".format(db_regular_price)

    print "API response and DB response match. PASSED"


test_create_product()
test_verify_product_db()

