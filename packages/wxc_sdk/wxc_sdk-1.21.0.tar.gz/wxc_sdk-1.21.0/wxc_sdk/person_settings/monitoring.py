"""
call monitoring API
"""
from typing import Optional, Union

from pydantic import Field

from .common import PersonSettingsApiChild
from ..base import ApiModel, webex_id_to_uuid
from ..common import MonitoredMember, CallParkExtension

__all__ = ['MonitoredElementMember', 'MonitoredElement', 'Monitoring',
           'MonitoringApi']


class MonitoredElementMember(MonitoredMember):
    #: The location ID for the location.
    location_id: Optional[str] = None

    @property
    def ci_location_id(self) -> Optional[str]:
        return self.location_id and webex_id_to_uuid(self.location_id)


class MonitoredElement(ApiModel):
    #: monitored person or place
    member: Optional[MonitoredElementMember] = None
    #: monitored call park extension
    cpe: Optional[CallParkExtension] = Field(alias='callparkextension', default=None)


class Monitoring(ApiModel):
    #: Call park notification is enabled or disabled.
    call_park_notification_enabled: Optional[bool] = None
    #: Settings of monitored elements which can be person, place, or call park extension.
    #: for updates IDs can be used directly instead of :class:`MonitoredElement` objects
    monitored_elements: Optional[list[Union[str, MonitoredElement]]] = None

    @property
    def monitored_cpes(self) -> list[CallParkExtension]:
        return [me.cpe for me in self.monitored_elements or []
                if me.cpe]

    @property
    def monitored_members(self) -> list[MonitoredElementMember]:
        return [me.member for me in self.monitored_elements or []
                if me.member]


class MonitoringApi(PersonSettingsApiChild):
    """
    API for person's call monitoring settings
    """

    feature = 'monitoring'

    def read(self, person_id: str, org_id: str = None) -> Monitoring:
        """
        Retrieve a Person's Monitoring Settings

        Retrieves the monitoring settings of the person, which shows specified people, places or, call park
        extensions under monitoring. Monitors the line status which indicates if a person or place is on a call and
        if  a call has been parked on that extension.

        This API requires a full, user, or read-only administrator auth token with a scope of spark-admin:people_read.

        :param person_id: Unique identifier for the person.
        :type person_id: str
        :param org_id: Person is in this organization. Only admin users of another organization (such as partners)
            may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        :return: monitoring settings
        :rtype: :class:`Monitoring`
        """
        ep = self.f_ep(person_id=person_id)
        params = org_id and {'orgId': org_id} or None
        data = self.get(ep, params=params)
        return Monitoring.model_validate(data)

    def configure(self, person_id: str, settings: Monitoring, org_id: str = None):
        """
        Configure Call Waiting Settings for a Person

        Configure a Person's Call Waiting Settings

        With this feature, a person can place an active call on hold and answer an incoming call. When enabled,
        while you are on an active call, a tone alerts you of an incoming call and you can choose to answer or ignore
        the call.

        This API requires a full or user administrator auth token with the spark-admin:people_write scope.

        :param person_id: Unique identifier for the person.
        :type person_id: str
        :param settings: settings for update
        :type settings: :class:`Monitoring`
        :param org_id: Person is in this organization. Only admin users of another organization (such as partners)
            may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        """
        ep = self.f_ep(person_id=person_id)
        params = org_id and {'orgId': org_id} or None
        data = {}
        if settings.call_park_notification_enabled is not None:
            data['enableCallParkNotification'] = settings.call_park_notification_enabled
        if settings.monitored_elements is not None:
            id_list = []
            for me in settings.monitored_elements:
                if isinstance(me, str):
                    id_list.append(me)
                else:
                    id_list.append(me.member and me.member.member_id or me.cpe and me.cpe.cpe_id)
            data['monitoredElements'] = id_list
        self.put(ep, params=params, json=data)
