#!/usr/bin/env python
import os
import sys
import json
import getpass

from lesspass import lesspass

LESSPASS_PROFILES_DIR='~/.lesspass'

def load_profile(name):
    dir_path = os.path.expanduser(LESSPASS_PROFILES_DIR)
    profile_path = os.path.join(dir_path, "{}.json".format(name))

    with open(profile_path, 'r') as f:
        profile = json.loads(f.read())
        return profile

    return None

def main(site, login, profile = None):
    try:
        user_profile = load_profile(profile) if profile else None
        password_profile = lesspass._get_password_profile(user_profile)
        master_password = getpass.getpass("LessPass Master Password: ")
        password = lesspass.generate_password(site, login,
                                              master_password, password_profile)
        print(password)
    except KeyboardInterrupt:
        print("Program stopped by user!", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as err:
        print("Profile {} not found!".format(profile), file=sys.stderr)
        sys.exit(1)
    except:
        print("An error occurred!", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 3:
        print("Usage: {} [profile] website login".format(sys.argv[0]),
              file=sys.stderr)
        sys.exit(1)
    if argc == 3:
        main(*sys.argv[1:])
    else:
        main(sys.argv[2], sys.argv[3], sys.argv[1])
