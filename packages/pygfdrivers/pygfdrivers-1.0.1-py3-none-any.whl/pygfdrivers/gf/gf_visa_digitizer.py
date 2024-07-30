# Author: Ethan Labbe
# Date  : 5/6/2024

"""
Available USB commands found in device_gfdigi_task.c file programmed into Atmel
microcontroller chip on-board.

File can be found in the gf_digitizer repo:
../gf_digitizer/microcontroller/GFDigitizer/src/GFDIGITIZER/device_gfdigi_task.c

Available commands:

    # chan = 2 digit zero padded channel_number min: 01, max: 10
    # state = 'ac' or 'dc' <- has to be lower case
    "set_coupling_state chan=xx state="
        i.e. Set channel 1 to AC coupling mode
        "set_coupling_state chan=01 state=ac" 

    # chan = 2 digit zero padded channel_number min: 1, max: 10
    # value:int = min: 1, max: 16
    "set_gain_value chan=xx value="
        i.e. Set channel 2 gain value to 10
        "set_gain_value chan=02 value=10"

    # value:int = min: 0, max: 100
    "set_pwm_value pwm=triglevel value="
        i.e. Set the trigger level to 50% of full scale
        "set_pwm_value pwm=triglevel value=50"

    # chan = 2 digit zero padded channel_number min: 01, max: 10
    # avgs = 3 digit zero padded amount of readings to average into one sample point
    # start = 6 digit zero padded amount of samples to wait before reading of multiple of 32
    # number = number of samples to read, must be at least 32 and a multiple of 32
    "readdata chan=xx avgs=xxx start=xxxxxx number="
        i.e. Read 100 samples from channel 3 with no average and time offset.
        "readdata chan=03 avgs=001 start=000000 number=100"
        note: to get data you need to read using read_bytes()    
    

    # Commands without parameters
    "set_trigger_arm"
    "set_trigger_force"
    "is_trigger_armed"

Further implementation examples can be derived from GFRemote C++ control of the device. Code 
can be found in Piston SVN here:
https://gfyvritsvcs01.gf.local:8443/svn/Piston/Infrastructure/GF_Digitizer.cpp


 """

from datetime import datetime
from struct import unpack
from time import sleep

from common.visa.visa_scope import VisaScope
from gf.models.digitizer_config import GFDigitizerConfigModel
from gf.visa_commands.root import GFDigitizerRoot
from gf.visa_commands.capture import GFDigitizerCapture
from gf.visa_commands.trigger import GFDigitizerTrigger
from gf.visa_commands.channel import GFDigitizerChannel

class DIG_CONSTANTS:
    # Hardware defined
    SAMPLING_RATE    = 5e6  # [samples/s]
    TX_BUFFER_SIZE   = 4096 # [Bytes]

