from typing import Any, Dict, List, Optional, cast

from aea.common import JSONLike
from aea.configurations.base import PublicId
from aea.contracts.base import Contract
from aea_ledger_ethereum import LedgerApi

PUBLIC_ID = PublicId.from_str("valory/demo:0.1.0")


class Demo(Contract):
    contract_id = PUBLIC_ID

    @classmethod
    def get_number(
        cls, ledger_api: LedgerApi, contract_address: str
    ) -> Dict[str, Any]:
        contract_instance = cls.get_instance(ledger_api, contract_address)
        data = contract_instance.functions.getNumber().call()
        print("contract -data",data)
        return dict(data=data)

    # @classmethod
    # def get_buy_property_tx(
    #     cls, ledger_api: LedgerApi, contract_address: str, id: int
    # ) -> Dict[str, Any]:
    #     contract_instance = cls.get_instance(ledger_api, contract_address)
    #     tx_data = contract_instance.encodeABI(
    #         fn_name="buyProperty",
    #         args=[id],
    #     )

    #     return dict(
    #         data=tx_data,
    #     )
