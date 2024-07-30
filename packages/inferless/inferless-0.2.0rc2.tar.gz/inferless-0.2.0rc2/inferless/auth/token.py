from inferless_cli.utils.services import decrypt_tokens


def get_access_token():
    access_token, _, _, _, _ = decrypt_tokens()
    return access_token


def auth_header():
    try:
        access_token = get_access_token()
        token_header = {"Authorization": f"Bearer {access_token}"}
        return token_header
    except Exception as e:
        print("Unable to fetch the credentials. Please login with inferless-cli. Follow instructions at "
              "https://docs.inferless.com/model-import/cli-import")
        raise SystemExit
