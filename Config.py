import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get(6218111662:AAHDZb3owNWP_i9dXsQxB4swYTT_k_lBTrA", "")
    STRING_SESSION = os.environ.get("1BVtsOLcBu6Yk5OP7mjf9n2fUx1VW2bwIcmsL0RXsexjz7pSlKp5CFuEZgzk8aDF4_Dbu98ze3sqnpMFdATSMOiMtl7bS-dymQXOBuT_qyOHY31jFqrQyXTECdXgFfrqy6dPGCcXPy_AEA8QiNPGB3EyGc84G15XZiFWejYs0bPtoq5Oga2fLjdy_fCyM45tsCo03nxOzIN4KIi0kGl2CjLWXbqBWGAcsK8GrPAhr50Res9fs95vNMms8UABpdPBBl5J8mQJ4KTvIrW3DwCHJ6L7dLwfZp6VJLMDvotdT7ZcBZxl3swtqMu_tDq7ZOrVIhaSR9f5TGIXamHUhdbjtGFyG6CWc74w=", "")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
