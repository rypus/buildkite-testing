import plistlib
import subprocess

def check_plist_keys():
    # Get profile changes in this PR
    command = [ "git", "diff", "--name-only", "main"]
    res = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='UTF-8')
    files = res.stdout.read().strip().split()

    if len(files) > 0:
        profiles_check_result = {'valid': [], 'invalid': []}
        for file in files:
            if file.startswith('config-profile/unsigned'):
                file_path = './' + file
                with open(file_path, 'rb') as infile:
                    plist = plistlib.load(infile)
                    required_keys = [ 'PayloadIdentifier', 'PayloadDisplayName', 'PayloadDescription' ]
                    res = all(key in plist.keys() for key in required_keys)
                    if res:
                        profiles_check_result['valid'].append(file.split('/')[-1])
                    else:
                        profiles_check_result['invalid'].append(file.split('/')[-1])
    if len(profiles_check_result['invalid']) > 0:
        print(f"Invalid profile found: {','.join(profiles_check_result['invalid'])}")
        assert len(profiles_check_result['invalid']) == 0


if __name__ == "__main__": 
    check_plist_keys()