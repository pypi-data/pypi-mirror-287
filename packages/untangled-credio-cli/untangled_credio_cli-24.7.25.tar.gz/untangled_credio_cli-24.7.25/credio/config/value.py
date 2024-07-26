"""Commonly-used values."""

import ipfshttpclient
import os


DEFAULT_SERVER_HOST = "0.0.0.0"
DEFAULT_SERVER_PORT = 8080
DEFAULT_SUPABASE_SCHEMA = "public"
DEFAULT_STORAGE_PATH = os.path.expanduser("~")
DEFAULT_IPFS_GATEWAY = str(ipfshttpclient.DEFAULT_ADDR)
DEFAULT_JWT_SECRET_KEY = ""
DEFAULT_JWT_ALGORITHM = "HS256"
DEFAULT_JWT_VALIDITY = 300
