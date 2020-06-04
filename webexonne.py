from webexteamssdk import WebexTeamsAPI


# Create a WebexTeamsAPI connection object; uses your WEBEX_TEAMS_ACCESS_TOKEN
# environment variable
api = WebexTeamsAPI()


# Get my user information
print("Get my information ...")
me = api.people.me()
print(me)



# Get my user information using my id
print("Get my information but using id ...")
me_by_id = api.people.get(me.id)
print(me_by_id)


class Person(ImmutableData, PersonBasicPropertiesMixin):
    """Webex Teams Person data model."""