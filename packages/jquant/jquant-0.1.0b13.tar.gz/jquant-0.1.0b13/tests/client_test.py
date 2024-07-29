import logging

import jquant


class TestExchange:
    pc = jquant.PlatformClient(
        "s1",
        "localhost:8081",
        # "192.168.1.200:18081",
        metadata=[
            ("initial-metadata-1", "The value should be str"),
            ("authorization", "gRPC Python is great"),
        ],
    )

    def test_get_ticker(self):
        reply = self.pc.get_ticker(platform="ctp.future", instrument="au2408")
        print(f"recv from server, result={reply}")

    def test_get_tickers(self):
        reply = self.pc.get_tickers(
            platforms=["ctp.future"], instruments=["c2409", "au2408"]
        )
        print(f"recv from server, result={reply}")

    def test_get_kline(self):
        reply = self.pc.get_kline(
            platform="ctp.future", instrument="au2408", period="1m"
        )
        print(f"recv from server, result={reply}")

    def test_get_position(self):
        reply = self.pc.get_position(platform="ctp.future")
        print(f"recv from server, result={reply}")

    def test_get_order(self):
        reply = self.pc.get_order(
            platform="ctp.future",
            instrument="c2409",
            client_order_id="193108902017",
        )
        print(f"recv from server, result={reply}")

    def test_get_orders(self):
        orders = self.pc.get_orders(
            platform="ctp.future",
            instruments=["au2408"],
            investor="PROD001",
            strategy="S01",
        )
        # print(f"recv from server, result={orders}")
        for order in orders:
            print(f"order={order}")

    def test_buy(self):
        reply = self.pc.buy(
            platform="ctp.future",
            instrument="c2409",
            price="2348",
            amount="1",
            investor="PROD001",
            strategy="S01",
            source="01",
            tag="01",
            # VolumeCondition="3",
        )
        print(f"recv from server, result={reply}")

    def test_closebuy(self):
        reply = self.pc.close_buy(
            platform="ctp.future",
            instrument="au2408",
            price="553",
            amount="3",
            investor="PROD001",
            strategy="S01",
        )
        print(f"recv from server, result={reply}")

    def test_cancel(self):
        reply = self.pc.cancel(
            platform="ctp.future",
            instrument="c2409",
            client_order_ids=["89917489281"],
        )
        print(f"recv from server, result={reply}")

    def test_get_position(self):
        reply = self.pc.get_position(
            platform="ctp.future",
        )
        print(f"recv from server, result={reply}")

    def test_get_instrument(self):
        reply = self.pc.get_instruments(
            platform="ctp.future",
            kinds=[jquant.InstrumentKind.FUTURE],
            instruments=["ag2408"],
        )
        print(f"recv from server, result={reply}")

    def test_subscribe_order(self):
        self.pc.subscribe_order(
            platform="ctp.future",
            instruments=["c2409"],
            investor="PROD001",
            strategy="S01",
            handler=self.on_order,
        )
        # print(f"recv from server, result={reply}")

    def on_order(self, orders):
        # print(f"recv from server, order={orders}")
        for order in orders:
            print(f"order={order}")

    def test_subscribe_ticker(self):
        self.pc.subscribe_tick(
            platforms=["ctp.future"],
            instruments=["c2409"],
            handler=self.on_tick,
        )
        # print(f"recv from server, result={reply}")

    def on_tick(self, ticker):
        print(f"recv from server, ticker={ticker}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    t = TestExchange()

    # t.test_get_ticker()
    # t.test_get_order()
    # t.test_get_orders()
    # t.test_buy()
    # t.test_closebuy()
    # t.test_cancel()
    # t.test_get_instrument()
    t.test_subscribe_ticker()
    # t.test_subscribe_order()
    # t.test_get_position()
