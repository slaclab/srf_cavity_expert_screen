from lcls_tools.superconducting.scLinac import SSA, CryoDict


class ExpertSSA(SSA):
    def __init__(self, cavity):
        super().__init__(cavity)
        self.drain_voltage_setpoint_pv: str = self.pv_addr("DrainVoltSetpt")
        self.drain_voltage_readback_pv: str = self.pv_addr("DrainVoltRBV")

        self.dc_enable_pv: str = self.pv_addr("DCEnable")
        self.dc_enable_readback_pv: str = self.pv_addr("DCEnableRBV")

        self.rf_enable_pv: str = self.pv_addr("RFEnable")
        self.rf_enable_readback_pv: str = self.pv_addr("RFEnableRBV")

        self.reset_internal_fault_pv: str = self.pv_addr("FaultIntReset")
        self.reset_external_fault_pv: str = self.pv_addr("FaultExtReset")
        self.reset_warning_pv: str = self.pv_addr("WarningReset")
        self.reboot_system_pv: str = self.pv_addr("SystemReboot")
        self.fan_alarm_sum_pv: str = self.pv_addr("FanAlarmSum.SEVR")


EXPERT_CRYOMODULE_OBJECTS = CryoDict(ssaClass=ExpertSSA)
