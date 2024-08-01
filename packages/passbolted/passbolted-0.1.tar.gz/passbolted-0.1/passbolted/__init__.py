import json

from passbolt import PassboltAPI


def get_credentials(key_fd, passphrase, search_name):
    key = key_fd.read()
    config = {
        "base_url": "https://pass.getnitro.co.in",
        "private_key": key,
        "passphrase": passphrase,
    }

    p = PassboltAPI(dict_config=config)

    resource = next((item for item in p.get_resources() if item["name"] == search_name), None)

    if resource is not None:
        res = (
            config.get("gpg_library", "PGPy") == "gnupg"
            and json.loads(p.decrypt(p.get_resource_secret(resource["id"])).data)
            or json.loads(p.decrypt(p.get_resource_secret(resource["id"])))
        )

        username = resource.get("username")
        res["username"] = username
        return res


