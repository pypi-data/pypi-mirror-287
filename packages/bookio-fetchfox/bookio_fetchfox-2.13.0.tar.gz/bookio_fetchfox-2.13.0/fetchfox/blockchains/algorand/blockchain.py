import base64
import logging
from datetime import datetime
from typing import Iterable, Optional, Tuple

import pytz

from fetchfox.apis.algorand import algonodecloud, nfdomains, randswapcom
from fetchfox.blockchains.base import Blockchain
from fetchfox.constants.blockchains import ALGORAND
from fetchfox.constants.currencies import ALGO
from fetchfox.constants.marketplaces import RANDGALLERY_COM
from fetchfox.dtos import (
    AssetDTO,
    CampaignDTO,
    FloorDTO,
    HoldingDTO,
    ListingDTO,
    SaleDTO,
    TransactionAssetDTO,
    TransactionDTO,
    TransactionInputOutputDTO,
)
from . import utils
from .exceptions import (
    InvalidAlgorandAccountException,
    InvalidAlgorandAssetIdException,
    InvalidAlgorandCollectionIdException,
)

logger = logging.getLogger(__name__)


class Algorand(Blockchain):
    def __init__(self):
        super().__init__(
            name=ALGORAND,
            currency=ALGO,
            logo="https://s2.coinmarketcap.com/static/img/coins/64x64/4030.png",
        )

    # checks
    def check_account(self, account: str):
        if not utils.is_account(account):
            raise InvalidAlgorandAccountException(account)

    def check_asset_id(self, asset_id: str):
        if not utils.is_asset_id(asset_id):
            raise InvalidAlgorandAssetIdException(asset_id)

    def check_collection_id(self, collection_id: str):
        if not utils.is_address(collection_id):
            raise InvalidAlgorandCollectionIdException(collection_id)

    # url builders
    def explorer_url(self, *, address: str = None, collection_id: str = None, asset_id: str = None, tx_hash: str = None) -> str:
        if address:
            return f"https://algoexplorer.io/address/{address.upper()}"

        if asset_id:
            return f"https://algoexplorer.io/asset/{asset_id}"

        if collection_id:
            return f"https://algoexplorer.io/address/{collection_id.upper()}"

        if tx_hash:
            return f"https://algoexplorer.io/tx/{tx_hash.upper()}"

        return None

    def marketplace_url(self, *, collection_id: str = None, asset_id: str = None) -> str:
        if asset_id:
            return f"https://www.randgallery.com/algo-collection/?address={asset_id}"

        if collection_id:
            return f"https://randgallery.com/algo-collection/?address={collection_id}"

        return None

    # accounts
    def get_account(self, wallet: str) -> Optional[str]:
        if not utils.is_account(wallet):
            return None

        resolved = self.resolve_account_name(wallet)

        return resolved or wallet

    def get_account_name(self, account: str) -> str:
        if utils.is_nf_domain(account):
            return account

        if utils.is_address(account):
            return nfdomains.get_nf_domain(account)

        return None

    def resolve_account_name(self, name: str) -> str:
        if utils.is_nf_domain(name):
            return nfdomains.resolve_nf_domain(name)

        return None

    # account attributes
    def get_account_assets(self, account: str, collection_id: str = None) -> Iterable[HoldingDTO]:
        self.check_account(account)

        if utils.is_nf_domain(account):
            account = nfdomains.resolve_nf_domain(account)

        response = algonodecloud.get_account_assets(account)

        for holding in response:
            asset_id = holding["asset-id"]
            quantity = holding["amount"]

            if quantity < 1:
                continue

            yield HoldingDTO(
                collection_id=None,
                asset_id=asset_id,
                address=account,
                quantity=quantity,
            )

    def get_account_balance(self, account: str) -> Tuple[float, str]:
        self.check_account(account)

        if utils.is_nf_domain(account):
            account = nfdomains.resolve_nf_domain(account)

        balance = algonodecloud.get_account_balance(account)

        return balance, self.currency

    def get_account_transactions(self, account: str, last: int = 10) -> Iterable[TransactionDTO]:
        self.check_account(account)

        if utils.is_nf_domain(account):
            account = nfdomains.resolve_nf_domain(account)

        for index, transaction in enumerate(algonodecloud.get_account_transactions(account)):
            if index >= last:
                break

            try:
                message = base64.b64decode(transaction["note"]).decode("utf-8")
            except:
                message = None

            sender = transaction["sender"]

            if transaction["tx-type"] == "pay":
                amount = transaction["payment-transaction"]["amount"]
                receiver = transaction["payment-transaction"]["receiver"]
                unit = "algos"
            elif transaction["tx-type"] == "axfer":
                amount = transaction["asset-transfer-transaction"]["amount"]
                receiver = transaction["asset-transfer-transaction"]["receiver"]
                unit = transaction["asset-transfer-transaction"]["asset-id"]
            else:
                continue

            yield TransactionDTO(
                blockchain=self.name,
                address=account,
                tx_hash=transaction["id"],
                message=message,
                inputs=[
                    TransactionInputOutputDTO(
                        address=sender,
                        assets=[
                            TransactionAssetDTO(
                                amount=amount,
                                unit=unit,
                            ),
                        ],
                    ),
                ],
                outputs=[
                    TransactionInputOutputDTO(
                        address=receiver,
                        assets=[
                            TransactionAssetDTO(
                                amount=amount,
                                unit=unit,
                            ),
                        ],
                    ),
                ],
            )

    # assets
    def get_asset(self, collection_id: str, asset_id: str, fetch_metadata: bool = True, *args, **kwargs) -> AssetDTO:
        if collection_id:
            self.check_collection_id(collection_id)

        self.check_asset_id(asset_id)

        asset_data = algonodecloud.get_asset_data(asset_id)

        if fetch_metadata:
            metadata = algonodecloud.get_asset_metadata(asset_id)
            metadata["name"] = asset_data["name"]
        else:
            metadata = {}

        return AssetDTO(
            collection_id=asset_data["creator"],
            asset_id=asset_id,
            metadata=metadata,
        )

    def get_asset_owners(self, collection_id: str, asset_id: str, *args, **kwargs) -> Iterable[HoldingDTO]:
        self.check_collection_id(collection_id)
        self.check_asset_id(asset_id)

        asset_owner = algonodecloud.get_asset_owner(str(asset_id))

        yield HoldingDTO(
            collection_id=collection_id,
            asset_id=asset_owner["asset_id"],
            address=asset_owner["address"],
            quantity=asset_owner["amount"],
        )

    # collections
    def get_collection_assets(self, collection_id: str, fetch_metadata: bool = True, *args, **kwargs) -> Iterable[AssetDTO]:
        self.check_collection_id(collection_id)

        collection_assets = algonodecloud.get_collection_assets(collection_id)

        for asset_id in collection_assets:
            if fetch_metadata:
                yield self.get_asset(
                    collection_id=collection_id,
                    asset_id=str(asset_id),
                )
            else:
                yield AssetDTO(
                    collection_id=collection_id,
                    asset_id=str(asset_id),
                    metadata={},
                )

    def get_collection_floor(self, collection_id: str, *args, **kwargs) -> FloorDTO:
        self.check_collection_id(collection_id)

        collection_listings = self.get_collection_listings(collection_id)

        floor = None
        count = 0

        for listing in collection_listings:
            count += 1

            if floor is None:
                floor = listing
            elif listing.usd < floor.usd:
                floor = listing

        return FloorDTO(
            listing=floor,
            listing_count=count,
        )

    def get_collection_listings(self, collection_id: str, *args, **kwargs) -> Iterable[ListingDTO]:
        self.check_collection_id(collection_id)

        collection_listings = randswapcom.get_collection_listings(collection_id)

        for listing in collection_listings:
            asset_id = str(listing["assetId"])
            asset_ids = [asset_id]
            asset_names = [""]

            listed_at = datetime.fromtimestamp(
                listing["timestamp"] // 1000,
            ).replace(
                tzinfo=pytz.UTC,
            )

            yield ListingDTO(
                identifier=listing["timestamp"],
                collection_id=collection_id,
                asset_ids=asset_ids,
                asset_names=asset_names,
                listing_id=listing["timestamp"],
                marketplace=RANDGALLERY_COM,
                price=listing["price"],
                currency=ALGO,
                listed_at=listed_at,
                listed_by=listing["sellerAddress"],
                marketplace_url=f"https://randgallery.com/algo-collection/?address={asset_id}",
            )

    def get_collection_sales(self, collection_id: str, *args, **kwargs) -> Iterable[SaleDTO]:
        pass

    def get_collection_snapshot(self, collection_id: str, *args, **kwargs) -> Iterable[HoldingDTO]:
        self.check_collection_id(collection_id)

        for asset in self.get_collection_assets(collection_id, fetch_metadata=False):
            yield from self.get_asset_owners(collection_id, asset.asset_id)

    # campaigns
    def get_campaigns(self, starts_after: datetime = None) -> Iterable[CampaignDTO]:
        return
