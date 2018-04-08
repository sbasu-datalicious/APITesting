from woocommerce import API

class Request():
    def __init__(self):
        admin_consumer_key = "ck_b8cca2d3ba8e0d7b08c830254b59e1f005df5bd4"
        admin_consumer_secret = "cs_b48bd72801b20cf8df76bee3864d21368f0ef444"

        self.wcapi = API(
            url = "http://127.0.0.1/testapi",
            consumer_key = admin_consumer_key,
            consumer_secret = admin_consumer_secret,
            version="v3"
        )

    def test_api(self):
        """

        :return:
        """
        print self.wcapi.get("").json()

    def post_request(self, endpoint, data):
        """

        :param endpoint:
        :param data:
        :return:
        """
        result = self.wcapi.post(endpoint, data)
        rs_code = result.status_code
        rs_body = result.json()
        rs_url = result.url

        return [rs_code, rs_body, rs_url]

    def get_request(self, endpoint):
        """

        :param endpoint:
        :return:
        """
        result = self.wcapi.get(endpoint)
        rs_code = result.status_code
        rs_body = result.json ( )
        rs_url = result.url

        return [rs_code, rs_body, rs_url]