from percoweb_functions import *

token = auth_token(server, headers_login)

operator = pd.DataFrame(json.loads(operators(token).text)["rows"])
