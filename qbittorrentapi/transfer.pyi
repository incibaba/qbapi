from typing import Iterable, Text

from qbittorrentapi.definitions import ClientCache
from qbittorrentapi.definitions import Dictionary
from qbittorrentapi.request import Request

class TransferInfoDictionary(Dictionary): ...

class Transfer(ClientCache):
    @property
    def info(self) -> TransferInfoDictionary: ...
    @property
    def speed_limits_mode(self) -> Text: ...
    speedLimitsMode = speed_limits_mode
    @speedLimitsMode.setter
    def speedLimitsMode(self, v: Text | int) -> None: ...
    @speed_limits_mode.setter
    def speed_limits_mode(self, v: Text | int) -> None: ...
    def toggle_speed_limits_mode(
        self, intended_state: bool = None, **kwargs
    ) -> None: ...
    toggleSpeedLimitsMode = toggle_speed_limits_mode
    @property
    def download_limit(self): ...
    downloadLimit = download_limit
    @downloadLimit.setter
    def downloadLimit(self, v: Text | int) -> None: ...
    @download_limit.setter
    def download_limit(self, v: Text | int) -> None: ...
    @property
    def upload_limit(self) -> int: ...
    uploadLimit = upload_limit
    @uploadLimit.setter
    def uploadLimit(self, v: Text | int) -> None: ...
    @upload_limit.setter
    def upload_limit(self, v: Text | int) -> None: ...
    def set_download_limit(self, limit: Text | int = None, **kwargs) -> None: ...
    setDownloadLimit = set_download_limit
    def set_upload_limit(self, limit: Text | int = None, **kwargs) -> None: ...
    setUploadLimit = set_upload_limit
    def ban_peers(self, peers: Text | Iterable[Text] = None, **kwargs) -> None: ...
    banPeers = ban_peers

class TransferAPIMixIn(Request):
    @property
    def transfer(self) -> Transfer: ...
    def transfer_info(self, **kwargs) -> TransferInfoDictionary: ...
    def transfer_speed_limits_mode(self, **kwargs) -> Text: ...
    transfer_speedLimitsMode = transfer_speed_limits_mode
    def transfer_toggle_speed_limits_mode(
        self, intended_state: bool = None, **kwargs
    ) -> None: ...
    transfer_toggleSpeedLimitsMode = transfer_toggle_speed_limits_mode
    def transfer_download_limit(self, **kwargs) -> int: ...
    transfer_downloadLimit = transfer_download_limit
    def transfer_upload_limit(self, **kwargs) -> int: ...
    transfer_uploadLimit = transfer_upload_limit
    def transfer_set_download_limit(
        self, limit: Text | int = None, **kwargs
    ) -> None: ...
    transfer_setDownloadLimit = transfer_set_download_limit
    def transfer_set_upload_limit(self, limit: Text | int = None, **kwargs) -> None: ...
    transfer_setUploadLimit = transfer_set_upload_limit
    def transfer_ban_peers(
        self, peers: Text | Iterable[Text] = None, **kwargs
    ) -> None: ...
    transfer_banPeers = transfer_ban_peers
