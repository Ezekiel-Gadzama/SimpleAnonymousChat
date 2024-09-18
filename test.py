import time
import requests
import subprocess

BASE_URL = 'http://localhost:8080/ChatApplication/messages'
MESSAGE = 'Test message for testing'
RESTART_WAIT_TIME = 10  # Time to wait for server restart, adjust as needed

# Function to test time behavior
def test_time_behavior():
    print("Testing time behavior...")
    
    # Test POST response time
    start_time = time.time()
    response = requests.post(BASE_URL, data={'message': MESSAGE})
    end_time = time.time()
    response_time = end_time - start_time
    print(f'POST response time: {response_time:.3f} seconds')
    assert response.status_code == 200

    # Test GET response time
    start_time = time.time()
    response = requests.get(f'{BASE_URL}/count')
    end_time = time.time()
    response_time = end_time - start_time
    print(f'GET count response time: {response_time:.3f} seconds')
    assert response.status_code == 200
    assert 'messageCount' in response.json()

# Function to test recoverability
def test_recoverability():
    print("Testing server recoverability...")
    
    def post_message():
        response = requests.post(BASE_URL, data={'message': MESSAGE})
        return response

    def get_message_count():
        response = requests.get(f'{BASE_URL}/count')
        return response.json()['messageCount']

    # Post a message and get the message count
    post_message()
    initial_count = get_message_count()
    print(f'Initial message count: {initial_count}')

    # Simulate server restart
    print("Restarting server...")
    time.sleep(RESTART_WAIT_TIME)  # Adjust based on your server restart time

    # Verify message count after server restart
    final_count = get_message_count()
    print(f'Final message count: {final_count}')
    assert final_count == initial_count

# Function to check code complexity (for Java code)
def check_code_complexity():
    print("Checking code complexity...")

    # Full path to the Checkstyle JAR file
    checkstyle_jar_path = 'C:/Users/ezeki/checkstyle-10.18.1-all.jar'

    # Run Checkstyle with the full path to the JAR file
    command = ['java', '-jar', checkstyle_jar_path, '-c', 'google_checks.xml', 'src/main/java/com/chatapp']
    result = subprocess.run(command, capture_output=True, text=True)

    print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)

if __name__ == '__main__':
    test_time_behavior()
    test_recoverability()
    check_code_complexity()
