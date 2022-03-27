from typing import Iterator, Dict
import requests


def get_hostnames() -> Iterator[str]:
    with open("./shellies.txt") as f:
        for line in f.readlines():
            yield line.strip()


def get_ota_info(hostname: str) -> Dict:
    response = requests.get(f"http://{hostname}/ota")
    if not response.ok:
        response.raise_for_status()
    return response.json()


def do_ota_update(hostname: str) -> Dict:
    response = requests.get(f"http://{hostname}/ota", params={"update": True})
    if not response.ok:
        response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    for hostname in get_hostnames():
        print(f"Checking {hostname}")
        try:
            ota_info = get_ota_info(hostname)
        except requests.exceptions.ConnectionError:
            print(f"  cannot connect to {hostname}, skipping")
            continue
        if not ota_info["has_update"]:
            print(f"  is up to date, running {ota_info['old_version']}")
        else:
            print(
                f"  needs update, {ota_info['old_version']} -> {ota_info['new_version']}"
            )
            update_info = do_ota_update(hostname)
            if update_info["status"] == "updating":
                print("  update in progress")
            else:
                print("  unknown response")
                print(update_info)
                break
