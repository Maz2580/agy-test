# Copyright (c) 2026 MyCompany LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from google.oauth2 import id_token
from google.auth.transport import requests

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")

def login():
    """Base login placeholder."""
    pass

def login_with_google(token):
    """
    Verifies a Google ID token and returns user details.
    """
    try:
        # Verify the OAuth2 token using Google's verification library
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)

        # Token is valid. Retrieve standard user identity details.
        userid = idinfo['sub']
        email = idinfo.get('email')
        name = idinfo.get('name')
        picture = idinfo.get('picture')
        
        return {
            "success": True,
            "user_id": userid,
            "email": email,
            "name": name,
            "picture": picture
        }
    except ValueError as e:
        # Invalid token signature, expired, or client ID mismatch
        return {
            "success": False,
            "error": f"Invalid token: {str(e)}"
        }

