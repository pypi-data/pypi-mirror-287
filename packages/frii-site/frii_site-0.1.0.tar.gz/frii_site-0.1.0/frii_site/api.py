from requests import Response, patch
from exceptions import InvalidDomain, InvalidType, InvalidPerms, BackendException
class API:
    def __init__(self,api_key:str,url_override:str|None=None) -> None:
        self.api_key=api_key.strip()
        self.url = "https://api.frii.site" or url_override
        self.allowed_types:list=["A","CNAME","TXT","NS"]
        
    def modify(self,domain:str,content:str,type:str) -> bool:
        """Modify a domain

        Args:
            domain (str): the domain (without the .frii.site part)
            content (str): the new content of the domain
            type (str):  the new type of the domain

        Raises:
            InvalidDomain: If your domain is invalid
            InvalidPerms: Your API token does not have sufficent permissions
            BackendException: Our backend didn't approve your request

        Returns:
            bool: Modified succesfully
        """
        if(domain.endswith(".frii.site")): 
            raise InvalidDomain(f"Your domain seems to end in .frii.site. The `domain` field should ignore the .frii.site suffix ({domain}->{domain[:-10]})")
        if(type.upper() not in self.allowed_types): raise InvalidType(f"Your type ({type.upper()}) is not in the supported list ({self.allowed_types})")
        headers_:dict = {
            "Content-Type":"application/json",
            "X-Api-Key":self.api_key
        }
        body_:dict = {
            "domain":domain,
            "content":content,
            "type":type.upper()
        }
        request_response:Response = patch(f"{self.url}/modify-domain")
        if(request_response.status_code==200): return True
        
        exceptions:dict = {
            403: InvalidPerms("Your API token does not have the sufficent permissions."),
            422: InvalidDomain("Your domain is invalid."),
            500: BackendException("Our backend did not approve of the request.")
        }
        
        raise exceptions.get(request_response.status_code)
        return False