#!/usr/bin/python3


""" Library to gather data from API """

import requests
import sys

""" Function to gather data from API """

def get_employee_todo_progress(employee_id):
    # Fetch employee data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        # Get employee information
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        employee_data = user_response.json()
        employee_name = employee_data.get('name')

        # Get TODO list for the employee
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Calculate progress
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task['completed']]
        num_completed = len(completed_tasks)

        # Display progress
        print(f"Employee {employee_name} is done with tasks({num_completed}/{total_tasks}):")
        
        # Display completed task titles
        for task in completed_tasks:
            print(f"\t {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
    except (KeyError, ValueError) as e:
        print(f"Error processing data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    get_employee_todo_progress(employee_id)
