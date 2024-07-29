from collections.abc import Generator
from dataclasses import dataclass
from typing import Optional

from pydantic import Field

from .intercept import LocationInterceptApi
from .internal_dialing import InternalDialingApi
from .moh import LocationMoHApi
from .numbers import LocationNumbersApi
from .receptionist_contacts import ReceptionistContactsDirectoryApi
from .vm import LocationVoicemailSettingsApi
from ...api_child import ApiChild
from ...base import ApiModel, to_camel
from ...common import ValidateExtensionsResponse, RouteType, DeviceCustomization
from ...locations import Location
from ...rest import RestSession

__all__ = ['CallingLineId', 'PSTNConnection', 'TelephonyLocation', 'TelephonyLocationApi']


class CallingLineId(ApiModel):
    """
    Location calling line information.
    """
    #: Group calling line ID name. By default it will be org name.
    #: when updating the name make sure to also include the phone number
    name: Optional[str] = None
    #: Directory Number / Main number in E164 Forma
    phone_number: Optional[str] = None


class PSTNConnection(ApiModel):
    """
    Connection details
    """
    #: Webex Calling location only supports TRUNK and ROUTE_GROUP connection type.
    type: RouteType
    #: A unique identifier of route type.
    id: str


class TelephonyLocation(ApiModel):
    #: A unique identifier for the location.
    location_id: Optional[str] = Field(alias='id', default=None)
    #: The name of the location.
    name: Optional[str] = None
    #: Location's phone announcement language.
    announcement_language: Optional[str] = None
    #: Location calling line information.
    calling_line_id: Optional[CallingLineId] = None
    #: Connection details are only returned for local PSTN types of TRUNK or ROUTE_GROUP.
    connection: Optional[PSTNConnection] = None
    #: External Caller ID Name value. Unicode characters.
    external_caller_id_name: Optional[str] = None
    #: Limit on the number of people at the location, Read-Only.
    user_limit: Optional[int] = None
    #: Location Identifier.
    p_access_network_info: Optional[str] = None
    #: Must dial to reach an outside line, default is None.
    outside_dial_digit: Optional[str] = None
    #: Must dial a prefix when calling between locations having same extension within same location.
    routing_prefix: Optional[str] = None
    #: Chargeable number for the line placing the call. When this is set, all calls placed from this location will
    #: include a P-Charge-Info header with the selected number in the SIP INVITE.
    charge_number: Optional[str] = None
    #: IP Address, hostname, or domain, Read-Only
    default_domain: Optional[str] = None
    #: True if E911 setup is required.
    e911_setup_required: Optional[bool] = None
    #: True when enforcing outside dial digit at location level to make PSTN calls.
    enforce_outside_dial_digit: Optional[bool] = None
    # TODO: undocumented
    subscription_id: Optional[str] = None
    # TODO: undocumented, item 169
    carrier_account_id: Optional[str] = None

    def update(self) -> dict:
        """
        restricted data used for updates

        :meta private:
        """
        data = self.model_dump(mode='json', exclude_unset=True, by_alias=True,
                               exclude={'location_id', 'name', 'user_limit', 'default_domain',
                                        'e911_setup_required', 'subscription_id', 'carrier_account_id'})
        if not self.connection:
            data.pop('connection', None)
        return data


