import time
import database
# from data_sources.eth import EthereumMetricProvider


class PollingManager:
    def __init__(self):
        db = database.SQLLiteDatabase()
        # etherium_metrics = EthereumMetricProvider()

        # TODO enable the polling loop
        # while True:
        #     # Main loop for polling APIs
        #
        #
        #     etherium_metrics = EthereumMetricProvider()
        #     # etherium_metrics.
        #     # TODO start with long delay for testing
        #     time.sleep(60)


polling_manager = PollingManager()

