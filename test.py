import time
import requests
import subprocess

BASE_URL = 'http://localhost:8080/ChatApplication/messages'
MESSAGE = 'Test message for testing'
RESTART_WAIT_TIME = 10  # Time to wait for server restart, adjust as needed

def time_behavior_fitness_function():
    print("Testing time behavior...")
    
    # Test POST response time
    start_time = time.time()
    response = requests.post(BASE_URL, data={'message': MESSAGE})
    post_response_time = time.time() - start_time
    if response.status_code != 200:
        return {'post_response_time': post_response_time, 'status': 'failed'}

    # Test GET response time
    start_time = time.time()
    response = requests.get(f'{BASE_URL}/count')
    get_response_time = time.time() - start_time
    if response.status_code != 200 or 'messageCount' not in response.json():
        return {'get_response_time': get_response_time, 'status': 'failed'}

    return {
        'post_response_time': post_response_time,
        'get_response_time': get_response_time,
        'status': 'passed'
    }

def recoverability_fitness_function():
    print("Testing server recoverability...")

    def post_message():
        requests.post(BASE_URL, data={'message': MESSAGE})

    def get_message_count():
        response = requests.get(f'{BASE_URL}/count')
        return response.json().get('messageCount')

    def simulate_server_crash():
        print("Simulating server crash...")
        crash_url = 'http://localhost:8080/ChatApplication/crash'
        start_time = time.time()
        try:
            requests.get(crash_url)  # Trigger the crash
        except requests.RequestException as e:
            print(f"Error simulating server crash: {e}")
        return time.time() - start_time

    post_message()
    initial_count = get_message_count()
    crash_time = simulate_server_crash()

    # Wait for server to recover
    print("Waiting for server to recover...")
    start_recovery_time = time.time()
    recovery_time = None
    while recovery_time is None:
        try:
            final_count = get_message_count()
            if final_count == initial_count:
                recovery_time = time.time() - start_recovery_time
            else:
                time.sleep(1)  # Wait before retrying
        except requests.RequestException:
            time.sleep(1)  # Wait before retrying

    return {
        'crash_time': crash_time,
        'recovery_time': recovery_time,
        'status': 'passed'
    }

def maintainability_fitness_function():
    print("Checking code complexity...")

    # Full path to the Checkstyle JAR file
    checkstyle_jar_path = 'C:/Users/ezeki/checkstyle-10.18.1-all.jar'
    command = ['java', '-jar', checkstyle_jar_path, '-c', 'google_checks.xml', 'src/main/java/com/chatapp']
    result = subprocess.run(command, capture_output=True, text=True)

    # Save the result in a file or process it as needed
    report_path = 'checkstyle_report.txt'
    with open(report_path, 'w') as file:
        file.write(result.stdout)
        if result.stderr:
            file.write("\nErrors:\n")
            file.write(result.stderr)

    return {
        'report_path': report_path,
        'status': 'completed'
    }

if __name__ == '__main__':
    # Run and print results for time behavior
    time_behavior_results = time_behavior_fitness_function()
    print(f"POST Response Time: {time_behavior_results['post_response_time']:.3f} seconds")
    print(f"GET Response Time: {time_behavior_results['get_response_time']:.3f} seconds")
    print(f"Status: {time_behavior_results['status']}")
    
    # Run and print results for recoverability
    recoverability_results = recoverability_fitness_function()
    print(f"Time to Simulate Crash: {recoverability_results['crash_time']:.3f} seconds")
    print(f"Time to Recover: {recoverability_results['recovery_time']:.3f} seconds")
    print(f"Status: {recoverability_results['status']}")

    # Run and print results for maintainability
    maintainability_results = maintainability_fitness_function()
    print(f"Checkstyle Report Saved To: {maintainability_results['report_path']}")
    print(f"Status: {maintainability_results['status']}")
