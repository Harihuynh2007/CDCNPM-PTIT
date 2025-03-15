# TodoManager Automated Testing Scenario Report

## 1. Introduction

### 1.1 Project Overview
The TodoManager is a web-based task management application that allows users to manage their tasks through a simple and intuitive interface. The application provides functionality for user authentication, task creation, task deletion, and other task management features.

### 1.2 Test Objectives
- Verify the user authentication functionality (login/logout)
- Validate task management operations (adding and deleting tasks)
- Ensure the application handles various user inputs appropriately
- Confirm system stability across different operations

### 1.3 Testing Environment
- **Frontend**: HTML, CSS, JavaScript
- **Testing Tools**: Python with Selenium WebDriver
- **Browser**: Microsoft Edge
- **Test Framework**: Python unittest

## 2. Test Scenarios

### 2.1 User Authentication Testing

#### 2.1.1 Successful Login (Test Case ID: TC001)
**Description**: This test verifies that users can successfully log in to the application using valid credentials.

**Test Steps**:
1. Navigate to the login page (http://127.0.0.1:5500/login.html)
2. Enter valid email address (tanhaorn@gmail.com)
3. Enter valid password (123456ae)
4. Click the login button
5. Verify successful redirection to the dashboard page

**Expected Results**: 
- User should be redirected to the application dashboard (index.html)
- The page title should contain "TodoManager"

**Automation Script Reference**: test1_login.py

#### 2.1.2 Failed Login - Invalid Password (Test Case ID: TC002)
**Description**: This test verifies that the system correctly handles login attempts with invalid credentials.

**Test Steps**:
1. Navigate to the login page
2. Enter valid email address (tanhaorn@gmail.com)
3. Enter invalid password ("wrongpassword")
4. Click the login button
5. Verify the error message display

**Expected Results**: 
- User remains on the login page
- Error message is displayed indicating invalid credentials

**Automation Script Reference**: test5_login_fail.py

#### 2.1.3 Successful Logout (Test Case ID: TC003)
**Description**: This test verifies that users can successfully log out of the application.

**Test Steps**:
1. Login to the application with valid credentials
2. Verify successful login
3. Click the logout button
4. Verify return to login page

**Expected Results**: 
- User should be redirected back to the login page
- Login form elements should be visible

**Automation Script Reference**: test4_logout.py

### 2.2 Task Management Testing

#### 2.2.1 Add New Task (Test Case ID: TC004)
**Description**: This test verifies that users can successfully create a new task.

**Test Steps**:
1. Login to the application with valid credentials
2. Click the "+" button in the "To do" board
3. Complete the task creation form with the following details:
   - Title: "Học Selenium"
   - Category: "Kiểm thử"
   - Description: "Làm bài tập kiểm thử tự động"
   - Due Date: Next day (dynamically calculated)
4. Click the save button
5. Verify the task appears in the "To do" list

**Expected Results**: 
- Task creation form should appear when "+" button is clicked
- Form should accept all the required inputs
- Task should be saved successfully and appear in the task list

**Automation Script Reference**: test2_add_task.py

#### 2.2.2 Delete Task (Test Case ID: TC005)
**Description**: This test verifies that users can successfully delete an existing task.

**Test Steps**:
1. Login to the application with valid credentials
2. Verify that tasks exist in the system
3. Locate a specific task with the title "Học Selenium"
4. Click the delete (trash) icon for the task
5. Verify the task is removed from the list

**Expected Results**: 
- The task should be successfully deleted
- The task should no longer appear in the task list

**Automation Script Reference**: test3_delete.py

## 3. Test Implementation

### 3.1 Technology Stack
- **Programming Language**: Python 3
- **Testing Framework**: unittest
- **Browser Automation**: Selenium WebDriver
- **Browser**: Microsoft Edge WebDriver
- **Wait Strategies**: Explicit waits with WebDriverWait and Expected Conditions

### 3.2 Implementation Challenges
- **Page Loading**: Implemented explicit waits to handle dynamic page loading
- **Element Visibility**: Used appropriate wait conditions to ensure elements are visible before interaction
- **JavaScript Execution**: Utilized JavaScript executor for clicking certain elements to bypass potential click interception
- **Test Data Management**: Implemented dynamic date calculation for task due dates

### 3.3 Key Implementation Patterns
- **Page Object Model**: Structured the tests using class-based approach with proper setup and teardown
- **Explicit Waits**: Used WebDriverWait with appropriate conditions for reliable element interaction
- **Test Isolation**: Implemented cookie deletion between tests to ensure isolation
- **Error Handling**: Added proper validation and error messages for better debugging

## 4. Test Results

### 4.1 Summary
| Test Case ID | Test Case Description | Status | Notes |
|--------------|----------------------|--------|-------|
| TC001 | Successful Login | Pass | Successfully verified login functionality |
| TC002 | Failed Login - Invalid Password | Pass | Correctly handled invalid credentials |
| TC003 | Successful Logout | Pass | Successfully verified logout functionality |
| TC004 | Add New Task | Pass | Successfully added a new task |
| TC005 | Delete Task | Pass | Successfully deleted an existing task |

### 4.2 Observations
- The application consistently performs user authentication operations
- Task management functionality works as expected
- The UI elements are reliably accessible via Selenium WebDriver
- All tests execute within an acceptable timeframe

### 4.3 Recommendations
- Implement additional test cases for edge scenarios (e.g., empty fields, special characters)
- Add test coverage for task editing functionality
- Consider adding test cases for task filtering and searching
- Implement cross-browser testing for broader compatibility verification

## 5. Conclusion
The automated testing implementation demonstrates the reliability and functionality of the TodoManager application. The test suite covers the core functionality of user authentication and task management operations. The application successfully passed all test cases, indicating a stable implementation of the required features.

Future test development should focus on expanding coverage to include additional edge cases and feature enhancements.

## 6. Appendices

### 6.1 Test Automation Code Structure
```
└── Tests/
    ├── test1_login.py            # Login success test
    ├── test2_add_task.py         # Add task test
    ├── test3_delete.py           # Delete task test
    ├── test4_logout.py           # Logout test
    └── test5_login_fail.py       # Login failure test
```

### 6.2 Test Execution Instructions
1. Ensure the TodoManager application is running on http://127.0.0.1:5500
2. Install the required dependencies: `pip install selenium`
3. Download and configure Microsoft Edge WebDriver
4. Execute tests individually: `python test1_login.py`
5. Alternatively, use a test runner to execute all tests: `python -m unittest discover -p "test*.py"`

### 6.3 References
- Selenium WebDriver Documentation: https://www.selenium.dev/documentation/webdriver/
- Python unittest Documentation: https://docs.python.org/3/library/unittest.html
