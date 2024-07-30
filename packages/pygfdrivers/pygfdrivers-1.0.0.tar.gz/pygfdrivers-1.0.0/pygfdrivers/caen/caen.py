# -----------------------------------------------------------------------------
#
# General Fusion CAEN FELib Scope Methods for Digitizer 2.0
#
# Author    : Stephen Bolanos
# Date      : 2023/08/24
#
# -----------------------------------------------------------------------------

from datetime import datetime
from math import ceil, log10
from common.scope_helper_classes import *
from common.base_scope import ScopeModel
from params import CAENScopeParams

from caen_felib import device, error

nl = "\n"


class ConfigError(Exception):
    pass


class CAENFElibScope(ScopeModel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

    def initialize(self):
        try:
            self.initializeScopeInfoObject()
            self.scope = device.connect(f"dig2://{self.configurationObject.connectionString}")
            print(f"{self.queryModelName()} SCOPE TYPE FOR SCOPE NAME ---- {self.name}")
            print(f"IP Address --- {self.queryIPAddress()}")
            self.connectionStatus = True
        except Exception as e:
            self.logToConsole(f"Error Initializing - {e}")
            self.connectionStatus = False

        self.logToConsole("Done initialization.")

    # ------------------------------------------------------------------------------------
    # Implementation Unique Methods
    # ------------------------------------------------------------------------------------

    def arm(self):
        self.logToConsole("Reset and clearing data...")
        self.cmdReset()
        self.cmdClearData()
        self.logToConsole("Configuring transient...")
        self.configureTransient()
        self.logToConsole("Arming...")
        self.cmdArmAcquisition()
        self.cmdSwStartAcquisition()

    def configureTransient(self):
        # configure scope with
        # TTL rising edge trigger from front panel input to capture
        # internal timestamps captured when capture is started
        # armed when software command is given
        # disable subsequent captures once the first event is done
        self.scope.par.IOLevel.value = "TTL"
        self.scope.par.TstampResetSource.value = "Start"
        self.scope.par.EnAutoDisarmAcq.value = "True"
        self.scope.par.StartSource.value = "SWcmd"

        # set trigger source between internal or externally triggered
        if self.configurationObject.triggerType == "internal":
            self.setAcqTriggerSource("SWTrg")
        else:
            self.setAcqTriggerSource("TrgIn")

        # set record record length by sample size
        self.setRecordLengthS(self.configurationObject.postMemSize)
        self.setTriggerDelayS(self.configurationObject.preMemSize)
        # self.setPreTriggerS(self.configurationObject.preMemSize) 
        reclen = self.configurationObject.preMemSize + self.configurationObject.postMemSize

        # capture total number of available channels on the scope
        nch = int(self.scope.par.NumCh.value)

        # configure all scope channels
        for ch_num in range(1, nch+1):
            # if channel is active based on user config, enable channel and set its offset
            # otherwise disable channel to speed up data download
            if ch_num in self.configurationObject.activeChannels:
                dc_offset = self.configurationObject.channelsConfigSettings[ch_num]["vOffset"]
                self.scope.ch[ch_num-1].par.ChEnable.value = "True"
                self.scope.ch[ch_num-1].par.DCOffset.value = f"{dc_offset}"
            else:
                self.scope.ch[ch_num-1].par.ChEnable.value = "False"

        # configure how the data is downloaded from the scope
        self.setActiveEndpoint("scope")
        data_format = self.setScopeDataFormat(nch, reclen)
        self.data = self.configureDataDownload(data_format)
        self.logToConsole("Finished configuring transient.")

    def waitForTrigger(self):
        try:
            # read_data() is set to block infinitely until new data is received or
            # function encounters an exception
            self.downloadData(self.data)
            self.scope.cmd.DisarmAcquisition()
            return True
        except error.Error as e:
            self.logToConsole(f"{e.func} encountered exception - {e.code}")
            self.scope.cmd.DisarmAcquisition()
            return False

    def trigger_software(self):
        self.cmdSendSWTrigger()

    def clear(self):
        # Ensure no old data present on new acquisition
        self.cmdClearData()

    def abort(self):
        # Ensure now new acquisition runs even if EnAutoDisarmAcq is disabled, then stop any
        # acquisitions that may already be occurring.
        self.scope.cmd.SwStopAcquisition()
        self.scope.cmd.DisarmAcquisition()
    
    def reset(self):
        self.cmdReset()

    def idn(self):
        pass

    """
    Override these from inherting classes    \/
    """
    
    # ------------------------------------------------------------------------------------
    # Get Methods
    # ------------------------------------------------------------------------------------

    # Grab Acquire Mode
    def queryAcquireMode(self):
        pass
    
    # Grab Trigger Mode
    def queryTriggerMode(self):
        return self.scope.par.StartSource.value
    
    # Grab Trigger Edge
    def queryTriggerEdge(self):
        pass
    
    # Grab Trigger Delay in seconds
    def queryTriggerDelay(self):
        sample_freq = float(self.querySamplingFrequency())
        pre_samples = float(self.queryPreTriggerS())
        trig_delay = pre_samples * (1 / sample_freq)

        return float(trig_delay)
    
    # Grab Trigger Source 
    def queryTriggerSource(self):
        trig_source = self.scope.par.AcqTriggerSource.value
        return trig_source

    def queryTriggerLevel(self):
        pass
    
    # Time Offset
    def queryTimeOffset(self):
        return None

    # Sampling Frequency
    def querySamplingFrequency(self):
        nom_sample_freq = float(self.queryADCSampleRate()) * 1.0e6
        decimation_factor = float(self.queryDecimationFactor())
        sample_freq = nom_sample_freq / decimation_factor
        return sample_freq

    # Number of points (Memory Size)
    def queryNumberOfPoints(self):
        pre_sample = int(self.queryPreTriggerS())
        post_sample = int(self.queryRecordLengthS())
        trig_delay = int(self.queryTriggerDelayS())
        total_samples = pre_sample + post_sample + trig_delay
        return total_samples
    
    # Time Division tdiv
    def queryTimeDivision(self):
        pass
        
    # Probe
    def queryProbeAttenuationForChannel(self, channel):
        pass

    # Voltage Division / Channel vdiv
    def queryVoltageDivisionForChannel(self, channel):
        pass
    
    # Voltage Offset
    def queryVoltageOffsetForChannel(self, channel):
        return self.configurationObject.channelsConfigSettings[channel]["vOffset"]
    
    # BW Limit
    def queryBWLimit(self, channel):
        pass

    # Coupling AC DC
    def queryCouplingForChannel(self, channel):
        pass

    # Trigger status
    def queryTriggerStatus(self):
        try:
            triggerStatus = (self.currentShot != self.queryTriggerIDMode())
            self.logToConsole(f"Trigger Status : {triggerStatus}")
            return triggerStatus
        except Exception as e:
            self.logToConsole(f"Erroy querying trigger status : {e}")

    # Arm status
    def queryArmStatus(self):
        try:
            armStatus = (self.queryAcquisitionStatus() == "Armed")
            self.logToConsole(f"Arm Status : {armStatus}")
        except Exception as e:
            self.logToConsole(f"Error querying arm status : {e}")

    # ------------------------------------------------------------------------------------
    #  Set Methods
    # ------------------------------------------------------------------------------------

    def setSingle(self, enable):
        pass

    # Setting acquire mode between normal (real-time) or segmented
    def setAcquireMode(self):
        pass

    # Trigger Delay
    def setTriggerDelay(self, trig_delay):
        pass

    # Trigger Source
    def setTriggerSource(self, source:str=None):
        if source == "external":
            self.setAcqTriggerSource("TrgIn")
        elif source == "internal":
            self.setAcqTriggerSource("SWTrg")
        else:
            self.logToConsole(f"{CAENScopeParams.ACQ_TRIG_SOURCE} - only")
        self.logToConsole(f"Trigger source set to {self.queryTriggerSource()}")

    def setTriggerMode(self, mode:str=None):
        if mode == "external":
            self.setStartSource("SINedge")
        elif mode == "internal":
            self.setStartSource("SWcmd")
        else:
            self.logToConsole(f"{CAENScopeParams.START_SOURCE} - only")
        self.logToConsole(f"Trigger mode set to {self.queryTriggerMode()}")
    
    # Trigger Level
    def setTriggerLevel(self, channel="AUX", level= None):
        pass

    def setTriggerEdge(self, slope="POS"):
        pass
    
    # Wave Format
    def setWaveFormFormat(self, wFormat=None):
        pass

    # Time Division
    def setTimeDivision(self, tdiv=None):
        pass
    
    # Y Increment voltage Division
    def setYIncrementForChannel(self, channel, vdiv=None):
        pass

    # System Header
    def setSystemHeader(self, state=None):
        pass
    
    # Beep
    def setBeepForHzDuration(self, hz, duration):
        pass

    # Time Offset
    def setTimeOffset(self, tOffset=None):
        pass

    #Set Sampling Frequency
    def setSamplingFrequency(self,sampFreq = None):
        pass

    def setCoupling(self,channel,coupling=None):
        pass

    #Set Memory Depth
    def setMemoryDepth(self, numPoints= None):
        pass

    # set attenuation for channel
    def setProbeAttenuationForChannel(self, channel, attn=None):
        pass

    # ------------------------------------------------------------------------------------
    #  Get Data Methods
    # ------------------------------------------------------------------------------------

    def populateVoltValueForActiveChannels(self):
        """
        Reads and stores the data for all active channels after a shot and converts it into 
        voltage values. Only the active channels are read and stored.
        """
        start = datetime.now()
        self.clearScopeInfoData()
        self.logToConsole(f"Collecting metadata...")
        self.populateMetaData()
        self.logToConsole(f"Downloading Data...")
        try:
            npChannelsArray = self.data[1].value
            # npWaveSize = self.data[2].value
        except Exception as e:
            self.logToConsole(f"Issues downloading raw data - {e}")

        for channel in self.configurationObject.activeChannels:
            ch_start = datetime.now()

            self.scopeInfo.channels[str(channel)].rawData = npChannelsArray[channel - 1][::-1].tolist()
            # self.scopeInfo.channels[str(channel)].waveSize = npWaveSize[channel - 1].tolist()
            self.logToConsole(f"Finished downloading raw data for channel {channel} in {datetime.now() - ch_start} s")
            # self.formatRawBinaryDataForChannel(channel)

        self.logToConsole(f"Finished reading raw data for active channels in {datetime.now() - start} s")

    def formatRawBinaryDataForChannel(self, channel:int, site:int=None):
        """
        Looks for raw data in a channel object and formats it into proper voltage values 
        based on channel's readData settings. Floats are rounded based on input voltage 
        range to ensure full resolution is visible.
        """
        try:
            absChan = channel

            rawData = self.scopeInfo.channels[str(absChan)].rawData

            if rawData is None:
                self.logToConsole("No raw data found for channel")
                return None

            conversion_factor = float(self.queryADCToVoltsFactor(channel))
            voltRange = float(self.scopeInfo.channels[str(absChan)].channelConfig.probe)
            offset_percent = self.configurationObject.channelsConfigSettings[channel]["vOffset"]
            offset_volts = (float(offset_percent) / 100.0) * float(voltRange)

            # Values are given in the range of a signed int16, and must be scaled using the voltage range
            intMax = 2**(self.queryADCBitDepth())-1 # 2/(2^16 - 1)

            # Always ensures that we can see the smallest resolution of the voltage range change.
            # One extra decimal place is added to avoid rounding errors.
            decimalPlaces = ceil(-log10(voltRange / intMax)) + 1

            volts = [round((counts * conversion_factor) - offset_volts, decimalPlaces) for counts in rawData]
            self.scopeInfo.channels[str(absChan)].voltValue = volts
            
            self.logToConsole(f"Finished populating volt values for channel {channel}.")
            # self.logToConsole(f"Data from this channel {channel} - volts: {volts[0:20]} - rawData: {len(rawData)} - {rawData[0:20]}")
        except Exception as e:
            self.logToConsole(f"Error formatting binary data : {e}")

    def decodeChannel(self, channelId:int, siteId:int=None):
        """
        Takes either a local channel id with site, or an absolute channel id, and fills in 
        the missing value and returns: site_id, local_channel_id, absolute_channel_id
        """
        totalChannels = 0
        absoluteChannelId = None

        channelId = int(channelId)
        siteId = int(siteId) if siteId is not None else siteId
        # self.sites is ordered by site number where s1 is the first entry

        if siteId is not None:
            localChannelId = channelId
            # Take absolute channel id and give back the site id with local channel id
            for site in self.sites:
                if site.site == siteId:
                    absoluteChannelId = totalChannels + channelId
                    break

                totalChannels += site.nchan

        else:
            localChannelId = None
            absoluteChannelId = channelId
            for site in self.sites:
                adjustedChannel = channelId - totalChannels
                if adjustedChannel <= site.nchan:
                    siteId = site.site
                    localChannelId = adjustedChannel
                    break

                totalChannels += site.nchan

        if localChannelId is None:
            raise ConfigError(f"Couldn't find the site for channel {absoluteChannelId}, check your config")

        return siteId, localChannelId, absoluteChannelId
    
    # ------------------------------------------------------------------------------------
    #  Meta Data Population
    # ------------------------------------------------------------------------------------
    def populateMetaData(self):
        self.populateChannelMetaData()
        self.populateTimeSeriesMetaData()

    # Grab time series data from scope
    def populateTimeSeriesMetaData(self):
        try: 
            self.scopeInfo.timeSeriesData.triggerDelay = self.queryTriggerDelay()
        except Exception as e: self.logToConsole(f"Error - MetaData population - querying trigger delay - Error: {e} ")

        try: 
            self.scopeInfo.timeSeriesData.frequency = self.querySamplingFrequency()
        except Exception as e: self.logToConsole(f"Error - MetaData population - sampling Frequency - Error: {e} ")

        try: 
            self.scopeInfo.timeSeriesData.offset = self.queryTimeOffset()
        except Exception as e: self.logToConsole(f"Error - MetaData population - time Offset - Error: {e} ")

        try: 
            self.scopeInfo.timeSeriesData.num_points = self.queryNumberOfPoints()
        except Exception as e: self.logToConsole(f"Error - MetaData population - number of points - Error: {e} ")

        try: 
            self.scopeInfo.timeSeriesData.delta_t = 1 / self.scopeInfo.timeSeriesData.frequency
        except Exception as e: self.logToConsole(f"Error - MetaData population - delta T - Error: {e} ")

        try: 
            self.scopeInfo.timeSeriesData.t_zero = self.queryTriggerDelay()
        except Exception as e: self.logToConsole(f"Error - MetaData population - t zero - Error: {e} ")

    # Grab Channel Data From Scope
    def populateChannelMetaData(self):
        for channel in self.configurationObject.activeChannels:
            try:
                self.scopeInfo.channels[str(channel)].channelReadData.name = self.scopeInfo.channels[str(channel)].channelConfig.name
            except Exception as e: self.logToConsole(f"Error - MetaData population - channel: {channel} - Name - Error: {e} ")
            try:
                self.scopeInfo.channels[str(channel)].channelReadData.id = self.scopeInfo.channels[str(channel)].channelConfig.id
            except Exception as e: self.logToConsole(f"Error - MetaData population - channel: {channel} - ID - Error: {e} ")
            try: 
                self.scopeInfo.channels[str(channel)].channelReadData.vOffset = self.queryVoltageOffsetForChannel(channel)
            except Exception as e: self.logToConsole(f"Error - MetaData population - channel: {channel} - voltage offset - Error: {e} ")

    # ------------------------------------------------------------------------------------
    # Helper Methods
    # ------------------------------------------------------------------------------------
    
    def is_valid_arg(self, args, valid_args):
        for arg in args.split("|"):
            if arg not in valid_args:
                raise ValueError(f"'{arg}' is not a valid option.")
            
        self.logToConsole("Options are all valid.")
        return True

    # ------------------------------------------------------------------------------------
    # CAEN Query Methods
    # TODO: Need to move these methods into its own driver file to be more reuseable
    # ------------------------------------------------------------------------------------

    def queryCupVer(self) -> str:
        """
        Returns a string of the Code Update (CUp) version currently in use in the format 
        “scope-YYYYMMDDNN” where YYYY year, MM month, DD day, and NN a progressive daily 
        index of the release.
        """
        return self.scope.par.CupVer.value
    
    def queryFPGAFirmwareVer(self) -> str:
        """
        Returns build version of the FPGA firmware currently in use as a string (eg. “0.4.183”).
        """
        return self.scope.par.FPGA_FwVer.value
    
    def queryFirmwareType(self):
        """
        Returns Digital Pulse Processing (DPP) firmware type as string of one the following:
            "DPP_PHA"        # Pulse Height Analysis
            "DPP_ZLE"        # Zero Length Encoding
            "DPP_PSD"        # Charge Integration and Pulse Shape Processing
            "DPP_DAW"        # Dynamic Acquisition Window
            "DPP_OPEN"       # Open (unknown status as of Aug. 25, 2023)
            "Scope"          # Digitizer 2.0 Waveform Recording Firmware
        """
        return self.scope.par.FwType.value
    
    def queryModelCode(self):
        """
        Returns CAEN model code as string (eg. "WV2740XAAAAA").
        """
        return self.scope.par.ModelCode.value
    
    def queryModelName(self):
        """
        Returns CAEN model name as string (eg. "V2740").
        """
        return self.scope.par.ModelName.value
    
    def querySerialNum(self):
        """
        Returns CAEN serial number as string (eg. "12741").
        """
        return self.scope.par.SerialNum.value
    
    def queryNumCh(self):
        """
        Returns number of available input channels as int.
        """
        return self.scope.par.SerialNum.value
    
    def queryADCBitDepth(self):
        """
        Returns number of bits of the ADCs as int.
        """
        return int(self.scope.par.ADC_Nbit.value)
    
    def queryADCSampleRate(self):
        """
        Returns sampling rate of the ADCs as int in [MS/s] unit.
        """
        return self.scope.par.ADC_SamplRate.value
    
    def queryADCToVoltsFactor(self, ch_num):
        """
        Returns factor to convert ADC counts to volts as float in [Vpp] units.
        """
        ch = self.scope.ch[ch_num]
        return ch.par.ADCToVolts.value
    
    def queryInputRange(self):
        """
        Returns input dynamic range as int in [Vpp] unit.
        """
        return self.scope.par.InputRange.value
    
    def queryInputType(self):
        """
        Returns input type as int where 1 if single ended, 0 if differential.
        """
        return self.scope.par.InputType.value
    
    def queryZin(self):
        """
        Returns input impedance of the analog channels as int in [Ohms] unit.
        """
        return self.scope.par.Zin.value
    
    def queryIPAddress(self):
        """
        Returns IP address as string (eg. "10.105.252.100")
        """
        return self.scope.par.IPAddress.value
    
    def queryNetmask(self):
        """
        Returns Netmask as string (eg. "255.255.255.0")
        """
        return self.scope.par.Netmask.value
    
    def queryGateway(self):
        """
        Returns Gateway as string (eg. "10.105.254.254")
        """
        return self.scope.par.Gateway.value
    
    def queryClockSource(self):
        """
        Returns string of source of the system clock.
        
        See CAENScopeParams.Clock.SOURCE for possible sources.
        """
        return self.scope.par.ClockSource.value
    
    def queryEnClockOutFP(self):
        """
        Returns True if clock output on front panel is enabled, False if not
        """
        return self.scope.par.EnClockOutFP.value
    
    def queryLedStatus(self):
        """
        Returns True if clock output on front panel is enabled, False if not
        """
        return self.scope.par.LedStatus.value

    def queryTriggerIDMode(self):
        """
        Returns the counting mode of the of a 24-bit identifier called TriggerID.
        """
        return self.scope.par.TriggerIDMode.value
    
    def queryEnAutoDisarmAcq(self):
        """
        Returns True if scope is enable to disarm the acquisition at the stop of run, else False
        """
        return self.scope.par.EnAutoDisarmAcq.value
    
    def queryTStampResetSource(self):
        """
        Returns source of the timestamp reset as string ().
        """
        return self.scope.par.TStampResetSource.value
    
    def queryAcquisitionStatus(self):
        """
        Returns a 32-bit word representing the acquisition status of the digitizer.
        """
        return self.scope.par.AcquisitionStatus.value
    
    def queryMaxRawDataSize(self):
        """
        Returns max size returned from a single GetData call from raw endpoint as int in [bytes].
        """
        return self.scope.par.MaxRawDataSize.value
    
    def queryWaveDataSource(self):
        """
        Return the source location of the ADC data as a string.
        """
        return self.scope.par.WaveDataSource.value
    
    def queryRecordLengthS(self):
        """
        Return the size of the acquisition window as an int in [samples] unit.
        """
        return self.scope.par.RecordLengthS.value
    
    def queryPreTriggerS(self):
        """
        Return the number of samples capture before trigger as int in [samples] unit.
        """
        return self.scope.par.PreTriggerS.value
    
    def queryTriggerDelayS(self):
        """
        Return the number of samples that represents the delay added to the acquisition trigger
        as int in [samples] unit.
        """
        return self.scope.par.TriggerDelayS.value
    
    def queryDecimationFactor(self):
        """
        Return the decimation factor to be applied to the Digitizer nominal sampling frequency.
        """
        return self.scope.par.DecimationFactor.value
    
    
    # ------------------------------------------------------------------------------------
    # CAEN Set Methods
    # TODO: Need to move these methods into its own driver file to be more reuseable
    # ------------------------------------------------------------------------------------

    def setStartSource(self, source):
        """
        Defines the source for the start of run. Multiple options are allowed, separated by “|”.

        See available options in CAENScopeParams.START_SOURCE
        """
        try:
            if source in CAENScopeParams.START_SOURCE:
                self.scope.par.StartSource.value = f"{source}"
            else:
                raise ValueError(f"'{source}' is not a valid option.")
        except Exception as e:
            self.logToConsole(f"setStartSource encountered exception - {e}")
            self.logToConsole(f"Valid AcqTriggerSources - {CAENScopeParams.START_SOURCE}")
    
    # Trigger Source
    def setAcqTriggerSource(self, source):
        """
        Defines the source for the Acquisition Trigger, which is the signal that opens 
        the acquisition window and saves the waveforms in the memory buffers. Multiple 
        options are allowed, separated by “|”.

        See available options in CAENScopeParams.Trigger.SOURCE
        """
        try:
            if source in CAENScopeParams.ACQ_TRIG_SOURCE:
                self.scope.par.AcqTriggerSource.value = f"{source}"
            else:
                raise ValueError(f"'{source}' is not a valid option.")
        except Exception as e:
            self.logToConsole(f"setAcqTriggerSource encountered exception - {e}")
            self.logToConsole(f"Valid AcqTriggerSources - {CAENScopeParams.ACQ_TRIG_SOURCE}")
    
    def setClockSource(self, clock_source):
        """
        Set source of the system clock (see CAENScopeParams.CLOCK_SOURCE for args).
        """
        try:
            if clock_source in CAENScopeParams.CLOCK_SOURCE:
                self.scope.par.ClockSource.value = f"{clock_source}"
            else:
                raise ValueError(f"'{clock_source}' is not a valid option.")
        except Exception as e:
            self.logToConsole(f"setClockSource encountered exception - {e}")
            self.logToConsole(f"Valid Clock Sources - {CAENScopeParams.CLOCK_SOURCE}")
    
    def setEnClockOutFP(self, enable):
        """
        Enables or disables the front panel clock output for daisy chaining clocks.
        """
        try:
            if not isinstance(enable, bool):
                raise ValueError("arg must be a boolean.")  
            else:
                self.scope.par.EnClockOutFP.value = f"{enable}"
        except Exception as e:
            self.logToConsole(f"setEnClockOutFP encountered exception - {e}")

    def setEnAutoDisarmAcq(self, enable):
        """
        Enables or disables if scope will restart acquisition run at the stop of a run.

        When the start of run is controlled by an external signal, this options prevents 
        the digitizer to restart without the intervention of the software.
        """
        try:
            if not isinstance(enable, bool):
                raise ValueError("arg must be a boolean.")  
            else:
                self.scope.par.EnAutoDisarmAcq.value = f"{enable}"
        except Exception as e:
            self.logToConsole(f"setEnAutoDisarmAcq encountered exception - {e}")

    def setTriggerIDMode(self, id):
        try:
            if id in CAENScopeParams.TRIG_ID_MODE:
                self.scope.par.TriggerIDMode.value = id
            else:
                raise ValueError(f"'{id}' is not a valid option.")
        except Exception as e:
            self.logToConsole(f"setTriggerIDMode encountered exception - {e}")
            self.logToConsole(f"Valid Trigger ID Modes - {CAENScopeParams.TRIG_ID_MODE}")

    def setWaveDataSource(self, wave_source):
        try:
            if wave_source in CAENScopeParams.WAVE_DATA_SOURCE:
                self.scope.par.WaveDataSource.value = f"{wave_source}"
            else:
                raise ValueError(f"'{wave_source}' is not a valid wave source.")
        except Exception as e:
            self.logToConsole(f"setWaveDataSource encountered exception - {e}")
            self.logToConsole(f"Valid Wave Data Sources - {CAENScopeParams.WAVE_DATA_SOURCE}")

    def setRecordLengthS(self, record_length):
        try:
            if record_length > 10_485_760 or record_length < 0:
                raise ValueError(f"'{record_length}' is outsite of the valid range.")
            else:
                self.scope.par.RecordLengthS.value = f"{record_length}"
        except Exception as e:
            self.logToConsole(f"setRecordLengthS encountered exception - {e}")
            self.logToConsole(f"Valid range between 0 to 10_485_760 [samples]")

    def setPreTriggerS(self, pre_trig):
        try:
            if pre_trig > 2042 or pre_trig < 0:
                raise ValueError(f"'{pre_trig}' is outsite of the valid range.")
            else:
                self.scope.par.PreTriggerS.value = f"{pre_trig}"
        except Exception as e:
            self.logToConsole(f"setPreTriggerS encountered exception - {e}")
            self.logToConsole(f"Valid range between 0 to 2042 [samples]")

    def setTriggerDelayS(self, trig_delay):
        try:
            if  0 <= trig_delay <= 34_359_738_360:
                self.scope.par.TriggerDelayS.value = f"{trig_delay}"
            else:
                raise ValueError(f"'{trig_delay}' is outside of the valid range.")
        except Exception as e:
            self.logToConsole(f"setTriggerDelayS encountered exception - {e}")
            self.logToConsole(f"Valid range between 0 to 34_359_738_360 [ns]")

    def setChEnable(self, ch_num):
        try:
            if isinstance(ch_num, int) and 0 <= ch_num <= 63:
                self.scope.ch.par.ChEnable.value = f"{ch_num}"
            else:
                raise ValueError(f"'{ch_num}' is outsite of the valid range or not an int.")        
        except Exception as e:
            self.logToConsole(f"setChEnable encountered exception - {e}")
            self.logToConsole(f"Valid channel numbers are 0 to 63.")

    def setDCOfffset(self, dc_offset):
        """
        Sets the DC offset of a channel using whole percents of the full-scale count, 
        where full-scale counts is 2^(bits)-1 ADC counts.
        """
        try:
            if isinstance(dc_offset, int) and 0 <= dc_offset <= 100:
                self.scope.ch.par.DCOffset.value = f"{dc_offset}"
            else:
                raise ValueError(f"'{dc_offset}' is outsite of the valid range or not an int.")        
        except Exception as e:
            self.logToConsole(f"setDCOffset encountered exception - {e}")
            self.logToConsole(f"Valid whole percent range are 0 to 100.")

    def setDecimationFactor(self, factor):
        """
        Sets the decimation factor to be applied to the Digitizer nominal sampling frequency.
        If enabled, the RecordLengthT, PreTriggerT and TriggerDelayT parameter versions should 
        not be used.
        """
        try:
            if isinstance(factor, int) and factor in CAENScopeParams.DEC_FACTOR:
                self.scope.par.DecimationFactor.value = f"{factor}"
            else:
                raise ValueError(f"'{factor}' is not a valid option.")        
        except Exception as e:
            self.logToConsole(f"setDecimationFactor encountered exception - {e}")
            self.logToConsole(f"Valid Decimation Factors - {CAENScopeParams.DEC_FACTOR}")

    # ------------------------------------------------------------------------------------
    # CAEN Command Methods
    # TODO: Need to move these methods into its own driver file to be more reuseable
    # ------------------------------------------------------------------------------------

    def cmdReset(self):
        self.scope.cmd.Reset()
    
    def cmdClearData(self):
        self.scope.cmd.ClearData()

    def cmdArmAcquisition(self):
        self.scope.cmd.ArmAcquisition()

    def cmdDisarmAcquisition(self):
        self.scope.cmd.DisarmAcquisition()

    def cmdSwStartAcquisition(self):
        self.scope.cmd.SwStartAcquisition()

    def cmdSwStopAcquisition(self):
        self.scope.cmd.SwStopAcquisition()

    def cmdSendSWTrigger(self):
        self.scope.cmd.SendSWTrigger()

    def cmdReloadCalibration(self):
        self.scope.cmd.ReloadCalibration()

    # ------------------------------------------------------------------------------------
    # CAEN Waveform Methods
    # TODO: Need to move these methods into its own driver file to be more reuseable
    # ------------------------------------------------------------------------------------

    def setActiveEndpoint(self, opt):
        try:
            if opt in CAENScopeParams.ACTIVE_ENDPOINT:
                self.scope.endpoint.par.ActiveEndpoint.value = f"{opt}"
            else:
                raise ValueError(f"'{opt}' is not a valid active endpoint.")
        except Exception as e:
            self.logToConsole(f"setActiveEndpoint encountered exception - {e}")
            self.logToConsole(f"Valid Active Endpoints - {CAENScopeParams.ACTIVE_ENDPOINT}")

    def setScopeDataFormat(self, nch, reclen):
        data_format = [
            { "name": "TIMESTAMP", "type": "U64"},
            { "name": "WAVEFORM", "type": "U16", "dim": 2, "shape": [nch, reclen]},
            { "name": "WAVEFORM_SIZE",  "type": "U64", "dim": 1, "shape": [nch]}
        ]
        return data_format

    def configureDataDownload(self, data_format):
        return self.scope.endpoint.scope.set_read_data_format(data_format)
    
    def downloadData(self, buffer):
        self.scope.endpoint.scope.read_data(-1, buffer)