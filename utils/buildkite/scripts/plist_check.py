import plistlib

def check_plist_keys():
    file = "/Users/rypus/Code/github/repos/rypus/buildkite-testing/config-profile/software-update-setting.mobileconfig"
    with open(file, 'rb') as infile:
        plist = plistlib.load(infile)

    required_keys = [ 'PayloadIdentifier', 'PayloadDisplayName', 'PayloadDescription' ]
    assert all(key in plist.keys() for key in required_keys)

if __name__ == "__main__": 
    check_plist_keys()