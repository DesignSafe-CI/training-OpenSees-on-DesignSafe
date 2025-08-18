def connect_tapis(token_filePath="~/.tapis_tokens.json", base_url="https://designsafe.tapis.io",
                  username="", password="", force_connect=False):
    """
    Connect to the Tapis platform with automatic token handling.

    - Checks for a saved access token in the specified token_filePath (default ~/.tapis_tokens.json).
    - If the token exists and is still valid, uses it to create an authenticated Tapis client.
    - If the token is expired, missing, or force_connect=True, prompts for username/password
      to generate a fresh token, then saves it for future use.
    - Prints out the token expiration details for transparency.

    Parameters:
        token_filePath (str): Path to the JSON file storing tokens.
        base_url (str): Tapis API endpoint URL.
        username (str): Optional preset username (prompts if empty).
        password (str): Optional preset password (prompts if empty).
        force_connect (bool): If True, forces a fresh login even if token is valid.

    Returns:
        Tapis: An authenticated Tapis client object ready to use.
    """

    # Silvia Mazzoni, 2025
    from tapipy.tapis import Tapis
    from getpass import getpass
    import os
    import json
    from datetime import datetime, timezone
    print(" -- Checking tapis Token --")
    validToken=False

    # Path to the saved tokens
    token_file = os.path.expanduser(token_filePath)

    now = datetime.now(timezone.utc)

    print(" Time now:",now)
    # Check if tokens exist
    if os.path.exists(token_file):
        with open(token_file, 'r') as f:
            tokens = json.load(f)
        print(" Token loaded from file.")
        expires_at = datetime.fromisoformat(tokens["expires_at"])


        # check if expired:
        if expires_at > now:
            print(" Token is still valid!")
            t = Tapis(base_url=base_url, access_token=tokens['access_token'])
            validToken=True
        else:
            print("Token has expired!")
            print(" Token Expired At:", expires_at)

    else:
        print("No saved tokens found!")

    if force_connect:
        print('Forcing a connection to Tapis')
    if not validToken or force_connect:
        print('-- Connect to Tapis --')
        if username == '':
            username = getpass('Username: ')
        if password == '':
            password = getpass('Password: ')
        t = Tapis(
          base_url = base_url,
          username = username,
          password = password)
        t.get_tokens()
        # Define a secure path to save the token
        token_file = os.path.expanduser("~/.tapis_tokens.json")
        # Save the access and refresh tokens in a JSON file
        tokens = {
            "access_token": t.access_token.access_token,
            "expires_at": t.access_token.expires_at.isoformat()
        }    #  Get the raw string, not the object
        with open(token_file, 'w') as f:
            json.dump(tokens, f)
        print(f" Token saved to {token_file}")
    expires_at_str = str(t.access_token.expires_at)
    print(" Token expires At:", t.access_token.expires_at)
    print(' Token expires In ',str(t.access_token.expires_at-now),' hh:mm:sec')
    print("-- LOG IN SUCCESSFUL!!! --")
    return t