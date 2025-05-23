#JSON Web Tokens
#
#
# Structue (css)
 xxxxx.yyyyy.zzzzz
 [Header].[Payload].[Signature]
#
#
#
# Payload (json)
 {
  "sub": "devnet_user",
  "exp": 1717000000,
  "role": "admin"
 }
#
#
# Authorization Header
 Authorization: Bearer <your_jwt_here>
#
#
#
# Environement Variables for a Secure Config
# Python File
import os

api_key = os.getenv("MERAKI_API_KEY")
#
# .env file
MERAKI_API_KEY=123abc456def
FLASK_ENV=development
#
#
# Bash to Run
 pip install python-dotenv
