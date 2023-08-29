from lcls_tools.superconducting.scLinac import (
    SSA,
    CryoDict,
    Cavity,
    StepperTuner,
    Piezo,
)


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


class ExpertCavity(Cavity):
    def __init__(
        self,
        cavityNum,
        rackObject,
        ssaClass=ExpertSSA,
        stepperClass=StepperTuner,
        piezoClass=Piezo,
    ):
        super().__init__(cavityNum, rackObject, ssaClass=ExpertSSA)
        self.hw_mode_des_pv: str = self.pv_addr("HWMODEDES")


EXPERT_CRYOMODULE_OBJECTS = CryoDict(ssaClass=ExpertSSA, cavityClass=ExpertCavity)
