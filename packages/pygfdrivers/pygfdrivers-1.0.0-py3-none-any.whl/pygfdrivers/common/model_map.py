from common.models.infrastructure.client import BaseClientModel
from common.models.infrastructure.server import BaseServerModel
from common.models.infrastructure.repo import BaseRepoModel
from common.models.tests.client import TestClientConfig

from keysight.models.scope_config import KeysightScopeConfigModel
from keysight.models.scope_data import KeysightScopeDataModel

from dtacq.models.scope_config import DtacqScopeConfigModel
from dtacq.models.scope_data import DtacqScopeDataModel

from lecroy.models.scope_config import LecroyScopeConfigModel
from lecroy.models.scope_data import LecroyScopeDataModel

from princeton_instruments.models.princeton_camera_config import PrincetonCameraConfigModel

from gf.models.digitizer_config import GFDigitizerConfigModel
from gf.models.digitizer_data import GFDigitizerDataModel
model_map = {
    'clients' : {
        'base'      : BaseClientModel,
        'test'      : TestClientConfig,
    },

    'servers' : {
        'base' : BaseServerModel,
    },

    'repos' : {
        'base' : BaseRepoModel
    },

    'scopes' : {
        'keysight_visa'     : KeysightScopeConfigModel,
        'dtacq'             : DtacqScopeConfigModel,
        'lecroy_visa'       : LecroyScopeConfigModel,
        'gf_digitizer'      : GFDigitizerConfigModel,
    },

    'cameras' : {
        'princeton_camera'     : PrincetonCameraConfigModel,
    },

    'scope_info' : {
        'keysight_visa'     : KeysightScopeDataModel,
        'dtacq'             : DtacqScopeDataModel,
        'lecroy_visa'       : LecroyScopeDataModel,
        'gf_digitizer'      : GFDigitizerDataModel,
    }
}