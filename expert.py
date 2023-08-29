from PyQt5.QtWidgets import QComboBox, QSpinBox
from lcls_tools.superconducting.scLinac import (
    Cryomodule,
)
from lcls_tools.superconducting.sc_linac_utils import ALL_CRYOMODULES
from pydm import Display
from pydm.widgets import PyDMLabel, PyDMPushButton, PyDMSpinbox

from expert_linac import EXPERT_CRYOMODULE_OBJECTS, ExpertSSA, ExpertCavity


class ExpertDisplay(Display):
    def __init__(self):
        super().__init__(ui_filename="expert.ui")
        self.cm_combobox: QComboBox = self.ui.cm_combobox
        self.cm_combobox.addItems(ALL_CRYOMODULES)
        self.cm_combobox.currentIndexChanged.connect(self.connect_signals)

        self.cav_spinbox: QSpinBox = self.ui.cav_spinbox
        self.cav_spinbox.valueChanged.connect(self.connect_signals)

        self.ssa_status_label: PyDMLabel = self.ui.ssa_status_label
        self.ssa_on_button: PyDMPushButton = self.ui.ssa_on_button
        self.ssa_off_button: PyDMPushButton = self.ui.ssa_off_button
        self.ssa_reset_button: PyDMPushButton = self.ui.ssa_reset_button

        self.ssa_drain_voltage_spinbox: PyDMSpinbox = self.ui.ssa_drain_voltage_spinbox
        self.ssa_drain_voltage_label: PyDMLabel = self.ui.ssa_drain_voltage_label

        self.ssa_dc_enable_button: PyDMPushButton = self.ui.ssa_dc_enable_button
        self.ssa_dc_disable_button: PyDMPushButton = self.ui.ssa_dc_disable_button
        self.ssa_dc_enable_readback_label: PyDMLabel = (
            self.ui.ssa_dc_enable_readback_label
        )

        self.ssa_rf_enable_button: PyDMPushButton = self.ui.ssa_rf_enable_button
        self.ssa_rf_disable_button: PyDMPushButton = self.ui.ssa_rf_disable_button
        self.ssa_rf_enable_readback_label: PyDMLabel = (
            self.ui.ssa_rf_enable_readback_label
        )

        self.ssa_reset_internal_fault_button: PyDMPushButton = (
            self.ui.ssa_reset_internal_fault_button
        )
        self.ssa_reset_external_fault_button: PyDMPushButton = (
            self.ui.ssa_reset_external_fault_button
        )
        self.ssa_reset_warning_button: PyDMPushButton = self.ui.ssa_reset_warning_button
        self.ssa_reboot_system_button: PyDMPushButton = self.ui.ssa_reboot_system_button
        self.ssa_fan_alarm_label: PyDMLabel = self.ui.ssa_fan_alarm_label

        self.rf_mode_label: PyDMLabel = self.ui.rf_mode_label
        self.selap_button: PyDMPushButton = self.ui.selap_button
        self.sela_button: PyDMPushButton = self.ui.sela_button
        self.sel_button: PyDMPushButton = self.ui.sel_button
        self.sel_raw_button: PyDMPushButton = self.ui.sel_raw_button
        self.pulse_button: PyDMPushButton = self.ui.pulse_button
        self.chirp_button: PyDMPushButton = self.ui.chirp_button

        self.rf_state_label: PyDMLabel = self.ui.rf_state_label
        self.rf_on_button: PyDMPushButton = self.ui.rf_on_button
        self.rf_off_button: PyDMPushButton = self.ui.rf_off_button

        self.hw_mode_label: PyDMLabel = self.ui.hw_mode_label
        self.online_button: PyDMPushButton = self.ui.online_button
        self.offline_button: PyDMPushButton = self.ui.offline_button
        self.maintenance_button: PyDMPushButton = self.ui.maintenance_button
        self.maintenance_done_button: PyDMPushButton = self.ui.maintenance_done_button
        self.ready_button: PyDMPushButton = self.ui.ready_button

        self.connect_signals()

    @property
    def cavity(self) -> ExpertCavity:
        cm_obj: Cryomodule = EXPERT_CRYOMODULE_OBJECTS[self.cm_combobox.currentText()]
        return cm_obj.cavities[self.cav_spinbox.value()]

    def connect_signals(self):
        ssa: ExpertSSA = self.cavity.ssa
        self.ssa_status_label.channel = ssa.status_pv
        self.ssa_on_button.channel = ssa.turn_on_pv
        self.ssa_off_button.channel = ssa.turn_off_pv
        self.ssa_reset_button.channel = ssa.reset_pv
        self.ssa_drain_voltage_spinbox.channel = ssa.drain_voltage_setpoint_pv
        self.ssa_drain_voltage_label.channel = ssa.drain_voltage_readback_pv

        self.ssa_dc_enable_button.channel = ssa.dc_enable_pv
        self.ssa_dc_disable_button.channel = ssa.dc_enable_pv
        self.ssa_dc_enable_readback_label = ssa.dc_enable_readback_pv

        self.ssa_rf_enable_button.channel = ssa.rf_enable_pv
        self.ssa_rf_disable_button.channel = ssa.rf_enable_pv
        self.ssa_rf_enable_readback_label = ssa.rf_enable_readback_pv

        self.ssa_reset_internal_fault_button.channel = ssa.reset_internal_fault_pv
        self.ssa_reset_external_fault_button.channel = ssa.reset_external_fault_pv
        self.ssa_reset_warning_button.channel = ssa.reset_warning_pv
        self.ssa_reboot_system_button.channel = ssa.reboot_system_pv
        self.ssa_fan_alarm_label.channel = ssa.fan_alarm_sum_pv

        self.rf_mode_label.channel = self.cavity.rf_mode_pv
        self.selap_button.channel = self.cavity.rf_mode_ctrl_pv
        self.sela_button.channel = self.cavity.rf_mode_ctrl_pv
        self.sel_button.channel = self.cavity.rf_mode_ctrl_pv
        self.sel_raw_button.channel = self.cavity.rf_mode_ctrl_pv
        self.pulse_button.channel = self.cavity.rf_mode_ctrl_pv
        self.chirp_button.channel = self.cavity.rf_mode_ctrl_pv

        self.rf_state_label.channel = self.cavity.rf_state_pv
        self.rf_on_button.channel = self.cavity.rf_control_pv
        self.rf_off_button.channel = self.cavity.rf_control_pv

        self.hw_mode_label.channel = self.cavity.hw_mode_pv
        self.online_button.channel = self.cavity.hw_mode_des_pv
        self.offline_button.channel = self.cavity.hw_mode_des_pv
        self.maintenance_button.channel = self.cavity.hw_mode_des_pv
        self.maintenance_done_button.channel = self.cavity.hw_mode_des_pv
        self.ready_button.channel = self.cavity.hw_mode_des_pv
