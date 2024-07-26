# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities
from . import outputs

__all__ = [
    'HostPoolScheduledAgentUpdates',
    'HostPoolScheduledAgentUpdatesSchedule',
    'ScalingPlanHostPool',
    'ScalingPlanSchedule',
    'GetHostPoolScheduledAgentUpdateResult',
    'GetHostPoolScheduledAgentUpdateScheduleResult',
]

@pulumi.output_type
class HostPoolScheduledAgentUpdates(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "useSessionHostTimezone":
            suggest = "use_session_host_timezone"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HostPoolScheduledAgentUpdates. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HostPoolScheduledAgentUpdates.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HostPoolScheduledAgentUpdates.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: Optional[bool] = None,
                 schedules: Optional[Sequence['outputs.HostPoolScheduledAgentUpdatesSchedule']] = None,
                 timezone: Optional[str] = None,
                 use_session_host_timezone: Optional[bool] = None):
        """
        :param bool enabled: Enables or disables scheduled updates of the AVD agent components (RDAgent, Geneva Monitoring agent, and side-by-side stack) on session hosts. If this is enabled then up to two `schedule` blocks must be defined. Default is `false`.
               
               > **NOTE:** if `enabled` is set to `true` then at least one and a maximum of two `schedule` blocks must be provided.
        :param Sequence['HostPoolScheduledAgentUpdatesScheduleArgs'] schedules: A `schedule` block as defined below. A maximum of two blocks can be added.
        :param str timezone: Specifies the time zone in which the agent update schedule will apply, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/). If `use_session_host_timezone` is enabled then it will override this setting. Default is `UTC`
        :param bool use_session_host_timezone: Specifies whether scheduled agent updates should be applied based on the timezone of the affected session host. If configured then this setting overrides `timezone`. Default is `false`.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if schedules is not None:
            pulumi.set(__self__, "schedules", schedules)
        if timezone is not None:
            pulumi.set(__self__, "timezone", timezone)
        if use_session_host_timezone is not None:
            pulumi.set(__self__, "use_session_host_timezone", use_session_host_timezone)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Enables or disables scheduled updates of the AVD agent components (RDAgent, Geneva Monitoring agent, and side-by-side stack) on session hosts. If this is enabled then up to two `schedule` blocks must be defined. Default is `false`.

        > **NOTE:** if `enabled` is set to `true` then at least one and a maximum of two `schedule` blocks must be provided.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def schedules(self) -> Optional[Sequence['outputs.HostPoolScheduledAgentUpdatesSchedule']]:
        """
        A `schedule` block as defined below. A maximum of two blocks can be added.
        """
        return pulumi.get(self, "schedules")

    @property
    @pulumi.getter
    def timezone(self) -> Optional[str]:
        """
        Specifies the time zone in which the agent update schedule will apply, [the possible values are defined here](https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/). If `use_session_host_timezone` is enabled then it will override this setting. Default is `UTC`
        """
        return pulumi.get(self, "timezone")

    @property
    @pulumi.getter(name="useSessionHostTimezone")
    def use_session_host_timezone(self) -> Optional[bool]:
        """
        Specifies whether scheduled agent updates should be applied based on the timezone of the affected session host. If configured then this setting overrides `timezone`. Default is `false`.
        """
        return pulumi.get(self, "use_session_host_timezone")


@pulumi.output_type
class HostPoolScheduledAgentUpdatesSchedule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dayOfWeek":
            suggest = "day_of_week"
        elif key == "hourOfDay":
            suggest = "hour_of_day"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HostPoolScheduledAgentUpdatesSchedule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HostPoolScheduledAgentUpdatesSchedule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HostPoolScheduledAgentUpdatesSchedule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 day_of_week: str,
                 hour_of_day: int):
        """
        :param str day_of_week: The day of the week on which agent updates should be performed. Possible values are `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, and `Sunday`
        :param int hour_of_day: The hour of day the update window should start. The update is a 2 hour period following the hour provided. The value should be provided as a number between 0 and 23, with 0 being midnight and 23 being 11pm. A leading zero should not be used.
        """
        pulumi.set(__self__, "day_of_week", day_of_week)
        pulumi.set(__self__, "hour_of_day", hour_of_day)

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> str:
        """
        The day of the week on which agent updates should be performed. Possible values are `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, and `Sunday`
        """
        return pulumi.get(self, "day_of_week")

    @property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> int:
        """
        The hour of day the update window should start. The update is a 2 hour period following the hour provided. The value should be provided as a number between 0 and 23, with 0 being midnight and 23 being 11pm. A leading zero should not be used.
        """
        return pulumi.get(self, "hour_of_day")


@pulumi.output_type
class ScalingPlanHostPool(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "hostpoolId":
            suggest = "hostpool_id"
        elif key == "scalingPlanEnabled":
            suggest = "scaling_plan_enabled"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScalingPlanHostPool. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScalingPlanHostPool.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScalingPlanHostPool.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 hostpool_id: str,
                 scaling_plan_enabled: bool):
        """
        :param str hostpool_id: The ID of the HostPool to assign the Scaling Plan to.
        :param bool scaling_plan_enabled: Specifies if the scaling plan is enabled or disabled for the HostPool.
        """
        pulumi.set(__self__, "hostpool_id", hostpool_id)
        pulumi.set(__self__, "scaling_plan_enabled", scaling_plan_enabled)

    @property
    @pulumi.getter(name="hostpoolId")
    def hostpool_id(self) -> str:
        """
        The ID of the HostPool to assign the Scaling Plan to.
        """
        return pulumi.get(self, "hostpool_id")

    @property
    @pulumi.getter(name="scalingPlanEnabled")
    def scaling_plan_enabled(self) -> bool:
        """
        Specifies if the scaling plan is enabled or disabled for the HostPool.
        """
        return pulumi.get(self, "scaling_plan_enabled")


@pulumi.output_type
class ScalingPlanSchedule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "daysOfWeeks":
            suggest = "days_of_weeks"
        elif key == "offPeakLoadBalancingAlgorithm":
            suggest = "off_peak_load_balancing_algorithm"
        elif key == "offPeakStartTime":
            suggest = "off_peak_start_time"
        elif key == "peakLoadBalancingAlgorithm":
            suggest = "peak_load_balancing_algorithm"
        elif key == "peakStartTime":
            suggest = "peak_start_time"
        elif key == "rampDownCapacityThresholdPercent":
            suggest = "ramp_down_capacity_threshold_percent"
        elif key == "rampDownForceLogoffUsers":
            suggest = "ramp_down_force_logoff_users"
        elif key == "rampDownLoadBalancingAlgorithm":
            suggest = "ramp_down_load_balancing_algorithm"
        elif key == "rampDownMinimumHostsPercent":
            suggest = "ramp_down_minimum_hosts_percent"
        elif key == "rampDownNotificationMessage":
            suggest = "ramp_down_notification_message"
        elif key == "rampDownStartTime":
            suggest = "ramp_down_start_time"
        elif key == "rampDownStopHostsWhen":
            suggest = "ramp_down_stop_hosts_when"
        elif key == "rampDownWaitTimeMinutes":
            suggest = "ramp_down_wait_time_minutes"
        elif key == "rampUpLoadBalancingAlgorithm":
            suggest = "ramp_up_load_balancing_algorithm"
        elif key == "rampUpStartTime":
            suggest = "ramp_up_start_time"
        elif key == "rampUpCapacityThresholdPercent":
            suggest = "ramp_up_capacity_threshold_percent"
        elif key == "rampUpMinimumHostsPercent":
            suggest = "ramp_up_minimum_hosts_percent"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScalingPlanSchedule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScalingPlanSchedule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScalingPlanSchedule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 days_of_weeks: Sequence[str],
                 name: str,
                 off_peak_load_balancing_algorithm: str,
                 off_peak_start_time: str,
                 peak_load_balancing_algorithm: str,
                 peak_start_time: str,
                 ramp_down_capacity_threshold_percent: int,
                 ramp_down_force_logoff_users: bool,
                 ramp_down_load_balancing_algorithm: str,
                 ramp_down_minimum_hosts_percent: int,
                 ramp_down_notification_message: str,
                 ramp_down_start_time: str,
                 ramp_down_stop_hosts_when: str,
                 ramp_down_wait_time_minutes: int,
                 ramp_up_load_balancing_algorithm: str,
                 ramp_up_start_time: str,
                 ramp_up_capacity_threshold_percent: Optional[int] = None,
                 ramp_up_minimum_hosts_percent: Optional[int] = None):
        """
        :param Sequence[str] days_of_weeks: A list of Days of the Week on which this schedule will be used. Possible values are `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, and `Sunday`
        :param str name: The name of the schedule.
        :param str off_peak_load_balancing_algorithm: The load Balancing Algorithm to use during Off-Peak Hours. Possible values are `DepthFirst` and `BreadthFirst`.
        :param str off_peak_start_time: The time at which Off-Peak scaling will begin. This is also the end-time for the Ramp-Down period. The time must be specified in "HH:MM" format.
        :param str peak_load_balancing_algorithm: The load Balancing Algorithm to use during Peak Hours. Possible values are `DepthFirst` and `BreadthFirst`.
        :param str peak_start_time: The time at which Peak scaling will begin. This is also the end-time for the Ramp-Up period. The time must be specified in "HH:MM" format.
        :param int ramp_down_capacity_threshold_percent: This is the value in percentage of used host pool capacity that will be considered to evaluate whether to turn on/off virtual machines during the ramp-down and off-peak hours. For example, if capacity threshold is specified as 60% and your total host pool capacity is 100 sessions, autoscale will turn on additional session hosts once the host pool exceeds a load of 60 sessions.
        :param bool ramp_down_force_logoff_users: Whether users will be forced to log-off session hosts once the `ramp_down_wait_time_minutes` value has been exceeded during the Ramp-Down period. Possible
        :param str ramp_down_load_balancing_algorithm: The load Balancing Algorithm to use during the Ramp-Down period. Possible values are `DepthFirst` and `BreadthFirst`.
        :param int ramp_down_minimum_hosts_percent: The minimum percentage of session host virtual machines that you would like to get to for ramp-down and off-peak hours. For example, if Minimum percentage of hosts is specified as 10% and total number of session hosts in your host pool is 10, autoscale will ensure a minimum of 1 session host is available to take user connections.
        :param str ramp_down_notification_message: The notification message to send to users during Ramp-Down period when they are required to log-off.
        :param str ramp_down_start_time: The time at which Ramp-Down scaling will begin. This is also the end-time for the Ramp-Up period. The time must be specified in "HH:MM" format.
        :param str ramp_down_stop_hosts_when: Controls Session Host shutdown behaviour during Ramp-Down period. Session Hosts can either be shutdown when all sessions on the Session Host have ended, or when there are no Active sessions left on the Session Host. Possible values are `ZeroSessions` and `ZeroActiveSessions`.
        :param int ramp_down_wait_time_minutes: The number of minutes during Ramp-Down period that autoscale will wait after setting the session host VMs to drain mode, notifying any currently signed in users to save their work before forcing the users to logoff. Once all user sessions on the session host VM have been logged off, Autoscale will shut down the VM.
        :param str ramp_up_load_balancing_algorithm: The load Balancing Algorithm to use during the Ramp-Up period. Possible values are `DepthFirst` and `BreadthFirst`.
        :param str ramp_up_start_time: The time at which Ramp-Up scaling will begin. This is also the end-time for the Ramp-Up period. The time must be specified in "HH:MM" format.
        :param int ramp_up_capacity_threshold_percent: This is the value of percentage of used host pool capacity that will be considered to evaluate whether to turn on/off virtual machines during the ramp-up and peak hours. For example, if capacity threshold is specified as `60%` and your total host pool capacity is `100` sessions, autoscale will turn on additional session hosts once the host pool exceeds a load of `60` sessions.
        :param int ramp_up_minimum_hosts_percent: Specifies the minimum percentage of session host virtual machines to start during ramp-up for peak hours. For example, if Minimum percentage of hosts is specified as `10%` and total number of session hosts in your host pool is `10`, autoscale will ensure a minimum of `1` session host is available to take user connections.
        """
        pulumi.set(__self__, "days_of_weeks", days_of_weeks)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "off_peak_load_balancing_algorithm", off_peak_load_balancing_algorithm)
        pulumi.set(__self__, "off_peak_start_time", off_peak_start_time)
        pulumi.set(__self__, "peak_load_balancing_algorithm", peak_load_balancing_algorithm)
        pulumi.set(__self__, "peak_start_time", peak_start_time)
        pulumi.set(__self__, "ramp_down_capacity_threshold_percent", ramp_down_capacity_threshold_percent)
        pulumi.set(__self__, "ramp_down_force_logoff_users", ramp_down_force_logoff_users)
        pulumi.set(__self__, "ramp_down_load_balancing_algorithm", ramp_down_load_balancing_algorithm)
        pulumi.set(__self__, "ramp_down_minimum_hosts_percent", ramp_down_minimum_hosts_percent)
        pulumi.set(__self__, "ramp_down_notification_message", ramp_down_notification_message)
        pulumi.set(__self__, "ramp_down_start_time", ramp_down_start_time)
        pulumi.set(__self__, "ramp_down_stop_hosts_when", ramp_down_stop_hosts_when)
        pulumi.set(__self__, "ramp_down_wait_time_minutes", ramp_down_wait_time_minutes)
        pulumi.set(__self__, "ramp_up_load_balancing_algorithm", ramp_up_load_balancing_algorithm)
        pulumi.set(__self__, "ramp_up_start_time", ramp_up_start_time)
        if ramp_up_capacity_threshold_percent is not None:
            pulumi.set(__self__, "ramp_up_capacity_threshold_percent", ramp_up_capacity_threshold_percent)
        if ramp_up_minimum_hosts_percent is not None:
            pulumi.set(__self__, "ramp_up_minimum_hosts_percent", ramp_up_minimum_hosts_percent)

    @property
    @pulumi.getter(name="daysOfWeeks")
    def days_of_weeks(self) -> Sequence[str]:
        """
        A list of Days of the Week on which this schedule will be used. Possible values are `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, and `Sunday`
        """
        return pulumi.get(self, "days_of_weeks")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the schedule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="offPeakLoadBalancingAlgorithm")
    def off_peak_load_balancing_algorithm(self) -> str:
        """
        The load Balancing Algorithm to use during Off-Peak Hours. Possible values are `DepthFirst` and `BreadthFirst`.
        """
        return pulumi.get(self, "off_peak_load_balancing_algorithm")

    @property
    @pulumi.getter(name="offPeakStartTime")
    def off_peak_start_time(self) -> str:
        """
        The time at which Off-Peak scaling will begin. This is also the end-time for the Ramp-Down period. The time must be specified in "HH:MM" format.
        """
        return pulumi.get(self, "off_peak_start_time")

    @property
    @pulumi.getter(name="peakLoadBalancingAlgorithm")
    def peak_load_balancing_algorithm(self) -> str:
        """
        The load Balancing Algorithm to use during Peak Hours. Possible values are `DepthFirst` and `BreadthFirst`.
        """
        return pulumi.get(self, "peak_load_balancing_algorithm")

    @property
    @pulumi.getter(name="peakStartTime")
    def peak_start_time(self) -> str:
        """
        The time at which Peak scaling will begin. This is also the end-time for the Ramp-Up period. The time must be specified in "HH:MM" format.
        """
        return pulumi.get(self, "peak_start_time")

    @property
    @pulumi.getter(name="rampDownCapacityThresholdPercent")
    def ramp_down_capacity_threshold_percent(self) -> int:
        """
        This is the value in percentage of used host pool capacity that will be considered to evaluate whether to turn on/off virtual machines during the ramp-down and off-peak hours. For example, if capacity threshold is specified as 60% and your total host pool capacity is 100 sessions, autoscale will turn on additional session hosts once the host pool exceeds a load of 60 sessions.
        """
        return pulumi.get(self, "ramp_down_capacity_threshold_percent")

    @property
    @pulumi.getter(name="rampDownForceLogoffUsers")
    def ramp_down_force_logoff_users(self) -> bool:
        """
        Whether users will be forced to log-off session hosts once the `ramp_down_wait_time_minutes` value has been exceeded during the Ramp-Down period. Possible
        """
        return pulumi.get(self, "ramp_down_force_logoff_users")

    @property
    @pulumi.getter(name="rampDownLoadBalancingAlgorithm")
    def ramp_down_load_balancing_algorithm(self) -> str:
        """
        The load Balancing Algorithm to use during the Ramp-Down period. Possible values are `DepthFirst` and `BreadthFirst`.
        """
        return pulumi.get(self, "ramp_down_load_balancing_algorithm")

    @property
    @pulumi.getter(name="rampDownMinimumHostsPercent")
    def ramp_down_minimum_hosts_percent(self) -> int:
        """
        The minimum percentage of session host virtual machines that you would like to get to for ramp-down and off-peak hours. For example, if Minimum percentage of hosts is specified as 10% and total number of session hosts in your host pool is 10, autoscale will ensure a minimum of 1 session host is available to take user connections.
        """
        return pulumi.get(self, "ramp_down_minimum_hosts_percent")

    @property
    @pulumi.getter(name="rampDownNotificationMessage")
    def ramp_down_notification_message(self) -> str:
        """
        The notification message to send to users during Ramp-Down period when they are required to log-off.
        """
        return pulumi.get(self, "ramp_down_notification_message")

    @property
    @pulumi.getter(name="rampDownStartTime")
    def ramp_down_start_time(self) -> str:
        """
        The time at which Ramp-Down scaling will begin. This is also the end-time for the Ramp-Up period. The time must be specified in "HH:MM" format.
        """
        return pulumi.get(self, "ramp_down_start_time")

    @property
    @pulumi.getter(name="rampDownStopHostsWhen")
    def ramp_down_stop_hosts_when(self) -> str:
        """
        Controls Session Host shutdown behaviour during Ramp-Down period. Session Hosts can either be shutdown when all sessions on the Session Host have ended, or when there are no Active sessions left on the Session Host. Possible values are `ZeroSessions` and `ZeroActiveSessions`.
        """
        return pulumi.get(self, "ramp_down_stop_hosts_when")

    @property
    @pulumi.getter(name="rampDownWaitTimeMinutes")
    def ramp_down_wait_time_minutes(self) -> int:
        """
        The number of minutes during Ramp-Down period that autoscale will wait after setting the session host VMs to drain mode, notifying any currently signed in users to save their work before forcing the users to logoff. Once all user sessions on the session host VM have been logged off, Autoscale will shut down the VM.
        """
        return pulumi.get(self, "ramp_down_wait_time_minutes")

    @property
    @pulumi.getter(name="rampUpLoadBalancingAlgorithm")
    def ramp_up_load_balancing_algorithm(self) -> str:
        """
        The load Balancing Algorithm to use during the Ramp-Up period. Possible values are `DepthFirst` and `BreadthFirst`.
        """
        return pulumi.get(self, "ramp_up_load_balancing_algorithm")

    @property
    @pulumi.getter(name="rampUpStartTime")
    def ramp_up_start_time(self) -> str:
        """
        The time at which Ramp-Up scaling will begin. This is also the end-time for the Ramp-Up period. The time must be specified in "HH:MM" format.
        """
        return pulumi.get(self, "ramp_up_start_time")

    @property
    @pulumi.getter(name="rampUpCapacityThresholdPercent")
    def ramp_up_capacity_threshold_percent(self) -> Optional[int]:
        """
        This is the value of percentage of used host pool capacity that will be considered to evaluate whether to turn on/off virtual machines during the ramp-up and peak hours. For example, if capacity threshold is specified as `60%` and your total host pool capacity is `100` sessions, autoscale will turn on additional session hosts once the host pool exceeds a load of `60` sessions.
        """
        return pulumi.get(self, "ramp_up_capacity_threshold_percent")

    @property
    @pulumi.getter(name="rampUpMinimumHostsPercent")
    def ramp_up_minimum_hosts_percent(self) -> Optional[int]:
        """
        Specifies the minimum percentage of session host virtual machines to start during ramp-up for peak hours. For example, if Minimum percentage of hosts is specified as `10%` and total number of session hosts in your host pool is `10`, autoscale will ensure a minimum of `1` session host is available to take user connections.
        """
        return pulumi.get(self, "ramp_up_minimum_hosts_percent")


@pulumi.output_type
class GetHostPoolScheduledAgentUpdateResult(dict):
    def __init__(__self__, *,
                 enabled: bool,
                 schedules: Sequence['outputs.GetHostPoolScheduledAgentUpdateScheduleResult'],
                 timezone: str,
                 use_session_host_timezone: bool):
        """
        :param bool enabled: Are scheduled updates of the AVD agent components (RDAgent, Geneva Monitoring agent, and side-by-side stack) enabled on session hosts.
        :param Sequence['GetHostPoolScheduledAgentUpdateScheduleArgs'] schedules: A `schedule` block as defined below.
        :param str timezone: The time zone in which the agent update schedule will apply.
        :param bool use_session_host_timezone: Specifies whether scheduled agent updates should be applied based on the timezone of the affected session host.
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "schedules", schedules)
        pulumi.set(__self__, "timezone", timezone)
        pulumi.set(__self__, "use_session_host_timezone", use_session_host_timezone)

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Are scheduled updates of the AVD agent components (RDAgent, Geneva Monitoring agent, and side-by-side stack) enabled on session hosts.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def schedules(self) -> Sequence['outputs.GetHostPoolScheduledAgentUpdateScheduleResult']:
        """
        A `schedule` block as defined below.
        """
        return pulumi.get(self, "schedules")

    @property
    @pulumi.getter
    def timezone(self) -> str:
        """
        The time zone in which the agent update schedule will apply.
        """
        return pulumi.get(self, "timezone")

    @property
    @pulumi.getter(name="useSessionHostTimezone")
    def use_session_host_timezone(self) -> bool:
        """
        Specifies whether scheduled agent updates should be applied based on the timezone of the affected session host.
        """
        return pulumi.get(self, "use_session_host_timezone")


@pulumi.output_type
class GetHostPoolScheduledAgentUpdateScheduleResult(dict):
    def __init__(__self__, *,
                 day_of_week: str,
                 hour_of_day: int):
        """
        :param str day_of_week: The day of the week on which agent updates should be performed.
        :param int hour_of_day: The hour of day the update window should start.
        """
        pulumi.set(__self__, "day_of_week", day_of_week)
        pulumi.set(__self__, "hour_of_day", hour_of_day)

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> str:
        """
        The day of the week on which agent updates should be performed.
        """
        return pulumi.get(self, "day_of_week")

    @property
    @pulumi.getter(name="hourOfDay")
    def hour_of_day(self) -> int:
        """
        The hour of day the update window should start.
        """
        return pulumi.get(self, "hour_of_day")


