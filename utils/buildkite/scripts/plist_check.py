import plistlib
import subprocess
from os import path

def check_plist_keys():
    # define required key for profiles
    required_keys = [ 'PayloadIdentifier', 'PayloadDisplayName', 'PayloadDescription' ]

    # Get profile changes in this PR
    command = [ "git", "diff", "--name-only", "main"]
    try: 
        res = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='UTF-8')
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        raise e
    
    files = res.stdout.read().strip().split()
    print(files)

    if len(files) > 0:
        profiles_check_result = {'valid': [], 'invalid': []}
        for file in files:
            if file.startswith('config-profile/unsigned') and path.splitext(file) == 'mobileconfig':
                file_path = path.join('./',file)
                file_name = file.split('/')[-1]
                with open(file_path, 'rb') as infile:
                    plist = plistlib.load(infile)
                    res = all(key in plist.keys() for key in required_keys)
                    if res:
                        profiles_check_result['valid'].append(file_name)
                    else:
                        profiles_check_result['invalid'].append(file_name)

        if len(profiles_check_result['invalid']) > 0:
            print(f"* Invalid profile found: {','.join(profiles_check_result['invalid'])}")
            assert len(profiles_check_result['invalid']) == 0
        else:
            print("Profiles check pass.")



if __name__ == "__main__": 
    check_plist_keys()