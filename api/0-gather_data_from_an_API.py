#!/usr/bin/env python3
"""
Retrieve and display an employee's TODO list progress from a REST API.

This script fetches employee data and their TODO list from JSONPlaceholder API,
then displays the progress of completed tasks in a specific format.
"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Fetch and display an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee whose TODO progress to check.

    Raises:
        requests.exceptions.RequestException: If API requests fail.
        ValueError: If employee_id is invalid or employee not found.
    """
    try:
        # Fetch employee details
        employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        response = requests.get(employee_url, timeout=10)
        response.raise_for_status()
        employee_data = response.json()
        employee_name = employee_data.get('name')

        if not employee_name:
            raise ValueError(f"No employee found with ID {employee_id}")

        # Fetch TODO list for the employee
        todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        response = requests.get(todos_url, timeout=10)
        response.raise_for_status()
        todos_data = response.json()

        # Calculate progress
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task['completed']]
        num_completed = len(completed_tasks)

        # Display progress
        print(f"Employee {employee_name} is done with tasks({num_completed}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")

    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(
            f"Failed to fetch data from API: {str(e)}"
        ) from e


def main():
    """Handle command-line arguments and execute the main functionality."""
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        if employee_id <= 0:
            raise ValueError("Employee ID must be a positive integer")
        get_employee_todo_progress(employee_id)
    except ValueError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"API Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
