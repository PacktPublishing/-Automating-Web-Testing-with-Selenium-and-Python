# Creating a testing suite 

Example web app: https://opensource-demo.orangehrmlive.com

## TC (Test Case) definitions 

| TCID | TC Name | Description | 
| --- | --- | --- | 
| [TC_L_001](#TC_L_001) | Login page loaded | Checking if the key elements on the page are loaded. Login fields and login button. | 
| [TC_L_002](#TC_L_002) | Successful login | Using correct username and pass and verifying succseful login. |  
| [TC_L_003](#TC_L_003) | Failed login | Using incorrect password and verifying the error message for failed login. |
| [TC_A_001](#TC_A_001) | Add new job title | Navigating to Admin > Job > Job Titles and fill in the form to add new job title. |  
| [TC_A_002](#TC_A_002) | Add new work shift | Navigating to Admin > Job > Work Shifts and add new work shift. |  
---

### Login TCs

Username : Admin | Password : admin123


| TCID | TC Name | Description | 
| --- | --- | --- | 
| TC_L_001 <a name="TC_L_001"></a> | Login page loaded | Checking if the key elements on the page are loaded. Login fields and login button. |  

```yaml
Preconditions:
  - None
Steps:
  1. Verify Login panel exists 
  2. Verify Username input filed exists 
  3. Verify Password field exists 
  4. Verify Login button exists and enabled for clicking 
Expected results: >
    All test steps passed as excepted. 
```

| TCID | TC Name | Description | 
| --- | --- | --- | 
| TC_L_002 <a name="TC_L_002"></a> | Successful login | Using correct username and pass and verifying succseful login. |  

```yaml
Preconditions:
  - None
Steps:
  1. Enter user name Admin in the username field
  2. Enter passerod admin123 in password field 
  3. Click on the Login button 
  4. Verify correct redirection to Dashboard - correct url 
  5. Verify that Dashboard is loaded 
Expected results: >
    Login successful and after login, redirected to Dashboard page. 
```

| TCID | TC Name | Description | 
| --- | --- | --- | 
| TC_L_003 <a name="TC_L_003"></a> | Failed login | Using incorrect password and verifying the error message for failed login. |  

```yaml
Preconditions:
  - None
Steps:
  1. Enter user name Admin in the username field
  2. Enter passerod password in password field 
  3. Verify the correct message is displayed  
Expected results: >
    All test steps passed as excepted. 
```

---


### Admin TCs

| TCID | TC Name | Description | 
| --- | --- | --- | 
| TC_A_001 <a name="TC_A_001"></a> | Add new job title | Navigating to Admin > Job > Job Titles and fill in the form to add new job title. |  

```yaml
Preconditions:
  - Login succesful
Steps:
  1. Navigate to Admin > Job > Job Titles
  2. Click on the button Add 
  3. Enter as job title: QA automation developer
  4. Enter as job description: Automating tests in Python and Selenium Webdriver. 
  5. Click on button Save
  6. Verify that new job title with description is on the list 
Expected results: >
    All test steps passed as excepted. 
```

| TCID | TC Name | Description | 
| --- | --- | --- | 
| TC_A_002 <a name="TC_A_002"></a> | Add new work shift | Navigating to Admin > Job > Work Shifts and add new work shift. |  

```yaml
Preconditions:
  - Login succesful
Steps:
  1. Navigate to Admin > Job > Work Shifts
  2. Click on the button Add 
  3. Enter as shift title: QA short shift
  4. From work hours select from 9:00 to 13:00  
  5. Click on button Save
  6. Verify that new job title with description is on the list 
Expected results: >
    All test steps passed as excepted. 
```


