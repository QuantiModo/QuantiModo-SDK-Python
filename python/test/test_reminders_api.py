# coding: utf-8

"""
    QuantiModo

    QuantiModo makes it easy to retrieve normalized user data from a wide array of devices and applications. [Learn about QuantiModo](https://quantimo.do), check out our [docs](https://github.com/QuantiModo/docs) or contact us at [help.quantimo.do](https://help.quantimo.do). 

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.reminders_api import RemindersApi


class TestRemindersApi(unittest.TestCase):
    """ RemindersApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.reminders_api.RemindersApi()

    def tearDown(self):
        pass

    def test_v1_tracking_reminder_notifications_get(self):
        """
        Test case for v1_tracking_reminder_notifications_get

        Get specific pending tracking reminders
        """
        pass

    def test_v1_tracking_reminder_notifications_skip_post(self):
        """
        Test case for v1_tracking_reminder_notifications_skip_post

        Skip a pending tracking reminder
        """
        pass

    def test_v1_tracking_reminder_notifications_snooze_post(self):
        """
        Test case for v1_tracking_reminder_notifications_snooze_post

        Snooze a pending tracking reminder
        """
        pass

    def test_v1_tracking_reminder_notifications_track_post(self):
        """
        Test case for v1_tracking_reminder_notifications_track_post

        Track a pending tracking reminder
        """
        pass

    def test_v1_tracking_reminders_delete_post(self):
        """
        Test case for v1_tracking_reminders_delete_post

        Delete tracking reminder
        """
        pass

    def test_v1_tracking_reminders_get(self):
        """
        Test case for v1_tracking_reminders_get

        Get repeating tracking reminder settings
        """
        pass

    def test_v1_tracking_reminders_post(self):
        """
        Test case for v1_tracking_reminders_post

        Store a Tracking Reminder
        """
        pass


if __name__ == '__main__':
    unittest.main()