from requests import Response, patch, post
from typing import List
from .perms import permission
from .exceptions import InvalidDomain, InvalidType, InvalidPerms, BackendException
class API:
    
    @staticmethod
    def create(auth_token:str, domains: List[str], perms:List[permission],comment:str) -> str:
        __permissions = []
        for perm in perms:
            __permissions.append(perm.value)
        body_:dict = {
            "domains":domains,
            "perms":__permissions,
            "comment":comment
        }
        headers_:dict = {
            "Content-Type":"application/json",
            "X-Auth-Token":auth_token
        }
        request_response:Response = post("https://api.frii.site/create-api",data=body_,headers=headers_)
        if(request_response.status_code==200): return request_response.text()
        return ""
    
    def __init__(self,api_key:str,url_override:str|None=None) -> None:
        self.api_key=api_key.strip()
        self.url = "https://api.frii.site" or url_override
        self.allowed_types:list=["A","CNAME","TXT","NS"]
        
    def modify(self,domain:str,content:str,type_:str) -> bool:
        """Modify a domain

        Args:
            domain (str): the domain (without the .frii.site part)
            content (str): the new content of the domain
            type_ (str):  the new type of the domain

        Raises:
            InvalidDomain: If your domain is invalid
            InvalidPerms: Your API token does not have sufficent permissions
            BackendException: Our backend didn't approve your request

        Returns:
            bool: Modified succesfully
        """
        if(domain.endswith(".frii.site")): 
            raise InvalidDomain(f"Your domain seems to end in .frii.site. The `domain` field should ignore the .frii.site suffix ({domain}->{domain[:-10]})")
        if(type_.upper() not in self.allowed_types): raise InvalidType(f"Your type ({type_.upper()}) is not in the supported list ({self.allowed_types})")
        headers_:dict = {
            "Content-Type":"application/json",
            "X-Api-Key":self.api_key
        }
        body_:dict = {
            "domain":domain,
            "content":content,
            "type":type_.upper()
        }
        request_response:Response = patch(f"{self.url}/modify-domain",headers=headers_,data=body_)
        if(request_response.status_code==200): return True
        
        if(request_response.status_code==403):
            raise InvalidPerms("Your API token does not have the sufficent permissions.")
        if(request_response.status_code==422):
            raise InvalidDomain("Your domain is invalid.")
        if(request_response.status_code==500):
            raise BackendException("Our backend did not approve of the request.")
        return False