from dtacq.dtacq_scope import DtacqScope
from gf.gf_visa_digitizer import GFVisaDigitizer
from lecroy.lecroy_visa_scope import LecroyVisaScope
from avantes.spec_avantes import AvantesSpectrometer
from keysight.keysight_visa_scope import KeysightVisaScope
from princeton_instruments.princeton_camera import PrincetonCamera


device_map = {
    'scopes' : {
        'keysight_visa'         : KeysightVisaScope,
        'lecroy_visa'           : LecroyVisaScope,
        'dtacq'                 : DtacqScope,
        'gf_digitizer'          : GFVisaDigitizer,
        'avantes_spectrometer'  : AvantesSpectrometer,
    },
    'cameras' : {
        'princeton_camera'      : PrincetonCamera
    }
}
