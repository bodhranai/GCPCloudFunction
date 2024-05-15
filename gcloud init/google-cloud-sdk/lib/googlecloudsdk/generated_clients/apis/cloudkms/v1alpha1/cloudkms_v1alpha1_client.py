"""Generated client library for cloudkms version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.cloudkms.v1alpha1 import cloudkms_v1alpha1_messages as messages


class CloudkmsV1alpha1(base_api.BaseApiClient):
  """Generated client library for service cloudkms version v1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://cloudkms.googleapis.com/'
  MTLS_BASE_URL = 'https://cloudkms.mtls.googleapis.com/'

  _PACKAGE = 'cloudkms'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/cloudkms']
  _VERSION = 'v1alpha1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'CloudkmsV1alpha1'
  _URL_VERSION = 'v1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudkms handle."""
    url = url or self.BASE_URL
    super(CloudkmsV1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects = self.ProjectsService(self)

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(CloudkmsV1alpha1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def GetProjectOptOutState(self, request, global_params=None):
      r"""Checks the project metadata and returns a boolean value indicating whether or not the project has been opted out. Fails with code.INVALID_ARGUMENT if the metadata type is unsupported or no longer valid (the related MSA notification period has expired).

      Args:
        request: (CloudkmsProjectsGetProjectOptOutStateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GetProjectOptOutStateResponse) The response message.
      """
      config = self.GetMethodConfig('GetProjectOptOutState')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetProjectOptOutState.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}:getProjectOptOutState',
        http_method='GET',
        method_id='cloudkms.projects.getProjectOptOutState',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}:getProjectOptOutState',
        request_field='',
        request_type_name='CloudkmsProjectsGetProjectOptOutStateRequest',
        response_type_name='GetProjectOptOutStateResponse',
        supports_download=False,
    )

    def SetProjectOptOutState(self, request, global_params=None):
      r"""Updates the project metadata according to the new customer preference, and returns a boolean value to confirm the updated project metadata value. Fails with code.INVALID_ARGUMENT if the metadata type is unsupported or no longer valid (the related MSA notification period has expired).

      Args:
        request: (CloudkmsProjectsSetProjectOptOutStateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SetProjectOptOutStateResponse) The response message.
      """
      config = self.GetMethodConfig('SetProjectOptOutState')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetProjectOptOutState.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}:setProjectOptOutState',
        http_method='POST',
        method_id='cloudkms.projects.setProjectOptOutState',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}:setProjectOptOutState',
        request_field='setProjectOptOutStateRequest',
        request_type_name='CloudkmsProjectsSetProjectOptOutStateRequest',
        response_type_name='SetProjectOptOutStateResponse',
        supports_download=False,
    )
