from ..functions.api_request import api_request

async def gender_lookup(api_key = None):
  api_response = await api_request("GET", "/lookup/gender", "", api_key)
  return api_response

async def region_lookup(api_key = None):
  api_response = await api_request("GET", "/lookup/region", "", api_key)
  return api_response

async def business_categories_lookup(api_key = None):
  api_response = await api_request("GET", "/lookup/business-categories", "", api_key)
  return api_response