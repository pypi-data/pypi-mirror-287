import sys
import json
from .disconnect import disconnect
from .get_websocket import get_websocket

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'


# Function to get the status of a single test
async def waiter(websocket, job_id, spinner):
    # Start the spinner thread
    spinner.start()

    try:
        # Send a request to listen for test status updates
        await websocket.send(json.dumps({'action': 'jobStatus', 'jobId': job_id}))

        # Listen for test status updates
        # while True:
        #     status_update = await websocket.recv()
        #     json_response = json.loads(status_update)
        #     json_body = json.loads(json_response.get('body', '{}'))

        #     message = json_body.get('message', None)

        #     if message:
        #         status = message.split(' | ')[1]
        #         msg_string = message.split(' | ')[2]

        #     errorMessage = json_body.get('errorMessage', None)

        #     if errorMessage:
        #         sys.stdout.write('\r' + ' ' * 80 + '\r')  # Clear the line
        #         print(f'Error: {errorMessage}')
        #         await disconnect(get_websocket())
        #         sys.exit(1)
        #     else:
        #         if msg_string == 'complete':
        #             sys.stdout.write('\r' + ' ' * 80 + '\r')  # Clear the line
        #             print('Test complete')
        #             break
        #         elif status == 'failed':
        #             sys.stdout.write('\r' + ' ' * 80 + '\r')  # Clear the line
        #             print(message)
        #             sys.exit(1)
        #         else:
        #             sys.stdout.write('\r' + ' ' * 80 + '\r')  # Clear the line
        #             print(message)
        # Listen for test status updates
        while True:
            status_update = await websocket.recv()
            json_response = json.loads(status_update)
            json_body = json.loads(json_response.get('body', '{}'))

            message = json_body.get('message', None)
            error_message = json_body.get('errorMessage', None)

            if error_message:
                sys.stdout.write(f'\r{RED}Error: {error_message}{RESET}\r')
                sys.stdout.flush()
                await disconnect(get_websocket())
                sys.exit(1)
            elif message:
                date, status, msg_string = message.split(' | ')
                status_with_color = f"\r{GREEN}passed{RESET}" if status == "passed" else f"{RED}failed{RESET}\r"

                if msg_string == 'complete':
                    print('Test complete')
                    break
                elif status == 'failed':
                    sys.stdout.write(f"\r{date} | {status_with_color} | {msg_string}\r")
                    sys.stdout.flush()
                    sys.exit(1)
                else:
                    sys.stdout.write(f"\r{date} | {status_with_color} | {msg_string}", end="\r", flush=True)
    except Exception as e:
        sys.stdout.write(f"\r{RED}Error: {e}{RESET}\r")
        sys.exit(1)
    finally:
        spinner.stop()
        spinner.join()
