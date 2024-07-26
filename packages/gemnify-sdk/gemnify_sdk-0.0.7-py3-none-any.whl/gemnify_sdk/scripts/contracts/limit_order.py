from gemnify_sdk.scripts.instance import ContractInstance
from gemnify_sdk.scripts.contracts.order import Order

class LimitOrder(Order):
    def __init__(self, config) -> None:
        super().__init__(config)
        self.config = config
        self.instance = ContractInstance(config, 'OrderBook')

    def create_increase_order(self, *args, value):
        return self.instance.create_transaction("createIncreaseOrder", args, value)

    def update_increase_order(self, *args):
        return self.instance.create_transaction("updateIncreaseOrder", args)

    def cancel_increase_order(self, *args):
        return self.instance.create_transaction("cancelIncreaseOrder", args)

    def get_increase_order_index(self, *args):
        return self.instance.call_function("increaseOrdersIndex", args)

    def get_increase_order(self, *args):
        result = self.instance.call_function("getIncreaseOrder", args)
        if isinstance(result, list) and len(result) == 9:
            keys = [
                "token",
                "token_amount",
                "collateral_token",
                "index_token",
                "size_delta",
                "is_long",
                "trigger_price",
                "trigger_above_threshold",
                "execution_fee"
            ]
            return dict(zip(keys, result))
        else:
            raise ValueError("Unexpected result format or length")

    def create_decrease_order(self, *args, value):
        return self.instance.create_transaction("createDecreaseOrder", args, value)

    def update_decrease_order(self, *args):
        return self.instance.create_transaction("updateDecreaseOrder", args)

    def cancel_decrease_order(self, *args):
        return self.instance.create_transaction("cancelDecreaseOrder", args)

    def get_decrease_order_index(self, *args):
        return self.instance.call_function("decreaseOrdersIndex", args)

    def get_decrease_order(self, *args):
        result = self.instance.call_function("getDecreaseOrder", args)
        if isinstance(result, list) and len(result) == 8:
            keys = [
                "collateral_token",
                "collateral_delta",
                "index_token",
                "size_delta",
                "is_long",
                "trigger_price",
                "trigger_above_threshold",
                "execution_fee"
            ]
            return dict(zip(keys, result))
        else:
            raise ValueError("Unexpected result format or length")

    def cancel_multiple(self, *args):
        return self.instance.create_transaction("cancelMultiple", args)

    def get_min_execution_fee(self):
        return self.instance.call_function("minExecutionFee")