class GFVisaDigitizer(VisaScope):

    def __init__(self, scope_config: GFDigitizerConfigModel = None) -> None:
        super().__init__(scope_config)

    def init(self):
        super().init()
        try:
            if self.scope is None:
                raise ValueError("GF Digitizer did not connect properly.")
            self.root = GFDigitizerRoot(self)
            self.capture = GFDigitizerCapture(self)
            self.trigger = GFDigitizerTrigger(self)
            self.channel = GFDigitizerChannel(self)
            self.log.info(f"GF DIGITIZER TYPE FOR DEVICE NAME ---- {self.name}")
        except Exception as e:
            self.log.error(f"Initializing GF digitizer encountered error: {e}")

    def apply_configurations(self)-> None:
        try:
            self.capture.apply_capture_config(self.config.capture)
            self.trigger.apply_trig_config(self.config.trigger)
            self.channel.apply_ch_config(self.config.active_channels, self.config.channels)
        except Exception as e:
            self.log.error(f"Applying configuration encountered error: {e}")

    def arm(self)-> None:
        try:
            self.prep_shot()
            self.root.arm()
            sleep(self.scope_talk_delay)
            self.is_armed = True
            self.log.info('Digitizer armed')
        except Exception as e:
            self.log.error(f"Arming encountered error: {e}")

    def prep_shot(self) -> None:
        try:
            self.abort()
            self.is_armed = False
            self.is_triggered = False
            self.is_downloaded = False
            self.is_aborted = False
            self.data = None
        except Exception as e:
            self.log.error(f"Preparing shot encountered error: {e}.")

    def trigger_software(self) -> None:
        try:
            self.root.trig_force()
            sleep(self.scope_talk_delay)
            self.is_triggered = True
            self.log.info('Digitizer triggered')
        except Exception as e:
            self.log.error(f"Triggering software encountered error: {e}.")

    def abort(self) -> None:
        try:
            self.trigger_software()
            self.root.clear()
            sleep(self.scope_talk_delay)
            self.root.read_bytes(64) #if this fails digitizer firmware needs upgrade
            sleep(self.scope_talk_delay)
            self.is_triggered = False
            self.log.info('Digitizer aborted')
            self.is_aborted = True
        except Exception as e:
            self.log.error(f"Aborting shot encountered error: {e}.")
    
    def check_connection(self)-> bool:
        try:
            query = self.root.rabbit() #communicate with device to check connection
            self.is_connected = True if query is not None else False
        except Exception:
            self.is_connected = False
        finally:
            return self.is_connected

    def apply_dc_levels_settings(self)-> None:
        try:
            self.capture.acq_count = 1
            self.capture.acq_start_sample = 0
            self.capture.acq_total_samples = 64 
            for ch in self.config.active_channels:
                self.channel.set_ch(setter='ch_gain', setting=1, ch= ch)
                self.channel.set_ch(setter='ch_coupling', setting='dc', ch=ch)
        except Exception as e:
            self.log.error(f"Applying DC levels settings failed: {e}")

    # ------------------------------------------------------------------------------------
    #  Read Only Methods
    # ------------------------------------------------------------------------------------

    @property
    def arm_status(self) -> bool:
        try:
            _is_armed = self.root.arm_status
            self.log.debug(f"Armed Status: {_is_armed}")
            return _is_armed
        except Exception as e:
            self.log.error(f"Querying arm status encountered error: {e}")

    @property
    def trigger_status(self) -> bool:
        try:
            _trigger_status = self.root.trig_status
            _trigger_status = _trigger_status and self.is_armed
            self.log.debug(f"Trigger Status: {_trigger_status}")
            return _trigger_status
        except Exception as e:
            self.log.error(f"Querying trigger status encountered error: {e}")

    # ------------------------------------------------------------------------------------
    #  Fetch Data Methods
    # ------------------------------------------------------------------------------------

    def fetch_data(self):
        self.clear_scope_info_data()
        self.log.info(f"Collecting metadata...")
        self.fetch_metadata()
        self.log.info(f"Downloading Data...")
        try:
            start = datetime.now()
            for channel in self.config.active_channels:
                start_time = datetime.now()
                self.scope_info.channels[str(channel)].raw_data   = self.read_channel_data(channel)
                self.scope_info.channels[str(channel)].volt_value = self.format_channel_data(channel)
                self.log.info(f'Length of data for channel {str(channel)} : {len(self.scope_info.channels[str(channel)].volt_value):,} - elapsed time: {datetime.now()-start_time}')
            self.log.info(f"Time to download and condition data for {len(self.config.active_channels)} channels: {datetime.now() - start}")
            self.data = self.scope_info
        except Exception as e:
            self.log.error(f"Error during populating {e}")

    def fetch_metadata(self):
        try:
            self.capture.fetch_capture_config(self.scope_info.capture)
            self.trigger.fetch_trig_config(self.scope_info.trigger)
            self.channel.fetch_ch_config(self.scope_info.active_channels, self.scope_info.channels)   
        except Exception as e:
            self.log.error(f"failed fetching metadata: {e}")

    # ------------------------------------------------------------------------------------
    #  Waveform Methods
    # ------------------------------------------------------------------------------------

    def format_channel_data(self, channel, raw_data = None):
        """
        unpacks raw data from a specific channel.

        Parameters:
        channel (int): Channel number.

        Returns:
        list: Conditioned data in millivolts.
        """
        if raw_data is None:
            raw_data = self.scope_info.channels[str(channel)].raw_data
        data = []
        offset = self.scope_info.channels[str(channel)].ch_offset
        volt_range = self.scope_info.capture.volt_range
        for i in range(len(raw_data)):
            buffer_size = int(len(raw_data[i])/2)
            string_format = ">" + buffer_size*'H'   
            unpacked_data = unpack(string_format, raw_data[i])
      
            # Digitizer returns values from 0 - 4096, which maps to a range dependant on digitizer
            # mV = [(1000 * (x / 4096.0) - volt_range/2) + offset for x in unpacked_data]
            volts = [(((x - 2048) / 2048) * volt_range) + offset for x in unpacked_data]
            data.extend(volts)
        return data

    def populateVoltValueForActiveChannels(self):
        """
        Populates Meta Data gets raw data and volt values to be used in BSON file
        """ 
        self.clear_scope_info_data()
        self.log.info(f"Collecting metadata...")
        self.fetch_metadata()
        self.log.info(f"Downloading Data...")
        self.fetch_data()

    def read_channel_data(self, channel):
        """
        calculates readdata command requirements, formats and writes command to scope.
        reads and stores raw bytes
        :param int channel  : Channel that will be read
        :return: an array of raw data
        """
        try:
            raw_bytes = []
            buffer_size = DIG_CONSTANTS.TX_BUFFER_SIZE
            total_transfers, final_transfer_size = divmod(self.capture.acq_total_samples, DIG_CONSTANTS.TX_BUFFER_SIZE)
            total_transfers += 1 if final_transfer_size != 0 else 0
            self.capture.get_data(channel)
            sleep(self.scope_talk_delay)
            for i in range(int(total_transfers)):
                # Deals with last transimissions between 4096 byte packets
                if (i+1 == total_transfers):
                    buffer_size = int(final_transfer_size)

                raw_bytes.append(self.root.read_bytes(2*buffer_size))
                self.is_downloaded = True    
        except Exception as e:
            self.log.error(f"Channel {channel} failed reading data: {e}")
            self.is_downloaded = False       
        finally:
            return raw_bytes

if __name__ == "__main__":
    pass