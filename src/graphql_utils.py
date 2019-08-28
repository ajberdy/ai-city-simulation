from sgqlc.endpoint.http import HTTPEndpoint

url = 'https://ai-city-server.herokuapp.com'
headers = {'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJjanpxMmwx'
                            'bDhjdjN3MDc5NGFpZ2JqbjZnIiwiaWF0IjoxNTY2Njg0NTYyfQ.MEHsGyvdmR'
                            'Hj7zQh0t8b7FLXPf4Z_KbDcDeLlJ_Hbj8'
           }
endpoint = HTTPEndpoint(url, headers)