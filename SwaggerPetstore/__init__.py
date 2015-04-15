#!/usr/bin/env python
"""Add all of the modules in the current directory to __all__"""
import os

# import models into package

from .models.connector import Connector

from .models.conversion_step import ConversionStep

from .models.correlation import Correlation

from .models.measurement import Measurement

from .models.measurement_range import MeasurementRange

from .models.measurement_source import MeasurementSource

from .models.pairs import Pairs

from .models.permission import Permission

from .models.unit import Unit

from .models.unit_category import UnitCategory

from .models.user import User

from .models.user_token_request import UserTokenRequest

from .models.user_token_successful_response import UserTokenSuccessfulResponse

from .models.user_token_failed_response import UserTokenFailedResponse

from .models.user_token_request_inner_user_field import UserTokenRequestInnerUserField

from .models.user_token_successful_response_inner_user_field import UserTokenSuccessfulResponseInnerUserField

from .models.variable import Variable

from .models.variable_category import VariableCategory

from .models.variable_user_settings import VariableUserSettings


# import apis into package

from .connectors_api import ConnectorsApi

from .oauth_api import OauthApi

from .variables_api import VariablesApi

from .administration_api import AdministrationApi

from .user_api import UserApi

from .measurements_api import MeasurementsApi

from .sharing_api import SharingApi

from .correlations_api import CorrelationsApi

from .organizations_api import OrganizationsApi

from .pairs_api import PairsApi

from .units_api import UnitsApi


# import ApiClient
from .swagger import ApiClient

__all__ = []

for module in os.listdir(os.path.dirname(__file__)):
  if module != '__init__.py' and module[-3:] == '.py':
    __all__.append(module[:-3])