@dataclass(init=False)
class TelephonyLocationApi(ApiChild, base='telephony/config/locations'):
    #: call intercept settings
    intercept: LocationInterceptApi
    #: internal dialing settings
    internal_dialing: InternalDialingApi
    #: moh settings
    moh: LocationMoHApi
    #: number settings
    number: LocationNumbersApi
    #: Location VM settings (only enable/disable transcription for now)
    voicemail: LocationVoicemailSettingsApi
    #: Receptionist contacts directories
    receptionist_contacts_directory: ReceptionistContactsDirectoryApi

    def __init__(self, session: RestSession):
        super().__init__(session=session)
        self.intercept = LocationInterceptApi(session=session)
        self.internal_dialing = InternalDialingApi(session=session)
        self.moh = LocationMoHApi(session=session)
        self.number = LocationNumbersApi(session=session)
        self.voicemail = LocationVoicemailSettingsApi(session=session)
        self.receptionist_contacts_directory = ReceptionistContactsDirectoryApi(session=session)

    def generate_password(self, location_id: str, generate: list[str] = None, org_id: str = None):
        """
        Generates an example password using the effective password settings for the location. If you don't specify
        anything in the generate field or don't provide a request body, then you will receive a SIP password by default.

        It's used while creating a trunk and shouldn't be used anywhere else.

        Generating an example password requires a full or write-only administrator auth token with a scope
        of spark-admin:telephony_config_write.

        :param location_id: Location for which example password has to be generated.
        :type location_id: str
        :param generate: password settings array.
        :type generate: list[str]
        :param org_id: Organization to which location belongs.
        :type org_id: str
        :return: new password
        :rtype: str
        """
        params = org_id and {'orgId': org_id} or None
        body = generate and {'generate': generate} or {}
        url = self.ep(f'{location_id}/actions/generatePassword/invoke')
        data = self.post(url=url, params=params, json=body)
        return data['exampleSipPassword']

    def validate_extensions(self, location_id: str, extensions: list[str],
                            org_id: str = None) -> ValidateExtensionsResponse:
        """
        Validate extensions for a specific location.

        Validating extensions requires a full administrator auth token with a scope
        of spark-admin:telephony_config_write.

        :param location_id: Validate extensions for this location.
        :type location_id: str
        :param extensions: Array of extensions that will be validated.
        :type extensions: list[str]
        :param org_id: Validate extensions for this organization.
        :type org_id: str
        :return: Validation result
        :rtype: :class:`wxc_sdk.common.ValidateExtensionsResponse`
        """
        url = self.ep(f'{location_id}/actions/validateExtensions/invoke')
        body = {'extensions': extensions}
        params = org_id and {'orgId': org_id} or None
        data = self.post(url=url, params=params, json=body)
        return ValidateExtensionsResponse.model_validate(data)

    def details(self, location_id: str, org_id: str = None) -> TelephonyLocation:
        """
        Shows Webex Calling details for a location, by ID.

        Specify the location ID in the locationId parameter in the URI.

        Searching and viewing location in your organization requires an administrator auth token with
        the spark-admin:telephony_config_read scope.

        :param location_id: Retrieve Webex Calling location attributes for this location.
        :type location_id: str
        :param org_id: Retrieve Webex Calling location attributes for this organization.
        :type org_id: str
        :return: Webex Calling details for location
        :rtype: :class:`TelephonyLocation`
        """
        params = org_id and {'orgId': org_id}
        url = self.ep(location_id)
        data = self.get(url=url, params=params)
        return TelephonyLocation.model_validate(data)

    def enable_for_calling(self, location: Location, org_id: str = None) -> str:
        """
        Enable a location by adding it to Webex Calling. This add Webex Calling support to a location created
        using the POST /v1/locations API.

        Locations are used to support calling features which can be defined at the location level.

        This API requires a full administrator auth token with a scope of spark-admin:telephony_config_write.

        :return: A unique identifier for the location.
        :rtype: str
        """
        params = org_id and {'orgId': org_id}
        url = self.ep()
        body = location.model_dump_json()
        data = self.post(url=url, data=body, params=params)
        return data['id']

    def list(self, name: str = None, order: str = None, org_id: str = None) -> Generator[TelephonyLocation, None, None]:
        """
        Lists Webex Calling locations for an organization with Webex Calling details.

        Searching and viewing locations with Webex Calling details in your organization require an administrator auth
        token with the spark-admin:telephony_config_read scope.

        :param name: List locations whose name contains this string.
        :type name: str
        :param order: Sort the list of locations based on name, either asc or desc.
        :type order: str
        :param org_id: List locations for this organization.
        :type org_id: str
        :return: generator of :class:`TelephonyLocation` instances
        """
        params = {to_camel(k): v
                  for k, v in locals().items()
                  if k != 'self' and v is not None}
        url = self.ep()
        return self.session.follow_pagination(url=url, model=TelephonyLocation, params=params, item_key='locations')

    def update(self, location_id: str, settings: TelephonyLocation, org_id: str = None) -> Optional[str]:
        """
        Update Webex Calling details for a location, by ID.

        Specify the location ID in the locationId parameter in the URI.

        Modifying the connection via API is only supported for the local PSTN types of TRUNK and ROUTE_GROUP.

        Updating a location in your organization requires an administrator auth token with
        the spark-admin:telephony_config_write scope.

        Example :

            .. code-block:: python

                api.telephony.location.update(location_id=location_id,
                                              settings=TelephonyLocation(
                                                  calling_line_id=CallingLineId(
                                                      phone_number=tn),
                                                  routing_prefix=routing_prefix,
                                                  outside_dial_digit='9'))

        :param location_id: Updating Webex Calling location attributes for this location.
        :type location_id: str
        :param settings: settings to update
        :type settings: :class:`TelephonyLocation`
        :param org_id: Updating Webex Calling location attributes for this organization.
        :type org_id: str
        :return: batch job id of update job if one is created
        :rtype: str
        """
        data = settings.update()
        params = org_id and {'orgId': org_id} or None
        url = self.ep(location_id)
        data = self.put(url=url, json=data, params=params)
        if data:
            return data.get('batchJobId')
        return

    def change_announcement_language(self, location_id: str, language_code: str, agent_enabled: bool = None,
                                     service_enabled: bool = None, org_id: str = None):
        """
        Change Announcement Language

        Change announcement language for the given location.

        Change announcement language for current people/workspaces and/or existing feature configurations. This does
        not change the default announcement language which is applied to new users/workspaces and new feature
        configurations.

        Changing announcement language for the given location requires a full administrator auth token with a scope
        of spark-admin:telephony_config_write.

        :param location_id: Change announcement language for this location.
        :type location_id: str
        :param language_code: Language code.
        :type language_code: str
        :param agent_enabled: Set to true to change announcement language for existing people and workspaces.
        :type agent_enabled: bool
        :param service_enabled: Set to true to change announcement language for existing feature configurations.
        :type service_enabled: bool
        :param org_id: Change announcement language for this organization.
        :type org_id: str
        """
        params = org_id and {'orgId': org_id} or None
        body = {'announcementLanguageCode': language_code}
        if agent_enabled is not None:
            body['agentEnabled'] = agent_enabled
        if service_enabled is not None:
            body['serviceEnabled'] = service_enabled
        url = self.session.ep(f'{location_id}/actions/modifyAnnouncementLanguage/invoke')
        self.put(url, json=body, params=params)

    def device_settings(self, location_id: str, org_id: str = None) -> DeviceCustomization:
        """
        Get device override settings for a location.

        This requires a full or read-only administrator auth token with a scope of spark-admin:telephony_config_read.

        :param location_id: Unique identifier for the location
        :type location_id: str
        :param org_id: Settings on the device in this organization
        :type org_id: str
        :return: device customization response
        :rtype: DeviceCustomization
        """
        params = org_id and {'orgId': org_id} or None
        url = self.ep(f'{location_id}/devices/settings')
        data = self.get(url=url, params=params)
        return DeviceCustomization.model_validate(data)
