from connect.connection import Connection
from connect import details as dtl

try:
    with Connection() as auto:
        # auto.check_setup()
        auto.open_and_input(username=dtl.USERNAME,password=dtl.PASSWORD)
        auto.quit()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    
    else:
        raise
